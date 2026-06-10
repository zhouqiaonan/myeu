# 英文: Base image using Python 3.12 slim version for smaller size
# 中文: 使用 Python 3.12 精简版基础镜像，减小体积
FROM python:3.12-slim

# 英文: Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
# 中文: 设置环境变量，防止 Python 生成 .pyc 文件并关闭标准输出缓冲
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 英文: Set the working directory inside the container
# 中文: 设置容器内部的工作目录
WORKDIR /app

# 英文: Install system dependencies required for PostgreSQL
# 中文: 安装 PostgreSQL 所需的系统级依赖库
RUN apt-get update && apt-get install -y libpq-dev gcc

# 英文: Copy requirements and install Python dependencies
# 中文: 复制依赖文件并安装 Python 依赖包
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 英文: Copy the entire project into the container
# 中文: 将整个项目代码复制到容器中
COPY . /app/