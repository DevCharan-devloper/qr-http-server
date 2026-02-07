import http.server
import socketserver
import socket
import pyqrcode
import webbrowser
import os
import sys

PORT = 8000


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


def generate_qr(url):
    print("\nGenerating QR Code...")
    qr = pyqrcode.create(url)
    qr.png("server_qr.png", scale=6)
    print("QR saved as server_qr.png")


def start_server():
    local_ip = get_local_ip()
    url = f"http://{local_ip}:{PORT}"

    print("\nServer URL:", url)

    generate_qr(url)

    try:
        webbrowser.open(url)
    except:
        pass

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("\nServer running...")
        print("Press CTRL+C to stop\n")
        httpd.serve_forever()


if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
