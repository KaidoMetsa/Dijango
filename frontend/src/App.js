import React, { useState, useEffect } from 'react';
import UploadImage from './components/UploadImage';
import DocumentList from './components/DocumentList';
import { getDocuments } from './api/api';

function App() {
  const [documents, setDocuments] = useState([]);

  useEffect(() => {
    fetchDocuments();
  }, []);

  const fetchDocuments = async () => {
    const res = await getDocuments();
    setDocuments(res.data);
  };

  const handleUpload = (newDoc) => {
    setDocuments([newDoc, ...documents]);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>OCR Library</h1>
      <UploadImage onUpload={handleUpload} />
      <DocumentList documents={documents} />
    </div>
  );
}

export default App;
