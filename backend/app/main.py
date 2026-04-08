from fastapi import FastAPI

from app.routers import profile, tasks, users

app = FastAPI(title="Arlo API", version="0.1.0")

app.include_router(users.router)
app.include_router(profile.router)
app.include_router(tasks.router)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
