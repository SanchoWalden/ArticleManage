#!/bin/bash

echo "========================================="
echo "ArticleManage 项目启动脚本"
echo "========================================="
echo ""

# 检查 PostgreSQL 是否运行
echo "1. 检查 PostgreSQL..."
if ! command -v psql &> /dev/null; then
    echo "❌ PostgreSQL 未安装，请先安装 PostgreSQL"
    exit 1
fi
echo "✅ PostgreSQL 已安装"
echo ""

# 启动后端
echo "2. 启动后端服务..."
cd backend

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "创建 Python 虚拟环境..."
    python -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "安装后端依赖..."
pip install -r requirements.txt -q

# 检查 .env 文件
if [ ! -f ".env" ]; then
    echo "⚠️  .env 文件不存在，从 .env.example 复制..."
    cp .env.example .env
    echo "⚠️  请编辑 backend/.env 文件配置数据库连接！"
    echo ""
    read -p "按回车继续..."
fi

# 启动后端
echo "启动 FastAPI 后端..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
echo "✅ 后端已启动 (PID: $BACKEND_PID)"
echo "   API 文档: http://localhost:8000/docs"
echo ""

cd ..

# 启动前端
echo "3. 启动前端服务..."
cd frontend

# 检查 node_modules
if [ ! -d "node_modules" ]; then
    echo "安装前端依赖..."
    npm install
fi

# 启动前端
echo "启动 Vue3 前端..."
npm run dev &
FRONTEND_PID=$!
echo "✅ 前端已启动 (PID: $FRONTEND_PID)"
echo "   访问地址: http://localhost:3000"
echo ""

cd ..

echo "========================================="
echo "🎉 项目启动完成！"
echo "========================================="
echo "后端: http://localhost:8000"
echo "前端: http://localhost:3000"
echo "API文档: http://localhost:8000/docs"
echo ""
echo "按 Ctrl+C 停止所有服务"
echo ""

# 等待进程
wait $BACKEND_PID $FRONTEND_PID
