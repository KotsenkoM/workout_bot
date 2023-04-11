FROM python:3.10-slim-buster
RUN apt-get update && apt-get install -y tzdata
ENV TZ=Europe/Moscow
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8001
CMD ["python", "main.py"]