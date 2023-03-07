from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers import done, task

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)


@app.get("/")  # @:デコレータ
async def root():
    return {"message": "Hello World"}
