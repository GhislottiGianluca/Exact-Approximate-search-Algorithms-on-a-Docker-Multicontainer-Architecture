FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY BYG.py .
ADD . .


CMD ["python", "BYG.py"]
