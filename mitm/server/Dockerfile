FROM python:3
WORKDIR /app
COPY bank.py .
COPY requirements.txt .
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "bank.py"]
