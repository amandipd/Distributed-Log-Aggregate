from flask import Flask, request, jsonify
from datetime import datetime, timedelta


class LogAggregator:
    def __init__(self):
        self.logs = {}

    def add_log(self, service, timestamp, message):
        # Create service log list if it doesn't exist
        if service not in self.logs:
            self.logs[service] = []

        # Add new log entry
        self.logs[service].append({
            'timestamp': timestamp,
            'message': message
        })

        # Remove old logs (older than 1 hour)
        self.clean_old_logs(service)

    def clean_old_logs(self, service):
        # Only keeping logs that are less than 1 hour old
        if service in self.logs:
            recent_logs = [
                log for log in self.logs[service]
                if self.is_recent(log['timestamp'])
            ]
            self.logs[service] = recent_logs

    def is_recent(self, timestamp):
        # Parse timestamp and calculate difference between current time and log time
        try:
            log_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
            current_time = datetime.now()
            time_difference = current_time - log_time

            return time_difference.total_seconds() < 3600  # Less than 1 hour
        except ValueError:
            # If timestamp is invalid, consider it not recent
            return False

    def get_logs(self, service, start_time, end_time):
        matching_logs = []

        if service not in self.logs:
            return matching_logs

        # Loop through logs for the service and check if they fall within the specified time range
        for log in self.logs[service]:
            if start_time <= log['timestamp'] and log['timestamp'] <= end_time:
                matching_logs.append(log)

        return matching_logs


app = Flask(__name__)
log_store = LogAggregator()


@app.route('/logs', methods=['POST'])
def add_log():
    # Receive and store a new log
    data = request.json
    try:
        log_store.add_log(
            service=data['service_name'],
            timestamp=data['timestamp'],
            message=data['message']
        )
        return jsonify({'status': 'Log added successfully'}), 201
    except KeyError:
        return jsonify({'error': 'Missing required fields'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/logs', methods=['GET'])
def get_logs():
    # Retrieve logs for a specific service and time range
    service = request.args.get('service')
    start = request.args.get('start')
    end = request.args.get('end')

    if not all([service, start, end]):
        return jsonify({'error': 'Missing parameters'}), 400

    logs = log_store.get_logs(service, start, end)
    return jsonify(logs)


if __name__ == '__main__':
    app.run(debug=True)
