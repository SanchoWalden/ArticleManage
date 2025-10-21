@echo off
chcp 65001 >nul
echo =========================================
echo ArticleManage 项目启动脚本 (Windows)
echo =========================================
echo.

echo 1. 检查 PostgreSQL...
where psql >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ PostgreSQL 未安装，请先安装 PostgreSQL
    pause
    exit /b 1
)
echo ✅ PostgreSQL 已安装
echo.

echo 2. 启动后端服务...
cd backend

if not exist "venv" (
    echo 创建 Python 虚拟环境...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo 安装后端依赖...
pip install -r requirements.txt -q

if not exist ".env" (
    echo ⚠️  .env 文件不存在，从 .env.example 复制...
    copy .env.example .env
    echo ⚠️  请编辑 backend\.env 文件配置数据库连接！
    echo.
    pause
)

echo 启动 FastAPI 后端...
start "ArticleManage Backend" cmd /k "venv\Scripts\activate.bat && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo ✅ 后端已启动
echo    API 文档: http://localhost:8000/docs
echo.

cd ..

echo 3. 启动前端服务...
cd frontend

if not exist "node_modules" (
    echo 安装前端依赖...
    call npm install
)

echo 启动 Vue3 前端...
start "ArticleManage Frontend" cmd /k "npm run dev"
echo ✅ 前端已启动
echo    访问地址: http://localhost:3000
echo.

cd ..

echo =========================================
echo 🎉 项目启动完成！
echo =========================================
echo 后端: http://localhost:8000
echo 前端: http://localhost:3000
echo API文档: http://localhost:8000/docs
echo.
echo 关闭窗口即可停止服务
pause
