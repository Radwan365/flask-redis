# Flask + Redis Docker App

## Overview

A Python Flask web application connected to Redis, managed with Docker Compose.
Redis is used to store and increment a visit counter.

## Routes

- `/` - Displays a welcome message
- `/count` - Increments and displays the visit count stored in Redis

## Requirements

- Docker
- Docker Compose

## How to Run

1. Clone the repo:

```bash
git clone git@github.com:Radwan365/flask-redis.git
cd flask-redis
```

2. Start the containers:

```bash
docker compose up --build
```

3. Visit the app:

- Welcome page: `http://localhost:5000`
- Visit counter: `http://localhost:5000/count`

## How to Stop

```bash
docker compose down
```

## Project Structure

```
flask-redis/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── dockerfile          # Docker image instructions
├── docker-compose.yml  # Multi-container setup
└── README.md           # Project documentation
```
