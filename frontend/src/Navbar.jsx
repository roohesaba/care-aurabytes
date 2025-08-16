import { Link } from "react-router-dom";
import "./Navbar.css";

export default function Navbar() {
  return (
    <nav className="navbar">
      {/* Left: logo */}
      <div className="logo">
        <Link to="/" className="logo">
          <img src="/logo.png" alt="Care Logo" className="logo-img" />
        </Link>
      </div>

      {/* Right: links */}
      <ul className="nav-links">
        <li><Link to="/">Homepage</Link></li>
        <li><Link to="/about">About us</Link></li>
        <li><Link to="/contact">Contact</Link></li>
      </ul>
    </nav>
  );
}
