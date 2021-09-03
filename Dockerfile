FROM python:3.8-slim-buster

# Create virtualenv
RUN python3 -m venv /opt/venv

# Install dependencies
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

# Create workdir
COPY . /app
WORKDIR /app

# Run api
EXPOSE 8000
CMD . /opt/venv/bin/activate && exec uvicorn main:app --reload --host 0.0.0.0 --port 8000
