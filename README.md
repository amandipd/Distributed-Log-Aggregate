# Distributed Log Aggregator

## Overview
This is a Flask-based log aggregation service that allows adding and retrieving logs for multiple services with in-memory storage and time-based log expiration.

## Prerequisites
- Python 3.8+
- pip (Python Package Installer)

## Setup and Installation
1. Clone the Repository
```bash
git clone https://github.com/yourusername/distributed-log-aggregator.git
cd distributed-log-aggregator
```
2. Install Dependencies
```bash
pip install flask
pip install requests
```
## Running the Application
1. Starting the Log Aggregator Service
```bash
python app.py
```
2. Running tests
```bash
python test_log_aggregator.py
```
## API Endpoints
### Add Log
- URL: ```/logs```
- Method: POST
- Request Body:
  ```bash
  {
  "service_name": "example_service",
  "timestamp": "2024-03-27 14:30:00",
  "message": "Log message content"
  }```
### Retrieve Logs
- URL: /logs
- Method: GET
- Query Parameters:
  - ```service```: Name of the service
  - ```start```: Start timestamp
  - ```end```: End timestamp

