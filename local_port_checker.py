import socket

print("=== Local Port Checker ===")

host = input("Enter host (default: 127.0.0.1): ").strip()
if not host:
    host = "127.0.0.1"

try:
    port = int(input("Enter port number (1-65535): "))

    if not 1 <= port <= 65535:
        print("Port must be between 1 and 65535.")
    else:
        with socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        ) as client:
            client.settimeout(2)
            result = client.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is accepting connections.")
        else:
            print(f"Port {port} is closed or unreachable.")

except ValueError:
    print("Please enter a valid port number.")
except socket.gaierror:
    print("Could not resolve the hostname.")
except OSError as error:
    print("Connection error:", error)
