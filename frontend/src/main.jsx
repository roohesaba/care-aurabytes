import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './index.css';

import Navbar from './Navbar';
import App from './App';
import About from './About';
import Contact from './Contact';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Router>
      <Navbar /> {/* Always visible */}
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Router>
  </StrictMode>
);
