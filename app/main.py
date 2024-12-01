import config
from api import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.SERVICE_HOST, port=int(config.SERVICE_PORT))