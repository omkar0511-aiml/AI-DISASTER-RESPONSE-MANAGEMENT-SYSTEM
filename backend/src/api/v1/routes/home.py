from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "success": True,
        "message": "AI Disaster Response System is running"
    }