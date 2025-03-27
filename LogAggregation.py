from flask import Flask, request, jsonify
from datetime import datetime, timedelta

class LogAggregator:
    def __init__(self):

        # Store logs for different services.
        self.logs = {}

    def add_log(self, service, timestamp, message):

        # Create service log list if it doesn't exist.
        if service not in self.logs:
            self.logs[service] = []
        
        # Otherwise, add new log entry.
        else:
            self.logs[service].append({
                'timestamp': timestamp,
                'message': message
        })
        
        # Remove old logs (older than 1 hour)
        self.clean_old_logs(service)