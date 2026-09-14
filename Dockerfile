FROM python:3.12-slim-bookworm
WORKDIR /app
COPY host_server.py widgets.json apps.json ./
RUN pip install --no-cache-dir fastapi "uvicorn[standard]"
ENV DESK_PROFILE=shayan PYTHONUNBUFFERED=1
EXPOSE 6910
CMD ["sh", "-c", "python host_server.py"]
