import '../css/Footer.css'

export default function Footer() {
  return (
    <footer className="footer">
      <p>© {new Date().getFullYear()} Weather Dashboard — Powered by OpenWeatherMap</p>
    </footer>
  )
}
