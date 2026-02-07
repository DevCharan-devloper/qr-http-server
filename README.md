# QR HTTP Server with QR Code Access

This project is a simple Python-based HTTP server that allows users to access locally hosted files from a mobile device by scanning a QR code. The application automatically detects the host machine's local IP address, generates a QR code containing the server URL, and starts a local web server.

## Features
- Local HTTP server using Python's built-in http.server
- Automatic local IP detection
- QR code generation for server access
- Mobile-friendly access via shared WiFi network
- Automatic browser launch

## Technologies Used
- Python
- http.server
- socket programming
- pyqrcode
- pypng

## How to Run

Install dependencies:

pip install pyqrcode pypng
Run the server:


Scan the generated QR code (`server_qr.png`) using a mobile device connected to the same network.

## Project Purpose
This project demonstrates basic networking concepts, HTTP server implementation, automation using Python, and QR-based usability enhancement for local services.
