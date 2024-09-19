FROM python:3.12.6-slim-bullseye
WORKDIR /app
EXPOSE 4000

ENV HOST=0.0.0.0
ENV PORT=4000

RUN apt update -y
RUN apt install gcc libpq-dev python3-dev -y

COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]