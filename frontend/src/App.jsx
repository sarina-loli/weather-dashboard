import { useState, useEffect } from 'react'
import Navbar from './components/Navbar.jsx'
import SearchBar from './components/SearchBar.jsx'
import CurrentWeather from './components/CurrentWeather.jsx'
import WeatherDetails from './components/WeatherDetails.jsx'
import HourlyForecast from './components/HourlyForecast.jsx'
import Forecast from './components/Forecast.jsx'
import Loader from './components/Loader.jsx'
import ErrorMessage from './components/ErrorMessage.jsx'
import Footer from './components/Footer.jsx'
import { fetchWeatherByCity } from './services/weatherService.js'
import './App.css'

const LAST_CITY_KEY = 'weather-dashboard:last-city'

export default function App() {
  const [weather, setWeather] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSearch = async (city) => {
    setLoading(true)
    setError('')
    try {
      const data = await fetchWeatherByCity(city)
      setWeather(data)
      localStorage.setItem(LAST_CITY_KEY, city)
    } catch (err) {
      setError(err.message)
      setWeather(null)
    } finally {
      setLoading(false)
    }
  }

  // On first mount, automatically reload whichever city the user last
  // searched for (stored in localStorage), so refreshing the page
  // doesn't leave them on a blank dashboard.
  useEffect(() => {
    const lastCity = localStorage.getItem(LAST_CITY_KEY)
    if (lastCity) {
      handleSearch(lastCity)
    }
  }, [])

  // Keep the browser tab title in sync with the current city/temperature.
  useEffect(() => {
    if (weather?.current) {
      document.title = `${weather.current.temperature}°C in ${weather.current.city} — Weather Dashboard`
    } else {
      document.title = 'Weather Dashboard'
    }
  }, [weather])

  return (
    <>
      <Navbar />

      <main className="dashboard">
        <SearchBar onSearch={handleSearch} disabled={loading} />

        {loading && <Loader />}

        {!loading && error && <ErrorMessage message={error} />}

        {!loading && !error && weather && (
          <>
            <CurrentWeather data={weather.current} />
            <WeatherDetails data={weather.current} />
            <HourlyForecast hourly={weather.hourly_forecast} />
            <Forecast daily={weather.daily_forecast} />
          </>
        )}

        {!loading && !error && !weather && (
          <p className="dashboard-hint">Search for a city to see the weather.</p>
        )}
      </main>

      <Footer />
    </>
  )
}
