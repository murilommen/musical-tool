import uvicorn
from fastapi import FastAPI

from musical_tool.routers import music
from musical_tool.domain import models
from musical_tool.infrastructure.context_manager import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(music.router)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
