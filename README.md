# Weather Dashboard

A full-stack weather dashboard: **React (Vite)** frontend + **Django REST Framework** backend, using the **OpenWeatherMap API**. Strict 3-color design system: `#00B4D8` (primary), `#FFFFFF` (background), `#03045E` (text).

## Project Structure

```
weather-dashboard/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── weather_dashboard/        # Django project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── weather/                  # Django app
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       ├── services.py           # OpenWeatherMap API calls
│       ├── urls.py
│       ├── admin.py
│       └── migrations/
│
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    ├── .env.example
    └── src/
        ├── main.jsx
        ├── App.jsx / App.css
        ├── index.css              # the 3 color CSS variables
        ├── services/
        │   └── weatherService.js
        ├── components/
        │   ├── Navbar.jsx
        │   ├── SearchBar.jsx
        │   ├── CurrentWeather.jsx
        │   ├── WeatherDetails.jsx
        │   ├── WeatherCard.jsx
        │   ├── HourlyForecast.jsx
        │   ├── Forecast.jsx
        │   ├── Loader.jsx
        │   ├── ErrorMessage.jsx
        │   ├── Footer.jsx
        │   └── Icons.jsx
        └── css/
            ├── Navbar.css
            ├── SearchBar.css
            ├── CurrentWeather.css
            ├── WeatherDetails.css
            ├── WeatherCard.css
            ├── Forecast.css
            ├── Loader.css
            ├── ErrorMessage.css
            └── Footer.css
```

---

## 1. Get a free OpenWeatherMap API key

Sign up at https://home.openweathermap.org/users/sign_up — the free tier is enough for this project. New keys can take 10–30 minutes to activate.

---

## 2. Backend setup (Django)

```bash
cd backend
python -m venv venv

# Activate the virtual environment
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

**Configure the .env file:**

```bash
cp .env.example .env
```

Open `.env` and fill in your real key:

```
OPENWEATHER_API_KEY=your_real_key_here
DJANGO_SECRET_KEY=some-long-random-string
DJANGO_DEBUG=True
```

**Run migrations and start the server:**

```bash
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/
python manage.py runserver
```

Backend is now running at `http://127.0.0.1:8000/`.

---

## 3. Frontend setup (React + Vite)

```bash
cd frontend
npm install
```

**Configure the .env file:**

```bash
cp .env.example .env
```

It should contain:

```
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

**Run the dev server:**

```bash
npm run dev
```

Frontend is now running at `http://localhost:5173/`.

---

## 4. Test the API directly

With the backend running, test in your browser or with curl:

```bash
curl "http://127.0.0.1:8000/api/weather/?city=London"
```

Expected: a JSON object with `current`, `hourly_forecast`, and `daily_forecast` keys.

Try an invalid city to confirm error handling:

```bash
curl "http://127.0.0.1:8000/api/weather/?city=asdkjaskjd"
# -> 404 with {"error": "City \"asdkjaskjd\" was not found..."}
```

---

## 5. How React connects to Django

- `frontend/src/services/weatherService.js` reads `VITE_API_BASE_URL` from the frontend `.env` file and calls `GET {base_url}/weather/?city=...` with Axios.
- Django's `corsheaders` middleware (configured in `settings.py` → `CORS_ALLOWED_ORIGINS`) explicitly allows requests from `http://localhost:5173`, which is Vite's default dev port.
- If you change the Vite port, add the new origin to `CORS_ALLOWED_ORIGINS` in `backend/weather_dashboard/settings.py`.

---

## 6. Preparing for production

**Backend:**
- Set `DJANGO_DEBUG=False` in `.env`.
- Set a strong, unique `DJANGO_SECRET_KEY`.
- Update `ALLOWED_HOSTS` in `settings.py` with your real domain.
- Switch `CORS_ALLOWED_ORIGINS` to your production frontend URL.
- Consider moving from SQLite to PostgreSQL for production traffic.
- Serve with Gunicorn/uWSGI behind Nginx (not `manage.py runserver`).
- Run `python manage.py collectstatic`.

**Frontend:**
- Set `VITE_API_BASE_URL` to your production API URL in `.env`.
- Run `npm run build` — outputs static files to `frontend/dist/`.
- Deploy `dist/` to any static host (Netlify, Vercel, S3+CloudFront, or Nginx).

---

## Notes

- The `weather/migrations/0001_initial.py` file included here was written by hand to match Django's standard migration format (matching the `SearchHistory` model in `models.py`). It's good practice to re-run `python manage.py makemigrations` yourself after setup to confirm it matches your installed Django version — it should report "No changes detected" if everything lines up.
- All icons in the UI are inline SVGs (`components/Icons.jsx`) rather than emoji, since emoji render with fixed built-in colors on every OS/browser regardless of CSS — that would have broken the strict 3-color requirement.
