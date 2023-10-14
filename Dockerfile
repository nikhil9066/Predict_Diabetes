FROM python:3.8

WORKDIR /app

COPY /Seaborn .

RUN pip install seaborn matplotlib

CMD ["python", "Dockwork.py"]