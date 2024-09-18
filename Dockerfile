FROM python:3.12.6-alpine3.20

WORKDIR /app

EXPOSE 4000

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh
ENTRYPOINT [ "./start.sh" ]