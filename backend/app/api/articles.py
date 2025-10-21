from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas.schemas import ArticleCreate, ArticleUpdate, ArticleResponse
from app.models.models import Article, User
from app.middleware.auth import get_current_user

router = APIRouter(prefix="/api/articles", tags=["文章管理"])

@router.get("/", response_model=List[ArticleResponse])
def get_articles(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取文章列表"""
    articles = db.query(Article).filter(Article.user_id == current_user.id).offset(skip).limit(limit).all()
    return articles

@router.post("/", response_model=ArticleResponse)
def create_article(
    article_data: ArticleCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """创建文章"""
    new_article = Article(
        **article_data.dict(),
        user_id=current_user.id
    )

    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article

@router.get("/{article_id}", response_model=ArticleResponse)
def get_article(
    article_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取文章详情"""
    article = db.query(Article).filter(
        Article.id == article_id,
        Article.user_id == current_user.id
    ).first()

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )

    return article

@router.put("/{article_id}", response_model=ArticleResponse)
def update_article(
    article_id: int,
    article_data: ArticleUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """更新文章"""
    article = db.query(Article).filter(
        Article.id == article_id,
        Article.user_id == current_user.id
    ).first()

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )

    # 更新字段
    for key, value in article_data.dict(exclude_unset=True).items():
        setattr(article, key, value)

    db.commit()
    db.refresh(article)

    return article

@router.delete("/{article_id}")
def delete_article(
    article_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """删除文章"""
    article = db.query(Article).filter(
        Article.id == article_id,
        Article.user_id == current_user.id
    ).first()

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )

    db.delete(article)
    db.commit()

    return {"message": "文章已删除"}
