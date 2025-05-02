import os
import socket
import sys
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def get_local_ip():
    """Obtains the local IP address of the machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # Attempt to connect to a remote host to retrieve the local IP
        s.connect(('192.168.1.196', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'  # If the IP cannot be retrieved, return localhost
    finally:
        s.close()
    return ip

def start_server(path_to_serve, port=8080):
    """Starts an HTTP server to host a file or directory."""
    # Change the working directory to the one containing the file to serve
    os.chdir(path_to_serve)

    # Obtains the local IP address
    ip = get_local_ip()

    print(f"Server running on {ip}:{port}...")
    
    # Configure the HTTP request handler
    handler = SimpleHTTPRequestHandler
    httpd = TCPServer((ip, port), handler)

    # Launch the HTTP server
    try:
        print(f"The files in the directory {path_to_serve} are now accessible at http://{ip}:{port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping the server...")
        httpd.server_close()

def main():
    print("Welcome to the network file hosting tool.")

    # Ask the user to specify the file or directory to host
    path_to_serve = input("Enter the path of the file or directory to host: ").strip()

    if not os.path.exists(path_to_serve):
        print(f"Error: The specified file or directory '{path_to_serve}' does not exist.")
        sys.exit(1)

    # If it's a file, use its directory
    if os.path.isfile(path_to_serve):
        path_to_serve = os.path.dirname(path_to_serve)

    # Ask the user for the port on which they wish to host
    port = input("Enter the port to host the file (default is 8080): ").strip()
    port = int(port) if port else 8080

    # Start the server to host the file/directory
    start_server(path_to_serve, port)

if __name__ == "__main__":
    main()
# filepath: c:\Users\melvi\Desktop\virus\serveur web avec python\serveur web.py
import os
import socket
import sys
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def get_local_ip():
    """Obtains the local IP address of the machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # Attempt to connect to a remote host to retrieve the local IP
        s.connect(('192.168.1.196', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'  # If the IP cannot be retrieved, return localhost
    finally:
        s.close()
    return ip

def start_server(path_to_serve, port=8080):
    """Starts an HTTP server to host a file or directory."""
    # Change the working directory to the one containing the file to serve
    os.chdir(path_to_serve)

    # Obtains the local IP address
    ip = get_local_ip()

    print(f"Server running on {ip}:{port}...")
    
    # Configure the HTTP request handler
    handler = SimpleHTTPRequestHandler
    httpd = TCPServer((ip, port), handler)

    # Launch the HTTP server
    try:
        print(f"The files in the directory {path_to_serve} are now accessible at http://{ip}:{port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping the server...")
        httpd.server_close()

def main():
    print("Welcome to the network file hosting tool.")

    # Ask the user to specify the file or directory to host
    path_to_serve = input("Enter the path of the file or directory to host: ").strip()

    if not os.path.exists(path_to_serve):
        print(f"Error: The specified file or directory '{path_to_serve}' does not exist.")
        sys.exit(1)

    # If it's a file, use its directory
    if os.path.isfile(path_to_serve):
        path_to_serve = os.path.dirname(path_to_serve)

    # Ask the user for the port on which they wish to host
    port = input("Enter the port to host the file (default is 8080): ").strip()
    port = int(port) if port else 8080

    # Start the server to host the file/directory
    start_server(path_to_serve, port)

if __name__ == "__main__":
    main()