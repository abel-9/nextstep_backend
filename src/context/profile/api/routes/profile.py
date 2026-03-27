from fastapi import APIRouter

router = APIRouter(prefix="/profile", tags=["Profile"])


@router.get("")
def get_profile():
    return {"message": "User profile details"}


@router.post("")
def create_profile():
    return {"message": "Profile created successfully"}


@router.put("")
def update_profile(profile_id: str):
    return {"message": f"Profile with id {profile_id} updated successfully"}


@router.delete("")
def delete_profile(profile_id: str):
    return {"message": f"Profile with id {profile_id} deleted successfully"}
