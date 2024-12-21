import os

from dotenv import load_dotenv

root_path = os.path.join(os.path.dirname(__file__), "..")

load_dotenv(dotenv_path=os.path.join(root_path, ".env"))

SERVICE_HOST: str = os.getenv("SERVICE_HOST")  # type: ignore[reportArgumentType]
SERVICE_PORT: str = os.getenv("SERVICE_PORT")  # type: ignore[reportArgumentType]

DATABASE_URL: str = os.getenv("DATABASE_URL")  # type: ignore[reportArgumentType]
