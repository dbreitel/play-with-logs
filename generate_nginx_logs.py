import random
import datetime

# List of possible HTTP methods
http_methods = ["GET", "POST", "PUT", "DELETE"]

# List of possible status codes
status_codes = [200, 301, 400, 401, 404, 500]

# List of possible user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

# List of possible request paths
request_paths = [
    "/index.html",
    "/about.html",
    "/contact.html",
    "/products/123",
    "/api/v1/data",
    "/login",
    "/logout",
    "/admin"
]

# Function to generate a random IP address
def generate_ip():
    # Create a small pool of IPs to ensure repetition
    ip_pool = [
        "192.168.1.1",
        "192.168.1.2",
        "192.168.1.3",
        "10.0.0.1",
        "10.0.0.2",
        "172.16.0.1",
        "172.16.0.2"
    ]
    return random.choice(ip_pool)

# Function to generate a random log entry
def generate_log_entry():
    ip = generate_ip()
    timestamp = datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    method = random.choice(http_methods)
    path = random.choice(request_paths)
    status = random.choice(status_codes)
    user_agent = random.choice(user_agents)
    return f'{ip} - - [{timestamp}] "{method} {path} HTTP/1.1" {status} {random.randint(100, 1000)} "{user_agent}"\n'

# Generate synthetic log data
log_entries = []
for _ in range(1000):  # Generate 1000 log entries
    log_entries.append(generate_log_entry())

# Write log entries to a file
with open("nginx_access.log", "w") as log_file:
    log_file.writelines(log_entries)

print("Synthetic NGINX log data generated and saved to 'nginx_access.log'")