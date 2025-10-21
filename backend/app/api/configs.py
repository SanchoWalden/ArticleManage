from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas.schemas import (
    AIModelCreate, AIModelUpdate, AIModelResponse,
    ProfileCreate, ProfileUpdate, ProfileResponse,
    BriefCreate, BriefUpdate, BriefResponse
)
from app.models.models import AIModel, Profile, Brief, User
from app.middleware.auth import get_current_user

router = APIRouter(prefix="/api/configs", tags=["配置管理"])

# ============ Profile (写作配置) API ============

@router.get("/profiles", response_model=List[ProfileResponse])
def get_profiles(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取所有写作配置"""
    profiles = db.query(Profile).filter(Profile.user_id == current_user.id).all()
    return profiles

@router.post("/profiles", response_model=ProfileResponse)
def create_profile(
    profile_data: ProfileCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """创建写作配置"""
    new_profile = Profile(
        **profile_data.dict(),
        user_id=current_user.id
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile

@router.put("/profiles/{profile_id}", response_model=ProfileResponse)
def update_profile(
    profile_id: int,
    profile_data: ProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """更新写作配置"""
    profile = db.query(Profile).filter(
        Profile.id == profile_id,
        Profile.user_id == current_user.id
    ).first()

    if not profile:
        raise HTTPException(status_code=404, detail="配置不存在")

    for key, value in profile_data.dict(exclude_unset=True).items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)

    return profile

@router.delete("/profiles/{profile_id}")
def delete_profile(
    profile_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """删除写作配置"""
    profile = db.query(Profile).filter(
        Profile.id == profile_id,
        Profile.user_id == current_user.id
    ).first()

    if not profile:
        raise HTTPException(status_code=404, detail="配置不存在")

    db.delete(profile)
    db.commit()

    return {"message": "配置已删除"}

# ============ Brief (需求文档) API ============

@router.get("/briefs", response_model=List[BriefResponse])
def get_briefs(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取所有需求文档"""
    briefs = db.query(Brief).filter(Brief.user_id == current_user.id).all()
    return briefs

@router.post("/briefs", response_model=BriefResponse)
def create_brief(
    brief_data: BriefCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """创建需求文档"""
    new_brief = Brief(
        **brief_data.dict(),
        user_id=current_user.id
    )

    db.add(new_brief)
    db.commit()
    db.refresh(new_brief)

    return new_brief

@router.put("/briefs/{brief_id}", response_model=BriefResponse)
def update_brief(
    brief_id: int,
    brief_data: BriefUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """更新需求文档"""
    brief = db.query(Brief).filter(
        Brief.id == brief_id,
        Brief.user_id == current_user.id
    ).first()

    if not brief:
        raise HTTPException(status_code=404, detail="需求文档不存在")

    for key, value in brief_data.dict(exclude_unset=True).items():
        setattr(brief, key, value)

    db.commit()
    db.refresh(brief)

    return brief

@router.delete("/briefs/{brief_id}")
def delete_brief(
    brief_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """删除需求文档"""
    brief = db.query(Brief).filter(
        Brief.id == brief_id,
        Brief.user_id == current_user.id
    ).first()

    if not brief:
        raise HTTPException(status_code=404, detail="需求文档不存在")

    db.delete(brief)
    db.commit()

    return {"message": "需求文档已删除"}
