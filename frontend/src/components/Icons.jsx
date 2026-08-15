/**
 * Icons.jsx
 *
 * WHY: Emoji (💧🌬️👁️ etc.) render with their own fixed built-in colors
 * on every platform, regardless of any CSS we write — that would break
 * the "only 3 colors" requirement. These tiny inline SVGs use
 * stroke="currentColor" instead, so they always render in whichever
 * color the surrounding CSS sets (--color-primary or --color-text).
 */

const common = {
  width: 20,
  height: 20,
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  strokeWidth: 1.8,
  strokeLinecap: 'round',
  strokeLinejoin: 'round',
}

export function DropletIcon() {
  return (
    <svg {...common}>
      <path d="M12 2c4 5 6 8.5 6 11.5A6 6 0 1 1 6 13.5C6 10.5 8 7 12 2Z" />
    </svg>
  )
}

export function WindIcon() {
  return (
    <svg {...common}>
      <path d="M3 8h11a3 3 0 1 0-3-3" />
      <path d="M3 14h14a3 3 0 1 1-3 3" />
      <path d="M3 11h8" />
    </svg>
  )
}

export function GaugeIcon() {
  return (
    <svg {...common}>
      <path d="M4 15a8 8 0 1 1 16 0" />
      <path d="M12 15l3-4" />
      <path d="M12 15h.01" />
    </svg>
  )
}

export function EyeIcon() {
  return (
    <svg {...common}>
      <path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6Z" />
      <circle cx="12" cy="12" r="3" />
    </svg>
  )
}

export function SunriseIcon() {
  return (
    <svg {...common}>
      <path d="M12 3v4" />
      <path d="M5 13a7 7 0 0 1 14 0" />
      <path d="M2 13h20" />
      <path d="M5 17h14" />
      <path d="M4 21h16" />
    </svg>
  )
}

export function SunsetIcon() {
  return (
    <svg {...common}>
      <path d="M12 3v4" />
      <path d="M5 9a7 7 0 0 1 14 0" />
      <path d="M2 13h20" />
      <path d="M5 17h14" />
      <path d="M4 21h16" />
    </svg>
  )
}

export function WarningIcon() {
  return (
    <svg {...common}>
      <path d="M12 3 2 20h20L12 3Z" />
      <path d="M12 10v4" />
      <path d="M12 17h.01" />
    </svg>
  )
}
