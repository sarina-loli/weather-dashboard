import { WarningIcon } from './Icons.jsx'
import '../css/ErrorMessage.css'

/**
 * ErrorMessage
 * Props:
 *  - message: string to display
 */
export default function ErrorMessage({ message }) {
  if (!message) return null

  return (
    <div className="error-message glass-card" role="alert">
      <span className="error-icon">
        <WarningIcon />
      </span>
      <p className="error-text">{message}</p>
    </div>
  )
}
