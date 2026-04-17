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
