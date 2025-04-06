# 🚀 DockFastID - A Dockerised FastAPI Server

A Dockerized FastAPI application that provides APIs to generate UUIDs and fetch random cat images. The app includes both synchronous and asynchronous endpoints for generating UUIDs, with a 3-second delay in the asynchronous version. It also fetches random cat images from an external API and returns them as JPEG images.

<p align="center">
  <a href="https://fastapi.tiangolo.com/">
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  </a>
  <a href="https://python-poetry.org/">
    <img src="https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=python&logoColor=white" alt="Poetry">
  </a>
  <a href="https://www.python-httpx.org/">
    <img src="https://img.shields.io/badge/HTTPX-4B8BBE?style=for-the-badge" alt="HTTPX">
  </a>
</p>

---

## 🚀 API Endpoints:

1. **GET /uuid**
   - Description: Generates a unique UUID v4 string.
   - Response: A UUID string (e.g., `"e57c2c48-b5ae-4e68-9f68-876ef02b6d2d"`).

2. **GET /async-uuid**
   - Description: Generates a unique UUID v4 string after a 3-second delay.
   - Response: A UUID string (e.g., `"f5e5e50d-4455-4e60-aad7-d1c6a2546f9e"`).

3. **GET /cat**
   - Description: Fetches a random cat image from [https://cataas.com/cat](https://cataas.com/cat).
   - Response: A random cat image in JPEG format.

---

## ⚙️ Setup Instructions:

### 🔧 1. Clone the repository:

```bash
git clone https://github.com/Djain318/darshan-jain-manufac-fast-api.git
cd darshan-jain-manufac-fast-api
```

---

### 🐳 2. Dockerize the application:

#### 🏗️ 2.1 Build the Docker image:

```bash
docker build -t manufac-fastapi .
```

#### 🚢 2.2 Run the Docker container:

```bash
docker run -d --name My_APP -p 8000:8000 manufac-fastapi
```

🐋 Or you can directly use the published docker image from Docker Hub
```bash
docker pull thrillseekr/manufac-project-image:v0.1.0
```

Your FastAPI app will be available at:

- [http://localhost:8000](http://localhost:8000)
- [http://127.0.0.1:8000](http://127.0.0.1:8000)

👉 Try:
- [http://localhost:8000/uuid](http://localhost:8000/uuid)
- [http://localhost:8000/async-uuid](http://localhost:8000/async-uuid)
- [http://localhost:8000/cat](http://localhost:8000/cat)

---

## 📘 3. Swagger UI

You can also explore and test the API using FastAPI’s interactive documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## ⚡ 4. Run without Docker

If you prefer not to use Docker, you can run the FastAPI app locally:

```bash
# Create a Virtual Environment
python -m venv .venv

# Activate the virtual environment:
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

# Install Poetry
pip install poetry

# Install Dependencies
poetry install --no-root

# Run the App
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload
```

Your FastAPI app will be available at:  
🔹 [http://127.0.0.1:8000](http://127.0.0.1:8000)  
🔹 Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
🔹 ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📝 License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
