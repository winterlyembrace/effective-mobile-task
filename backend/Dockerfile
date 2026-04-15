# We use the lightest possible image based on Alpine Linux with Python 3.13
FROM python:3.13.13-alpine3.23

WORKDIR /app

# Create a system user "appuser" without a password and with a specific UID of 1001
# This is necessary to avoid running the application as root for security reasons.
RUN adduser -D -u 1001 appuser

# Copy the application file into the container, immediately assigning ownership to our appuser
COPY --chown=appuser:appuser app.py .

# Now all commands (including application launch) will run as appuser
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]
