FROM python:3.10-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose the port your app runs on
EXPOSE 8080

# Start the app (change app.py to your actual entry point)
CMD ["python", "app.py"]