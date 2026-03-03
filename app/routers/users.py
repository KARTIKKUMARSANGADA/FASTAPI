from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import UsersTable
from app.schemas.user import GetUser
from app.dependencies import get_current_user, require_admin


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# ---------------------------------------
# Get Current Logged-in User
# ---------------------------------------
@router.get("/me", response_model=GetUser)
def get_me(current_user: UsersTable = Depends(get_current_user)):
    return current_user


# ---------------------------------------
# Get All Users (Admin Only)
# ---------------------------------------
@router.get("/", response_model=list[GetUser])
def get_all_users(
    db: Session = Depends(get_db),
    current_user: UsersTable = Depends(require_admin)
):
    users = db.query(UsersTable).all()
    return users


# ---------------------------------------
# Get User By ID (Admin Only)
# ---------------------------------------
@router.get("/{user_id}", response_model=GetUser)
def get_user_by_id(
    user_id: UUID,
    db: Session = Depends(get_db),
    current_user: UsersTable = Depends(require_admin)
):
    user = db.query(UsersTable).filter(UsersTable.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


# ---------------------------------------
# Delete User (Admin Only)
# ---------------------------------------
@router.delete("/{user_id}")
def delete_user(
    user_id: UUID,
    db: Session = Depends(get_db),
    current_user: UsersTable = Depends(require_admin)
):
    user = db.query(UsersTable).filter(UsersTable.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}