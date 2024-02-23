import http.server
import socketserver
import webbrowser
import threading

# Define the handler to use
handler = http.server.SimpleHTTPRequestHandler

# Specify the port you want to use
port = 8080

# Create a server instance
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving on port {port}")

# Open the browser to the server URL
webbrowser.open(f"http://localhost:{port}")

# Start the server in a separate thread
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.start()

try:
    # Your Python code goes here
    print("Your Python code is running!")

    # For example, you can use a loop to simulate your Python code running indefinitely
    while True:
        pass

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("Stopping server...")
    httpd.shutdown()

# Wait for the server thread to finish
server_thread.join()
