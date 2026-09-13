FROM python:3.12-slim

WORKDIR /app

COPY bibliotecas.txt .

RUN pip install --no-cache-dir -r bibliotecas.txt

COPY . .

RUN mkdir -p uploads

EXPOSE 5000

CMD ["python", "app.py"]