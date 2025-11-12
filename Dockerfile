FROM python:3.11-slim

RUN pip install mkdocs mkdocs-material

COPY . /app
WORKDIR /app

RUN python generate_course.py

RUN mkdocs build

EXPOSE 8000

CMD ["python", "-m", "http.server", "8000", "--directory", "site"]