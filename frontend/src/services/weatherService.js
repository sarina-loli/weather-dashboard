/**
 * weatherService.js
 *
 * WHY: Keeping the axios call in one dedicated "service" file (instead
 * of inside a component) means components stay focused on rendering,
 * and if the API URL or request logic ever changes, there's only one
 * place to update it.
 */

import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api'

/**
 * Fetch current weather + hourly + 5-day forecast for a city.
 * @param {string} city
 * @returns {Promise<object>} weather payload from the Django API
 * @throws {Error} with a user-friendly message on failure
 */
export async function fetchWeatherByCity(city) {
  try {
    const response = await axios.get(`${API_BASE_URL}/weather/`, {
      params: { city },
    })
    return response.data
  } catch (err) {
    if (err.response && err.response.data && err.response.data.error) {
      const { error } = err.response.data
      // error can be a string or a serializer error object like {city: [...]}
      if (typeof error === 'string') {
        throw new Error(error)
      }
      const firstKey = Object.keys(error)[0]
      throw new Error(Array.isArray(error[firstKey]) ? error[firstKey][0] : String(error))
    }
    throw new Error('Unable to reach the server. Please try again.')
  }
}
