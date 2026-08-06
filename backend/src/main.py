from fastapi import FastAPI
from backend.src.config.config import APP_NAME, APP_VERSION
from backend.src.logger.logging import logger
from backend.src.exceptions.custom_exception import DisasterResponseException
from backend.src.exceptions.exception_handler import disaster_exception_handler

logger.info("AI Disaster Response System has started successfully.")

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.add_exception_handler(
    DisasterResponseException,
    disaster_exception_handler
)

@app.get("/")
def home():
    logger.info("Home endpoint accessed")

    return {
        "message": "Welcome to AI Disaster Response System"
    }

@app.get("/error")
def test_error():
    raise DisasterResponseException(
        "This is a custom exception.",
        status_code=400
    )