import React from 'react';

const DocumentList = ({ documents }) => (
  <div>
    {documents.map(doc => (
      <div key={doc.id} style={{ border: '1px solid gray', margin: '10px', padding: '10px' }}>
        <h4>{doc.title || 'Untitled'}</h4>
        <p>{doc.text}</p>
        <small>{new Date(doc.uploaded_at).toLocaleString()}</small>
      </div>
    ))}
  </div>
);

export default DocumentList;
