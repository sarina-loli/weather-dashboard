import '../css/Loader.css'

export default function Loader() {
  return (
    <div className="loader-wrapper" role="status" aria-live="polite">
      <div className="loader-spinner"></div>
      <p className="loader-text">Fetching weather data...</p>
    </div>
  )
}
