FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir fastmcp httpx

COPY server.py .

ENV LSO_BASE=https://lonestaroracle.xyz

EXPOSE 8018

CMD ["python", "server.py"]
