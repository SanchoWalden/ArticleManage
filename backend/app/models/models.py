from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="user")  # user, admin
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 关系
    articles = relationship("Article", back_populates="author")
    ai_models = relationship("AIModel", back_populates="user")
    profiles = relationship("Profile", back_populates="user")
    briefs = relationship("Brief", back_populates="user")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text)
    category = Column(String(50))
    status = Column(String(20), default="草稿")  # 草稿, 已发布, 待审核
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    ai_model_id = Column(Integer, ForeignKey("ai_models.id"))
    brief = Column(Text)  # 需求描述
    metadata = Column(JSON)  # 额外元数据
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 关系
    author = relationship("User", back_populates="articles")
    profile = relationship("Profile")
    ai_model = relationship("AIModel")


class AIModel(Base):
    __tablename__ = "ai_models"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100), nullable=False)  # 显示名称
    provider = Column(String(50), nullable=False)  # OpenAI, Anthropic, 文心一言等
    model_name = Column(String(100), nullable=False)  # gpt-4, claude-3-opus等
    api_key = Column(String(255), nullable=False)
    base_url = Column(String(255))  # 可选的自定义API地址
    temperature = Column(Float, default=0.7)
    max_tokens = Column(Integer, default=4000)
    priority = Column(Integer, default=1)  # 优先级
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 关系
    user = relationship("User", back_populates="ai_models")


class Profile(Base):
    """写作风格配置"""
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    content = Column(Text, nullable=False)  # Markdown格式的配置内容
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 关系
    user = relationship("User", back_populates="profiles")


class Brief(Base):
    """需求文档"""
    __tablename__ = "briefs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 关系
    user = relationship("User", back_populates="briefs")
