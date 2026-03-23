# 🚀 FASTAPI Projects Collection

This repository contains multiple FastAPI-based projects organized in a monorepo structure.

---

## 📂 Projects Included

### 📘 1. Student Management System
A FastAPI-based backend for managing students.

**Features:**
- Create, update, delete students
- Database integration (SQLAlchemy)
- REST APIs
- Alembic migrations

---

### 📗 2. Library Management System
Backend system to manage books and library operations.

**Features:**
- Book management
- Issue/return tracking
- API-based structure

---

### 💳 3. Stripe Payment Integration
FastAPI project demonstrating Stripe payment gateway integration.

**Features:**
- Payment processing
- Secure API endpoints
- Stripe integration

---

## ⚙️ Tech Stack

- ⚡ FastAPI
- 🐍 Python 3.11
- 🗄️ SQLAlchemy
- 🔄 Alembic
- 🚀 Uvicorn
- 🧪 Pytest (for testing)

---

## 🚀 CI/CD Pipeline

This repository uses GitHub Actions for CI/CD.

- Runs on push to `main`
- Triggered only when **Student Management System** folder changes
- Installs dependencies and runs tests automatically

---

## ▶️ Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/KARTIKKUMARSANGADA/FASTAPI.git
cd FASTAPI