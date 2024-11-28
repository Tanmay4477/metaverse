import uvicorn
from fastapi import FastAPI
from db.config import start_db
from contextlib import asynccontextmanager

from api.endpoints.auth import AUTH_ROUTES
from api.endpoints.user import USER_ROUTES
from api.endpoints.space import SPACE_ROUTES
from api.endpoints.arena import ARENA_ROUTES
from api.endpoints.admin import ADMIN_ROUTES 

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def health_checkup():
    return {"msg": "Hi, The Backend is running"}

app.include_router(USER_ROUTES, prefix="/user" ,tags=["users"])
app.include_router(AUTH_ROUTES, prefix="/auth" ,tags=["auth"])
app.include_router(SPACE_ROUTES, prefix="/space" ,tags=["space"])
app.include_router(ARENA_ROUTES, prefix="/elements" ,tags=["arena"])
app.include_router(ADMIN_ROUTES, prefix="/admin" ,tags=["admin"])


if __name__ == "__main__":
    uvicorn.run("main:app")