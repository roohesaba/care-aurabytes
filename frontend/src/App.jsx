import { useState, useEffect } from 'react';
import Navbar from './Navbar';
import FileList from './FileList';

export default function App() {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/files')
      .then(res => res.json())
      .then(data => setFiles(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <Navbar />
      <h4>Care.</h4>
      <FileList files={files} />
    </div>
  );
}
