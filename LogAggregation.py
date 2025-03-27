from flask import Flask, request, jsonify
from datetime import datetime, timedelta

class LogAggregator:
    def __init__(self):

        # Store logs for different services
        self.logs = {}


    def add_log(self, service, timestamp, message):

        # Create service log list if it doesn't exist
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


    def clean_old_logs(self, service):
        
        # Create a new list to store recent logs
        recent_logs = []

        # Loop through existing logs, keeping only recent ones
        for log in self.logs[service]:
            if self.is_recent(log['timestamp']):
                recent_logs.append(log)
            
        # Replace old logs with recent logs
        self.logs[service] = recent_logs
    

    # Check if the log is less than 1 hour old
    def is_recent(self, timestamp):
        
        # Parse the timestamp   
        log_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')



        