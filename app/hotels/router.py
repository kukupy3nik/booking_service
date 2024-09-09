from fastapi import APIRouter



router = APIRouter(prefix="/hotels")


@router.get("")
def get_hotels():
    ...
