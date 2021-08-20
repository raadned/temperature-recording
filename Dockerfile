FROM python:3

WORKDIR /tmp

COPY requirements.txt .
COPY proto ./proto
COPY server.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./server.py" ]

