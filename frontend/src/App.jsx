import { useState, useEffect } from 'react';
import FileList from './FileList';

export default function App() {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/files')
      .then(res => res.json())
      .then(data => setFiles(data))
      .catch(err => console.error('Error fetching files:', err));
  }, []);

  return (
  <div style={{ paddingTop: 80, paddingLeft: 16, paddingRight: 16 }}>
    <FileList files={files} />
  </div>
);
}
