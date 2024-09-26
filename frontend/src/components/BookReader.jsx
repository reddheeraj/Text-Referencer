import React, { useState } from 'react';
import axios from 'axios';
import HighlightPopUp from './HighlightPopUp';

function BookReader({ content, onHighlight }) {
    const [highlightedText, setHighlightedText] = useState('');
    const [similarSentences, setSimilarSentences] = useState([]);
    const [anchorEl, setAnchorEl] = useState(null);


    const handleMouseUp = async () => {
    const selection = window.getSelection().toString();
    if (selection) {
        
        setHighlightedText(selection);
        const rect = window.getSelection().getRangeAt(0).getBoundingClientRect();
        const top = window.scrollY;
        const left = window.scrollX;
        setAnchorEl({
            getBoundingClientRect: () => ({
              top: top,
              left: left,
              bottom: rect.bottom + window.scrollY,
              right: rect.right + window.scrollX,
              width: rect.width,
              height: rect.height,
            }),
        });
    
        try {
            const response = await axios.post('http://127.0.0.1:5000/similar-sentences', {
            sentence: selection,
            });
            console.log(response.data.similar_sentences);
            setSimilarSentences(response.data.similar_sentences);

            // onHighlight(response.data.similar_sentences);
        } catch (error) {
            console.error('Error fetching similar sentences:', error);
        }
    }
    else {
        setAnchorEl(null);  // Hide the pop-up if no text is selected
        setSimilarSentences([]);
    }
  };

  const handleClose = () => {
    setAnchorEl(null);
    setSimilarSentences([]);
  };

  return (
    <div className="book-reader bg-gray-100 p-4 rounded-lg shadow-lg my-4" onMouseUp={handleMouseUp}>
      <p className="whitespace-pre-line">{content}</p>
      <HighlightPopUp sentences={similarSentences} anchorEl={anchorEl} onClose={handleClose} />
    </div>
  );
}

export default BookReader;
