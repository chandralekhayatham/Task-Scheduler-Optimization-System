# Task-Scheduler-Optimization-System
A Task Scheduler Optimization System developed using FastAPI and React.js that implements the Greedy Scheduling Algorithm with an interactive dashboard and timeline visualization.
# Task Scheduler Optimization System

## Overview

The Task Scheduler Optimization System is a web-based application that demonstrates task scheduling using the Greedy Scheduling Algorithm.

The system provides an interactive dashboard to visualize scheduled tasks, timeline representation, and scheduling metrics.

---

## Technologies Used

### Frontend
- React.js
- HTML
- CSS
- JavaScript

### Backend
- FastAPI
- Python

---

## Features

- Generate optimized task schedule
- Greedy Scheduling Algorithm
- Interactive dashboard
- Timeline visualization
- Task cards
- Scheduling metrics
- FastAPI REST API integration

---

## Project Structure

Task-Scheduler-Optimization-System

├── Backend

│ ├── src

│ │ ├── app.py

│ │ ├── greedy.py

│ │ ├── metrices.py

│ │ └── cpsat_solver.py

│ └── requirements.txt

│

├── Frontend

│ ├── src

│ │ ├── App.js

│ │ ├── App.css

│ │ └── index.js

│ └── package.json

---

## How to Run

### Backend

```bash
cd Backend
uvicorn src.app:app --reload
