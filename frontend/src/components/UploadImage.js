import React, { useState } from 'react';
import { uploadImage } from '../api/api';

const UploadImage = ({ onUpload }) => {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('image', file);
    const res = await uploadImage(formData);
    onUpload(res.data);
  };

  return (
    <div>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default UploadImage;
