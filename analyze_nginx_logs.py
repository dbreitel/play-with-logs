from collections import defaultdict
import sys
import json

# Function to parse a log entry
def parse_log_entry(entry):
    parts = entry.split()
    ip = parts[0]
    timestamp = parts[3] + " " + parts[4]
    method = parts[5].strip('"')
    path = parts[6]
    status = int(parts[8])
    user_agent = " ".join(parts[11:]).strip('"')
    return ip, timestamp, method, path, status, user_agent

# Function to analyze the log file
def analyze_log_file(log_file):
    ip_data = defaultdict(lambda: defaultdict(list))  # Group by IP
    status_401_data = []  # Group by 401 status

    with open(log_file, "r") as file:
        for line in file:
            ip, timestamp, method, path, status, user_agent = parse_log_entry(line)

            # Group by IP, including both path and status
            ip_data[ip]["requests"].append({"path": path, "status": status})

            # Group 401 status requests
            if status == 401:
                status_401_data.append({"ip": ip, "path": path})

    return ip_data, status_401_data

# Function to save the analysis results to a JSON file
def save_results_to_json(ip_data, status_401_data, output_file):
    results = {
        "grouped_by_ip": {ip: data for ip, data in ip_data.items()},
        "grouped_by_401_status": status_401_data
    }

    with open(output_file, "w") as json_file:
        json.dump(results, json_file, indent=4)

# Main function
def main():
    # Check if the log file path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python analyze_nginx_logs.py PATH_TO_FILE")
        sys.exit(1)

    log_file = sys.argv[1]  # Get the log file path from the command line
    output_file = "analysis_results.json"  # Output JSON file

    try:
        ip_data, status_401_data = analyze_log_file(log_file)
        save_results_to_json(ip_data, status_401_data, output_file)
        print(f"Analysis results saved to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: The file '{log_file}' does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    main()