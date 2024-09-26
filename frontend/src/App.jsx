import React, { useState } from 'react';
import UploadBook from './components/UploadBook.jsx';
import BookReader from './components/BookReader.jsx';
import HighlightPopUp from './components/HighlightPopUp.jsx';
import './App.css';

function App() {
  const [bookText, setBookText] = useState('');
  const [similarSentences, setSimilarSentences] = useState([]);

  // Handle book upload
  const handleUpload = (text) => {
    setBookText(text);
  };

  // Handle sentence highlight
  const handleHighlight = (sentences) => {
    setSimilarSentences(sentences);
  };

  return (
    <div className="App container mx-auto p-8">    
          
      <h1 className="text-4xl font-bold text-gray-800 text-center mb-8">Book Embedding Referencer</h1>
      <UploadBook onUpload={handleUpload} />
      {bookText && <BookReader content={bookText} />}
    </div>
  );
}

export default App;
