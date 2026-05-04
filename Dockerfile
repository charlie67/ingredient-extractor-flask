FROM python:3.14-alpine

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Flask app port
EXPOSE 5001

# Run the app
CMD ["gunicorn", "-b", "0.0.0.0:5001", "main:app"]