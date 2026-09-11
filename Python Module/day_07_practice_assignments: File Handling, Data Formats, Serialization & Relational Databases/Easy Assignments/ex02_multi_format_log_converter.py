'''
Assignment 2: Multi-Format Log Converter (Text to CSV & JSON)

Scenario
A server records raw access events as unformatted plain-text log lines. You need to parse the log lines into structured records and export them to both CSV and JSON formats.

Problem Description
Create a function convert_log_file(input_log_path, output_csv_path, output_json_path):

Each line in input_log_path follows the format: "<TIMESTAMP> | <USER_ID> | <ENDPOINT> | <STATUS_CODE>" (e.g., "2026-09-01 10:15:30 | USR102 | /api/v1/predict | 200").
Parses each line into a dictionary containing keys: timestamp, user_id, endpoint, status_code (as integer).
Writes all parsed records to output_csv_path with a header row using csv.DictWriter.
Writes the list of records to output_json_path with an indentation of 2 spaces using json.dump().
Example Walkthrough
convert_log_file("server_access.log", "access_records.csv", "access_records.json")
'''

import csv
import json


def process_logs(input_file, output_csv, output_json):

    logs = []

    with open(input_file, "r") as file:

        for line in file:

            line = line.strip()

            date, time, level, message = line.split(",", 3)

            log = {
                "date": date,
                "time": time,
                "level": level,
                "message": message
            }

            logs.append(log)

    with open(output_csv, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["date", "time", "level", "message"]
        )

        writer.writeheader()
        writer.writerows(logs)

    level_counts = {}

    for log in logs:

        level = log["level"]

        if level in level_counts:
            level_counts[level] = level_counts[level] + 1
        else:
            level_counts[level] = 1

    summary = {
        "total_logs": len(logs),
        "level_counts": level_counts
    }

    with open(output_json, "w") as file:
        json.dump(summary, file, indent=4)

    print("Logs processed successfully.")


process_logs("logs.txt", "logs.csv", "log_summary.json")
