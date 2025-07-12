FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "granite_cli_assist.main:app", "--host", "0.0.0.0", "--port", "8000"]
