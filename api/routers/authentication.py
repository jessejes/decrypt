from fastapi import APIRouter

router = APIRouter()

@router.post("/auth/sign-up")
async def signUp():
    pass
