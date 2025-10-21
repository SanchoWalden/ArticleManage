from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas.schemas import AIModelCreate, AIModelUpdate, AIModelResponse, AIGenerateRequest, AIGenerateResponse
from app.models.models import AIModel, User, Profile
from app.middleware.auth import get_current_user
from app.services.ai_service import generate_article_content

router = APIRouter(prefix="/api/ai", tags=["AI模型"])

@router.get("/models", response_model=List[AIModelResponse])
def get_ai_models(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取所有AI模型配置"""
    models = db.query(AIModel).filter(AIModel.user_id == current_user.id).all()
    return models

@router.post("/models", response_model=AIModelResponse)
def create_ai_model(
    model_data: AIModelCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """添加AI模型配置"""
    new_model = AIModel(
        **model_data.dict(),
        user_id=current_user.id
    )

    db.add(new_model)
    db.commit()
    db.refresh(new_model)

    return new_model

@router.put("/models/{model_id}", response_model=AIModelResponse)
def update_ai_model(
    model_id: int,
    model_data: AIModelUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """更新AI模型配置"""
    model = db.query(AIModel).filter(
        AIModel.id == model_id,
        AIModel.user_id == current_user.id
    ).first()

    if not model:
        raise HTTPException(status_code=404, detail="模型配置不存在")

    for key, value in model_data.dict(exclude_unset=True).items():
        setattr(model, key, value)

    db.commit()
    db.refresh(model)

    return model

@router.delete("/models/{model_id}")
def delete_ai_model(
    model_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """删除AI模型配置"""
    model = db.query(AIModel).filter(
        AIModel.id == model_id,
        AIModel.user_id == current_user.id
    ).first()

    if not model:
        raise HTTPException(status_code=404, detail="模型配置不存在")

    db.delete(model)
    db.commit()

    return {"message": "模型配置已删除"}

@router.post("/generate", response_model=AIGenerateResponse)
async def generate_article(
    request: AIGenerateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """生成文章内容"""
    # 获取AI模型配置
    if request.ai_model_id:
        ai_model = db.query(AIModel).filter(
            AIModel.id == request.ai_model_id,
            AIModel.user_id == current_user.id
        ).first()
    else:
        # 如果未指定模型，使用优先级最高且已启用的模型
        ai_model = db.query(AIModel).filter(
            AIModel.user_id == current_user.id,
            AIModel.enabled == True
        ).order_by(AIModel.priority.desc()).first()

    if not ai_model:
        raise HTTPException(status_code=404, detail="没有可用的AI模型")

    # 获取Profile配置（如果指定）
    profile_content = None
    if request.profile_id:
        profile = db.query(Profile).filter(
            Profile.id == request.profile_id,
            Profile.user_id == current_user.id
        ).first()
        if profile:
            profile_content = profile.content

    # 调用AI服务生成文章
    content = await generate_article_content(
        brief=request.brief,
        ai_model=ai_model,
        profile_content=profile_content
    )

    return {
        "content": content,
        "model_used": ai_model.name
    }
