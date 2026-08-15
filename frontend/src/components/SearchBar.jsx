import { useState } from 'react'
import '../css/SearchBar.css'

/**
 * SearchBar
 * Props:
 *  - onSearch(city: string): called when the user submits a valid city name
 *  - disabled: boolean, disables the input/button while a request is loading
 */
export default function SearchBar({ onSearch, disabled }) {
  const [city, setCity] = useState('')
  const [touched, setTouched] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault()
    setTouched(true)
    const trimmed = city.trim()
    if (!trimmed) return
    onSearch(trimmed)
  }

  return (
    <form className="search-bar" onSubmit={handleSubmit}>
      <input
        type="text"
        className="search-input"
        placeholder="Search for a city (e.g. London)"
        value={city}
        onChange={(e) => setCity(e.target.value)}
        disabled={disabled}
        aria-label="City name"
      />
      <button type="submit" className="search-button" disabled={disabled}>
        Search
      </button>
      {touched && !city.trim() && (
        <p className="search-hint">Please enter a city name.</p>
      )}
    </form>
  )
}
