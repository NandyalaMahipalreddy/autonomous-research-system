# Autonomous Multi-Agent Research System


## Live Demo

### Application URL

https://autonomous-research-frontend.onrender.com

You can access the deployed Autonomous Multi-Agent Research System using the above link.

### Features Available in Demo

* Research Topic Search
* Multi-Agent Workflow
* Real-Time Web Research
* AI-Generated Reports
* PDF Download
* Cost Tracking
* Research Statistics
* Live Agent Trace







## Overview

Autonomous Multi-Agent Research System is an AI-powered research platform that automatically performs research, validates information, detects contradictions, and generates professional reports with PDF export.

The system uses multiple AI agents coordinated through LangGraph to automate the complete research workflow.

---

## Features

* Multi-Agent Architecture
* Real-Time Web Research using Tavily
* AI-Powered Analysis using Groq
* Fact Checking
* Contradiction Detection
* Confidence Scoring
* Research Statistics
* Cost Tracking
* Live Agent Trace
* PDF Report Export
* File Upload Support
* Research History

---

## Architecture

User Query

↓

React Frontend

↓

FastAPI Backend

↓

LangGraph Workflow

↓

Planner Agent

↓

Web Research Agent

↓

Fact Checker Agent

↓

Contradiction Checker Agent

↓

Critic Agent

↓

Formatter Agent

↓

Research Report + PDF

---

## Technology Stack

### Frontend

* React.js

### Backend

* FastAPI

### AI & Agents

* LangGraph
* Groq (GPT-OSS-20B)

### Search

* Tavily Search API

### PDF Generation

* ReportLab

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd autonomous-research-system
```

### Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### Install Frontend Dependencies

```bash
cd frontend
npm install
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run Backend

```bash
python -m uvicorn backend.app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Run Frontend

```bash
cd frontend
npm start
```

Frontend URL:

```text
http://localhost:3000
```

---

## Deployment

The project is deployed using Render.

After pushing code to GitHub:

```bash
git add .
git commit -m "update"
git push origin main
```

Render automatically rebuilds and deploys the latest version.

---

## Future Enhancements

* Redis State Management
* PostgreSQL Storage
* Qdrant Vector Database
* OpenTelemetry Observability
* Grafana Monitoring Dashboard
* RAG-based Document Retrieval
* Advanced Agent Memory

---

## Author

Mahipal Reddy

Autonomous Multi-Agent Research System
Built using React, FastAPI, LangGraph, Tavily, and Groq.
