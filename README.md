# ArticleManage - AI 文章管理系统

基于 Vue3 + FastAPI + PostgreSQL 的智能文章管理与生成系统。

## ✨ 功能特性

- 🔐 **用户认证**: JWT Token 认证，支持注册/登录，角色权限控制
- 📝 **文章管理**: 创建、编辑、查看、删除文章，支持多种状态管理
- 🤖 **AI 集成**: 支持多种 AI 大模型（OpenAI、Claude、国产模型等）
- ⚙️ **灵活配置**: Profile 写作风格配置，Brief 需求文档管理
- 🎨 **现代 UI**: 基于 Vuetify 3 的 Material Design 风格界面
- 👥 **多用户**: 支持多用户独立使用，数据隔离

## 🏗️ 技术栈

### 前端
- **框架**: Vue 3 (Composition API)
- **构建工具**: Vite
- **UI 框架**: Vuetify 3
- **路由**: Vue Router 4
- **状态管理**: Pinia
- **HTTP 客户端**: Axios

### 后端
- **框架**: FastAPI
- **ORM**: SQLAlchemy
- **数据库**: PostgreSQL
- **认证**: JWT (python-jose)
- **密码加密**: Passlib (bcrypt)
- **AI SDK**: OpenAI, Anthropic

## 📦 项目结构

```
ArticleManage/
├── frontend/                 # Vue3 前端
│   ├── src/
│   │   ├── views/           # 页面组件
│   │   ├── stores/          # Pinia stores
│   │   ├── router/          # 路由配置
│   │   └── plugins/         # Vuetify 配置
│   ├── package.json
│   └── vite.config.js
│
├── backend/                 # FastAPI 后端
│   ├── app/
│   │   ├── main.py         # 应用入口
│   │   ├── api/            # API 路由
│   │   ├── models/         # 数据模型
│   │   ├── schemas/        # Pydantic Schemas
│   │   ├── services/       # 业务逻辑（AI调用）
│   │   └── database/       # 数据库配置
│   ├── requirements.txt
│   └── .env.example
│
├── CLAUDE.md               # AI 协作说明
└── README.md
```

## 🚀 快速开始

### 环境要求

- **Node.js**: >= 16.x
- **Python**: >= 3.9
- **PostgreSQL**: >= 13.x

### 1. 数据库准备

```bash
# 安装 PostgreSQL 后，创建数据库
createdb article_manage
```

### 2. 后端启动

```bash
cd backend

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，配置以下内容：
# DATABASE_URL=postgresql://user:password@localhost:5432/article_manage
# SECRET_KEY=your-secret-key-here

# 启动后端服务
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

后端服务启动后：
- API 文档: http://localhost:8000/docs
- 健康检查: http://localhost:8000/health

### 3. 前端启动

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端服务启动后访问: http://localhost:3000

### 4. 初始化管理员账号

首次使用需要注册账号，第一个注册的用户默认为普通用户。

如需创建管理员，可以：
1. 注册普通账号
2. 直接在数据库中将 `users` 表的 `role` 字段改为 `admin`

```sql
UPDATE users SET role = 'admin' WHERE username = 'your_username';
```

## 🔧 配置说明

### 后端环境变量 (.env)

```env
# 数据库连接
DATABASE_URL=postgresql://user:password@localhost:5432/article_manage

# JWT 配置
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS 配置
ALLOWED_ORIGINS=http://localhost:3000
```

### AI 模型配置

系统支持以下 AI 服务商：

| 服务商 | 说明 | 配置要点 |
|--------|------|----------|
| **OpenAI** | GPT-4, GPT-3.5 等 | 填写 API Key 即可 |
| **Anthropic** | Claude 系列 | 填写 API Key 即可 |
| **文心一言** | 百度 | 需配置 Base URL（OpenAI 兼容接口） |
| **通义千问** | 阿里云 | 需配置 Base URL（OpenAI 兼容接口） |
| **智谱AI** | ChatGLM | 需配置 Base URL（OpenAI 兼容接口） |
| **开源模型** | 本地部署 | 需配置 Base URL |

在系统 "AI模型配置" 页面添加模型后即可使用。

## 📚 使用指南

### 1. 创建写作配置 (Profile)

Profile 是写作风格配置文件，定义了语言风格、段落习惯、禁忌词汇等。

1. 进入 "配置管理" → "写作配置"
2. 点击 "新建配置"
3. 填写配置名称、描述和 Markdown 格式的配置内容
4. 保存后可在生成文章时选择使用

**示例 Profile**:
```markdown
# 科技测评-专业向

## 语言风格
- 专业严谨，数据驱动
- 口语化程度: 4/10

## 段落习惯
- 中等长度，逻辑清晰

## 禁忌词汇
- 避免: "赋能"、"降维打击"等营销化词汇
```

### 2. 创建需求文档 (Brief)

Brief 是文章需求说明，可以保存常用的写作需求模板。

1. 进入 "配置管理" → "需求文档"
2. 点击 "新建需求"
3. 填写需求标题和详细内容
4. 保存后可复用

### 3. 生成文章

1. 进入 "文章管理" → "创建文章"
2. 选择写作配置 (Profile)
3. 选择 AI 模型
4. 填写需求描述
5. 点击 "生成文章" 按钮
6. AI 生成完成后可继续编辑
7. 保存文章

## 🔐 API 端点

### 认证
- `POST /api/auth/register` - 用户注册
- `POST /api/auth/login` - 用户登录
- `GET /api/auth/me` - 获取当前用户信息

### 文章管理
- `GET /api/articles/` - 获取文章列表
- `POST /api/articles/` - 创建文章
- `GET /api/articles/{id}` - 获取文章详情
- `PUT /api/articles/{id}` - 更新文章
- `DELETE /api/articles/{id}` - 删除文章

### AI 模型
- `GET /api/ai/models` - 获取模型列表
- `POST /api/ai/models` - 添加模型配置
- `PUT /api/ai/models/{id}` - 更新模型配置
- `DELETE /api/ai/models/{id}` - 删除模型配置
- `POST /api/ai/generate` - 生成文章内容

### 配置管理
- `GET /api/configs/profiles` - 获取 Profiles
- `POST /api/configs/profiles` - 创建 Profile
- `GET /api/configs/briefs` - 获取 Briefs
- `POST /api/configs/briefs` - 创建 Brief

完整 API 文档: http://localhost:8000/docs

## 🛠️ 开发指南

### 添加新的 AI 服务商

1. 编辑 `backend/app/services/ai_service.py`
2. 添加新的调用函数（如 `_call_new_provider`）
3. 在 `generate_article_content()` 中添加判断逻辑
4. 前端 `AIModels.vue` 的 `providers` 数组添加选项

### 数据库迁移

当前使用 SQLAlchemy 自动创建表，如需版本控制可集成 Alembic:

```bash
# 安装 Alembic
pip install alembic

# 初始化
alembic init alembic

# 生成迁移
alembic revision --autogenerate -m "description"

# 执行迁移
alembic upgrade head
```

## 📖 相关项目

- **[ArticleGenerate](../ArticleGenerate)**: 基于文件夹的本地 AI 写作工具（本项目的灵感来源）

两个项目的 Profile 配置机制保持一致，可以复用写作风格配置。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

**最后更新**: 2025-10-21
**版本**: 1.0.0
