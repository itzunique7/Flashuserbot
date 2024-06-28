FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y git curl ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app/
RUN pip install -U -r requirements.txt
RUN chmod +x start
CMD ["bash","start.sh"]
