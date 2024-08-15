from fastapi import FastAPI
from fastapi.routing import APIRoute
import uvicorn
from src.sport_app.settings import settings

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host=settings.server_host, port=settings.server_port, reload=True)