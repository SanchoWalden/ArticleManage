from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    id: int
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    token: str
    user: UserResponse

# Article Schemas
class ArticleBase(BaseModel):
    title: str
    content: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = "草稿"
    brief: Optional[str] = None

class ArticleCreate(ArticleBase):
    profile_id: Optional[int] = None
    ai_model_id: Optional[int] = None

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None

class ArticleResponse(ArticleBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# AI Model Schemas
class AIModelBase(BaseModel):
    name: str
    provider: str
    model_name: str
    api_key: str
    base_url: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 4000
    priority: int = 1
    enabled: bool = True

class AIModelCreate(AIModelBase):
    pass

class AIModelUpdate(BaseModel):
    name: Optional[str] = None
    provider: Optional[str] = None
    model_name: Optional[str] = None
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    priority: Optional[int] = None
    enabled: Optional[bool] = None

class AIModelResponse(AIModelBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Profile Schemas
class ProfileBase(BaseModel):
    name: str
    description: Optional[str] = None
    content: str

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None

class ProfileResponse(ProfileBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Brief Schemas
class BriefBase(BaseModel):
    title: str
    content: str

class BriefCreate(BriefBase):
    pass

class BriefUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class BriefResponse(BriefBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# AI Generation Schema
class AIGenerateRequest(BaseModel):
    brief: str
    profile_id: Optional[int] = None
    ai_model_id: Optional[int] = None

class AIGenerateResponse(BaseModel):
    content: str
    model_used: str
