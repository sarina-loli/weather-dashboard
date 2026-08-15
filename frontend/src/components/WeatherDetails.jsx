import WeatherCard from './WeatherCard.jsx'
import { DropletIcon, WindIcon, GaugeIcon, EyeIcon, SunriseIcon, SunsetIcon } from './Icons.jsx'
import '../css/WeatherDetails.css'

/**
 * WeatherDetails
 * Renders the grid of secondary weather stats using the reusable
 * WeatherCard component. Icons are inline SVGs (see Icons.jsx) rather
 * than emoji, so they always render in the site's 3-color palette.
 *
 * Props:
 *  - data: the `current` object returned by the API
 */
export default function WeatherDetails({ data }) {
  if (!data) return null

  return (
    <section className="weather-details">
      <WeatherCard icon={<DropletIcon />} label="Humidity" value={`${data.humidity}%`} />
      <WeatherCard icon={<WindIcon />} label="Wind Speed" value={`${data.wind_speed} m/s`} />
      <WeatherCard icon={<GaugeIcon />} label="Pressure" value={`${data.pressure} hPa`} />
      <WeatherCard icon={<EyeIcon />} label="Visibility" value={`${data.visibility} km`} />
      <WeatherCard icon={<SunriseIcon />} label="Sunrise" value={data.sunrise} />
      <WeatherCard icon={<SunsetIcon />} label="Sunset" value={data.sunset} />
    </section>
  )
}
