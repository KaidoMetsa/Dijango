import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';   
// Adjust the URL based on your backend configuration

export const uploadImage = (formData) => axios.post(`${API_URL}upload/`, formData);
export const getDocuments = () => axios.get(`${API_URL}documents/`);