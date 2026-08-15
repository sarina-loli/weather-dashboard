import '../css/Navbar.css'

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-brand">
        <svg
          className="navbar-icon"
          width="26"
          height="26"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.8"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <path d="M17.5 19H8a5 5 0 1 1 1.3-9.8A6 6 0 0 1 21 12.5a4.5 4.5 0 0 1-3.5 6.5Z" />
        </svg>
        <span className="navbar-title">Weather Dashboard</span>
      </div>
    </header>
  )
}
