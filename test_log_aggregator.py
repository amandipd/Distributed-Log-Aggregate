import requests
from datetime import datetime, timedelta
import time

# Base URL for the Flask application
BASE_URL = 'http://127.0.0.1:5000'


def test_log_aggregator():
    # Test 1: Adding a single log
    print("Test 1: Adding a single log")
    log_data = {
        'service_name': 'test_service',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'message': 'This is a test log message'
    }

    try:
        response = requests.post(f'{BASE_URL}/logs', json=log_data)
        print(f"Add log response status code: {response.status_code}")
        print(f"Add log response text: {response.text}")

        # Try to parse JSON if possible
        try:
            print(f"Add log response JSON: {response.json()}")
        except ValueError as json_err:
            print(f"JSON Parsing Error: {json_err}")
    except requests.RequestException as e:
        print(f"Request Error: {e}")

    # Wait a moment to ensure log is processed
    time.sleep(1)

    # Test 2: Retrieving logs
    print("\nTest 2: Retrieving logs")
    start_time = (datetime.now() - timedelta(hours=1)
                  ).strftime('%Y-%m-%d %H:%M:%S')
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    get_params = {
        'service': 'test_service',
        'start': start_time,
        'end': end_time
    }

    try:
        response = requests.get(f'{BASE_URL}/logs', params=get_params)
        print(f"Get logs status code: {response.status_code}")
        print(f"Get logs response text: {response.text}")

        try:
            print(f"Get logs response JSON: {response.json()}")
        except ValueError as json_err:
            print(f"JSON Parsing Error: {json_err}")
    except requests.RequestException as e:
        print(f"Request Error: {e}")

    # Test 3: Adding multiple logs with detailed error handling
    print("\nTest 3: Adding multiple logs")
    multiple_logs = [
        {
            'service_name': 'test_service',
            'timestamp': (datetime.now() - timedelta(minutes=i*10)).strftime('%Y-%m-%d %H:%M:%S'),
            'message': f'Log message {i}'
        } for i in range(5)
    ]

    for log in multiple_logs:
        try:
            response = requests.post(f'{BASE_URL}/logs', json=log)
            print(f"\nAdding log: {log}")
            print(f"Status code: {response.status_code}")
            print(f"Response text: {response.text}")

            try:
                print(f"Response JSON: {response.json()}")
            except ValueError as json_err:
                print(f"JSON Parsing Error: {json_err}")
        except requests.RequestException as e:
            print(f"Request Error: {e}")

    # Additional error diagnosis
    print("\nDebugging Information:")
    print(f"Base URL: {BASE_URL}")
    print("Ensure:")
    print("1. Flask server is running")
    print("2. No firewall blocking local connections")
    print("3. Correct port and host")


if __name__ == '__main__':
    print("Log Aggregator Debugging Script")
    print("Make sure your Flask application is running on http://127.0.0.1:5000")
    input("Press Enter to start testing...")
    test_log_aggregator()
