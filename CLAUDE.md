# ArticleManage 项目 - AI 协作说明

## 📋 项目概述

这是一个基于 **Vue3 + FastAPI + PostgreSQL** 的 AI 文章管理系统。

当 AI 助手需要协助开发、调试或扩展此项目时，请遵循以下规范。

---

## 🏗️ 项目架构

### 技术栈
- **前端**: Vue3 + Vite + Vuetify 3 + Vue Router + Pinia + Axios
- **后端**: Python FastAPI + SQLAlchemy + JWT
- **数据库**: PostgreSQL (单一数据库，存储所有数据)
- **AI集成**: OpenAI, Anthropic Claude, 文心一言, 通义千问, 智谱AI等

### 目录结构

```
ArticleManage/
├── frontend/                 # Vue3 前端项目
│   ├── src/
│   │   ├── views/           # 页面组件
│   │   ├── components/      # 可复用组件
│   │   ├── router/          # 路由配置
│   │   ├── stores/          # Pinia 状态管理
│   │   ├── api/             # API 封装
│   │   └── plugins/         # Vuetify 配置
│   ├── package.json
│   └── vite.config.js
│
└── backend/                 # FastAPI 后端项目
    ├── app/
    │   ├── main.py         # 应用入口
    │   ├── config.py       # 配置管理
    │   ├── database/       # 数据库连接
    │   ├── models/         # SQLAlchemy 模型
    │   ├── schemas/        # Pydantic Schemas
    │   ├── api/            # API 路由
    │   ├── services/       # 业务逻辑（AI调用等）
    │   ├── middleware/     # 中间件（认证等）
    │   └── utils/          # 工具函数
    ├── requirements.txt
    └── .env.example
```

---

## 🗄️ 数据库设计

### PostgreSQL 表结构

**users** - 用户表
- id, username, email, password_hash, role, created_at, updated_at

**articles** - 文章表
- id, user_id, title, content, category, status, profile_id, ai_model_id, brief, metadata, created_at, updated_at

**ai_models** - AI模型配置表
- id, user_id, name, provider, model_name, api_key, base_url, temperature, max_tokens, priority, enabled, created_at, updated_at

**profiles** - 写作风格配置表
- id, user_id, name, description, content, created_at, updated_at

**briefs** - 需求文档表
- id, user_id, title, content, created_at, updated_at

---

## 🔑 核心功能

### 1. 用户认证
- JWT Token 认证
- 角色权限控制（user/admin）
- 注册、登录、获取用户信息

### 2. 文章管理
- 创建、查看、编辑、删除文章
- 文章状态管理（草稿、已发布、待审核）
- 基于 Profile 和 AI 模型生成文章

### 3. AI 模型配置
- 支持多种 AI 服务商（OpenAI、Claude、国产模型等）
- 灵活配置 API Key、Base URL、参数
- 优先级和启用状态管理

### 4. 写作配置管理
- **Profiles**: 写作风格配置（参考 ArticleGenerate 项目的 Profile 机制）
- **Briefs**: 需求文档管理
- 支持 Markdown 格式

---

## 🤖 AI 调用机制

### 工作流程
1. 用户在前端选择 **Profile**（写作风格）和 **AI Model**
2. 填写 **Brief**（需求描述）
3. 后端调用 `ai_service.py` 中的 `generate_article_content()`
4. 根据 AI 模型的 `provider` 字段，调用对应的 API
5. 返回生成的文章内容

### 支持的 AI 服务商
- **OpenAI**: 官方 API 或兼容接口
- **Anthropic**: Claude 系列
- **国产模型**: 文心一言、通义千问、智谱AI、豆包等（通过 OpenAI 兼容接口）

### AI Service 代码位置
- `backend/app/services/ai_service.py`

---

## 🔧 开发规范

### API 开发规范
1. 所有 API 路由放在 `app/api/` 目录
2. 使用 Pydantic Schemas 进行数据验证
3. 需要认证的接口使用 `Depends(get_current_user)`
4. 管理员权限接口使用 `Depends(require_admin)`

### 前端开发规范
1. 页面组件放在 `src/views/`
2. 可复用组件放在 `src/components/`
3. 使用 Pinia 管理全局状态（如用户认证）
4. API 调用统一使用 Axios，配置在 `stores/` 中

### 数据库操作规范
1. 使用 SQLAlchemy ORM
2. 所有模型定义在 `app/models/models.py`
3. 使用 `get_db()` 依赖注入获取数据库会话
4. 查询时注意过滤 `user_id`，确保用户只能访问自己的数据

---

## 🚀 启动项目

### 后端启动
```bash
cd backend

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，配置数据库连接和 SECRET_KEY

# 启动服务
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 前端启动
```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

### 数据库初始化
```bash
# 确保 PostgreSQL 已安装并运行
# 创建数据库
createdb article_manage

# 表会在首次启动后端时自动创建（通过 SQLAlchemy）
```

---

## 📝 AI 协助开发指南

### 添加新功能时
1. **后端**:
   - 在 `models/models.py` 添加数据模型
   - 在 `schemas/schemas.py` 添加 Pydantic Schema
   - 在 `api/` 创建新的路由文件
   - 在 `main.py` 注册路由

2. **前端**:
   - 在 `views/` 创建页面组件
   - 在 `router/index.js` 添加路由
   - 如需全局状态，在 `stores/` 创建 Pinia store
   - 在 `Layout.vue` 的菜单中添加入口

### 调试问题时
1. **后端错误**: 查看 FastAPI 自动生成的文档 `http://localhost:8000/docs`
2. **前端错误**: 检查浏览器控制台和 Network 面板
3. **数据库问题**: 确认 PostgreSQL 连接字符串正确，表已创建

### 扩展 AI 模型支持
1. 在 `services/ai_service.py` 添加新的调用函数
2. 在 `generate_article_content()` 中添加 provider 判断逻辑
3. 前端 `AIModels.vue` 的 `providers` 数组添加新选项

---

## ⚠️ 注意事项

### 安全
- **API Key 加密**: 当前 API Key 以明文存储在数据库，生产环境应加密
- **CORS 配置**: `.env` 中的 `ALLOWED_ORIGINS` 应限制为可信域名
- **JWT Secret**: `SECRET_KEY` 必须在生产环境中使用强随机字符串

### 性能
- AI 生成文章是异步操作，前端应显示加载状态
- PostgreSQL 的 `content` 字段使用 `Text` 类型，适合长文本
- 考虑对文章列表添加分页（已预留 `skip` 和 `limit` 参数）

### 扩展性
- **文件存储**: 当前文章内容存储在数据库，未来可考虑迁移到 S3 等对象存储
- **任务队列**: AI 生成任务可改为后台队列（Celery + Redis）
- **缓存**: 可添加 Redis 缓存热门文章或 Profile 配置

---

## 🔗 参考资源

- **FastAPI 文档**: https://fastapi.tiangolo.com/
- **Vue 3 文档**: https://vuejs.org/
- **Vuetify 3 文档**: https://vuetifyjs.com/
- **SQLAlchemy 文档**: https://docs.sqlalchemy.org/
- **PostgreSQL 文档**: https://www.postgresql.org/docs/

---

## 📌 与 ArticleGenerate 项目的关系

本项目是 **ArticleGenerate** 的管理系统版本：
- ArticleGenerate: 基于文件夹的本地写作工具（Markdown 文件）
- ArticleManage: 基于数据库的 Web 管理系统（可多用户、权限控制）

**Profile 机制保持一致**: 两个项目使用相同的写作风格配置理念，可复用 Profile 配置。

---

**最后更新**: 2025-10-21
**版本**: 1.0.0
