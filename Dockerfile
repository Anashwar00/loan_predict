FROM python:3.11-slim


WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8501

# Correct CMD syntax
CMD ["streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]
