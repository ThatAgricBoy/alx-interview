#!/usr/bin/python3
"""Log parsing"""
import sys
import signal

# Define the status codes to track
status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {code: 0 for code in status_codes}
line_count = 0


def print_metrics():
    """Print metrics"""
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def signal_handler(signal, frame):
    """Signal handler"""
    print_metrics()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) == 7:
        ip, date, method, path, version, status_code, file_size = parts
        try:
            status_code = int(status_code)
            file_size = int(file_size)
            if status_code in status_codes:
                total_file_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1
        except ValueError:
            pass

    if line_count == 10:
        print_metrics()
        line_count = 0

print_metrics()
