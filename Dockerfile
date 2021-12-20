FROM python:3.9-buster
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENV PORT 8443
EXPOSE 8443
ENTRYPOINT ["python", "main.py"]
