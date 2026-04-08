# Arlo Backend

FastAPI + PostgreSQL backend for Arlo. Milestone 1: user bootstrap, profile sync, task event logging.

## Local development setup

### 1. Start PostgreSQL

The easiest way is Docker. If you have Docker installed:

```bash
docker run --name arlo-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=arlo_dev \
  -p 5432:5432 \
  -d postgres:16
```

To stop it later: `docker stop arlo-postgres`
To start it again: `docker start arlo-postgres`

### 2. Set up the Python environment

From the `backend/` directory:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

The default values in `.env.example` match the Docker Postgres command above, so no edits are needed for local dev.

### 4. Run the database migration

```bash
alembic upgrade head
```

This creates the `users`, `user_profiles`, and `task_events` tables.

### 5. Start the server

```bash
uvicorn app.main:app --reload --port 8000
```

The API is now running at `http://localhost:8000`.
Interactive docs: `http://localhost:8000/docs`

---

## Pointing the iOS app at the dev backend

In `ArloAPIClient.swift`, the base URL is set via a compile-time flag:

```swift
#if DEBUG
static let baseURL = "http://localhost:8000"
#else
static let baseURL = "https://your-production-url.com"  // set when deploying
#endif
```

When running the app in Simulator, `localhost:8000` reaches your Mac directly.

If testing on a physical device on the same Wi-Fi:
1. Find your Mac's local IP: `System Settings → Wi-Fi → Details`
2. Change `localhost` to that IP in `ArloAPIClient.swift` temporarily, or add it as a second debug constant.

---

## API endpoints (Milestone 1)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | /health | none | Health check |
| POST | /users/register | none | Bootstrap anonymous user from device ID |
| GET | /profile | Bearer token | Get current user profile |
| PUT | /profile | Bearer token | Update profile (partial) |
| POST | /tasks/event | Bearer token | Log a task completion, skip, or snooze |

Full interactive docs available at `/docs` when the server is running.

---

## Adding a future migration

```bash
alembic revision --autogenerate -m "describe the change"
alembic upgrade head
```
