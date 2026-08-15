import '../css/WeatherCard.css'

/**
 * WeatherCard
 * A small reusable "glass" card used to display a single weather
 * statistic (label + value), e.g. Humidity: 64%.
 *
 * Props:
 *  - label: string
 *  - value: string | number
 *  - icon: optional string/emoji shown above the label
 */
export default function WeatherCard({ label, value, icon }) {
  return (
    <div className="weather-card glass-card">
      {icon && <span className="weather-card-icon">{icon}</span>}
      <p className="weather-card-value">{value}</p>
      <p className="weather-card-label">{label}</p>
    </div>
  )
}
