import '../css/Forecast.css'

/**
 * Forecast
 * Renders the 5-day forecast summary.
 *
 * Props:
 *  - daily: array of { date, day_name, temp_min, temp_max, icon, description }
 */
export default function Forecast({ daily }) {
  if (!daily || daily.length === 0) return null

  return (
    <section className="forecast-section">
      <h3 className="forecast-heading">5-Day Forecast</h3>
      <div className="daily-list">
        {daily.map((day, idx) => (
          <div className="daily-item glass-card" key={idx}>
            <p className="daily-day">{day.day_name}</p>
            <img
              src={`https://openweathermap.org/img/wn/${day.icon}.png`}
              alt={day.description}
              className="daily-icon"
            />
            <p className="daily-description">{day.description}</p>
            <p className="daily-temps">
              <span className="daily-max">{day.temp_max}°</span>
              <span className="daily-min"> / {day.temp_min}°</span>
            </p>
          </div>
        ))}
      </div>
    </section>
  )
}
