import '../css/CurrentWeather.css'

/**
 * CurrentWeather
 * Props:
 *  - data: the `current` object returned by the API
 */
export default function CurrentWeather({ data }) {
  if (!data) return null

  const iconUrl = `https://openweathermap.org/img/wn/${data.icon}@2x.png`

  return (
    <section className="current-weather glass-card">
      <div className="current-weather-top">
        <div>
          <h2 className="current-city">
            {data.city}, {data.country}
          </h2>
          <p className="current-time">Local time: {data.local_time}</p>
        </div>
        <img src={iconUrl} alt={data.description} className="current-icon" />
      </div>

      <div className="current-weather-main">
        <span className="current-temp">{data.temperature}°C</span>
        <div className="current-meta">
          <p className="current-description">{data.description}</p>
          <p className="current-feels-like">Feels like {data.feels_like}°C</p>
        </div>
      </div>
    </section>
  )
}
