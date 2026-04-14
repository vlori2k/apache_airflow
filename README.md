# Apache Airflow

A small Apache Airflow project running locally with Docker for learning and practice.

## About the project

This project uses the official Apache Airflow Docker Compose setup to run Airflow locally.
The goal is to learn the basics of Airflow, understand how the services work together, and create simple DAGs for practice.

## Tech stack

- Apache Airflow 3.2.0
- Docker
- Docker Compose
- Python

## Project structure

```text
apache_airflow/
├── config/
├── dags/
├── logs/
├── plugins/
├── .env
├── cheat_sheet.txt
├── docker-compose.yaml
└── main.py
```

## Getting started

### 1. Download the official Docker Compose file

#### Windows
```powershell
Invoke-WebRequest -Uri "https://airflow.apache.org/docs/apache-airflow/3.2.0/docker-compose.yaml" -OutFile "docker-compose.yaml"
```

#### Linux
```bash
curl -L "https://airflow.apache.org/docs/apache-airflow/3.2.0/docker-compose.yaml" -o docker-compose.yaml
```

### 2. Create the `.env` file

#### Windows
```powershell
Set-Content -Path ".env" -Value "AIRFLOW_UID=50000"
```

#### Linux
```bash
echo "AIRFLOW_UID=50000" > .env
```

### 3. Initialize Airflow

```bash
docker compose up airflow-init
```

### 4. Start Airflow

```bash
docker compose up
```

### 5. Open Airflow in the browser

```text
http://localhost:8080
```

## Login

- Username: `airflow`
- Password: `airflow`

## Notes

- This setup is meant for local learning and development.
- Docker is used because standard Airflow does not run properly directly on Windows.
- The official Docker Compose file from Apache Airflow is used in this project.

## Learning goals

- Understand what Apache Airflow is
- Learn how to run Airflow locally with Docker
- Create and test DAGs
- Explore scheduling, logs, and task execution

## Status

Current progress:

- Airflow installed
- Docker Compose setup downloaded
- Airflow initialized successfully
- Airflow UI running locally
- Ready to create the first DAG
