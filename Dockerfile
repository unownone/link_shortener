FROM python:3.11.0-alpine3.16
RUN apk add --no-cache gcc musl-dev linux-headers


WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE $PORT
RUN pip install --no-cache-dir bjoern
CMD ["python","serve.py"]
