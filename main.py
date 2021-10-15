import uvicorn
from fastapi import FastAPI

from musical_tool.routers import music


app = FastAPI()
app.include_router(music.router)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
