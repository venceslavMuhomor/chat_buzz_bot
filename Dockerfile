FROM python:3.10

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY . /app

CMD ["python", "./main.py"]