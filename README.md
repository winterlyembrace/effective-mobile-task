# effective-mobile-task
Simple web application deployment using Nginx as a reverse proxy and a Python HTTP server, all orchestrated with Docker Compose.

# 🏃 How to Run
1. Clone the repository:
```bash
git clone https://github.com/winterlyembrace/effective-mobile-task.git
cd effective-mobile-task
```

2. Start the app:
```bash
docker-compose up -d --build
```

3. Check container status:
```bash
docker-compose ps
```
The backend should show (healthy) status before Nginx starts accepting traffic.

# ✅ How to Verify
Run the following command in your terminal:
```bash
curl -i http://localhost
```

Expected Output:
```bash
HTTP/1.1 200 OK
...
Hello from Effective Mobile!
```

To check the health check endpoint:
```bash
curl -i http://localhost/health
```

# 🧱 Architecture Overview
The project implements Reverse Proxy pattern:

1. Client sends an HTTP request to port 80.

2. Nginx (acting as a Reverse Proxy) receives the request.

3. Nginx forwards the request to the Backend service using the internal Docker network and the upstream directive.

4. Backend (Python HTTP server) processes the request and returns the response.

Schema (ASCII):
```ASCII
User (curl) -> [ Nginx (Port 80) ] -> [ Docker Network ] -> [ Backend (Port 8080) ]
```

# 📂 Project Structure
```Plaintext
├── backend/
│   ├── Dockerfile      # Multi-stage-ready non-root build
│   └── app.py          # Python HTTP server with /health endpoint
├── nginx/
│   └── nginx.conf      # Custom reverse proxy configuration
├── docker-compose.yml  # Services orchestration
└── README.md           # Documentation
```

# 🛡 Security & Best Practices
* **Non-root user**: Backend runs under a dedicated `appuser` (hardening).
* **Network Isolation**: Backend is not exposed to the host; accessible only via Nginx.
* **Read-only**: Nginx configuration is mounted as read-only.
* **Minimal Images**: Used `alpine` to reduce attack surface and size.


# 🛠 Technologies Used
* **Python 3.13.13-alpine3.23** — Minimal base image for the application.
* **Nginx 1.19-alpine** — Lightweight and secure web server.
* **Docker & Docker Compose** — Containerization and orchestration.


