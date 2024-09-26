// src/components/UploadBook.js
import React, { useState } from 'react';
import axios from 'axios';

function UploadBook({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:5000/upload-book', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      const data = response.data.book_text;
      onUpload(data);  // Assuming backend returns sentence list
      alert('Book uploaded successfully!');
    } catch (error) {
      console.error('Error uploading book:', error);
    }
  };

  return (
    <div className="my-4">
      <input type="file" onChange={handleFileChange} className="p-2 border border-gray-300 rounded-lg" />
      <button onClick={handleUpload} className="ml-4 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
        Upload Book
      </button>
    </div>
  );
}

export default UploadBook;
