import '../css/Forecast.css'

/**
 * HourlyForecast
 * Props:
 *  - hourly: array of { time, temperature, icon, description }
 */
export default function HourlyForecast({ hourly }) {
  if (!hourly || hourly.length === 0) return null

  return (
    <section className="forecast-section">
      <h3 className="forecast-heading">Hourly Forecast</h3>
      <div className="hourly-scroll">
        {hourly.map((hour, idx) => (
          <div className="hourly-item glass-card" key={idx}>
            <p className="hourly-time">{hour.time}</p>
            <img
              src={`https://openweathermap.org/img/wn/${hour.icon}.png`}
              alt={hour.description}
              className="hourly-icon"
            />
            <p className="hourly-temp">{hour.temperature}°C</p>
          </div>
        ))}
      </div>
    </section>
  )
}
