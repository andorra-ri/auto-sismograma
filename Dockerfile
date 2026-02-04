FROM python:3.14-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=Europe/Andorra
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app
WORKDIR /app

CMD ["python", "main.py"]

