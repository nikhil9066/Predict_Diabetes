FROM python:3.10

WORKDIR /app
COPY . /app

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install dependencies, including kaleido
RUN pip install scikit-learn
RUN pip install -U kaleido

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python3", "app.py"]