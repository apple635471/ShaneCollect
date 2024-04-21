import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

from .setting import get_settings

app = FastAPI()


class Settings(BaseModel):
    FAST_MODE: str
    HOST: str
    PORT: int
    RELOAD: bool
    FRAMEWORK: str


@app.get("/", response_model=Settings, summary="Application Information")
def myinfo() -> Settings:
    """
    Application Information containing following details:
    - APP_MODE: Application mode
    - HOST: Host IP
    - PORT: Port number
    - RELOAD: Reload mode
    - FRAMEWORK: FastAPI
    """
    settings = get_settings()
    info = settings.to_dict()
    info.update({"FRAMEWORK": "FastAPI"})
    return info


def deploy():
    settings = get_settings()
    print(settings)
    uvicorn.run(
        "shanecollect.app:app",
        host=settings.HOST,
        port=int(settings.PORT),
        reload=settings.RELOAD,
    )


if __name__ == "__main__":
    deploy()
