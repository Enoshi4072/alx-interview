#!/usr/bin/python3
""" Mock Interview """

import sys
import signal

# Dictionary to hold counts of status codes
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

total_file_size = 0
line_count = 0

def print_statistics():
    print("File size:", total_file_size)
    # Print status code counts in ascending order
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")

def handle_interrupt(sig, frame):
    print_statistics()
    sys.exit(0)

# Register SIGINT (Ctrl+C) signal handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 7:
            continue  # Skip lines with invalid format

        # Extract file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # If 10 lines are read, print statistics and reset counts
        if line_count == 10:
            print_statistics()
            line_count = 0

    # Print final statistics when stdin is closed
    print_statistics()

except KeyboardInterrupt:
    # If interrupted by Ctrl+C, print statistics before exiting
    print_statistics()
