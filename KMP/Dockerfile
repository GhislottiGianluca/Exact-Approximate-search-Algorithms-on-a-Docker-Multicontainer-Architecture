FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY KMP.py .
ADD . .


CMD ["python", "KMP.py"]
