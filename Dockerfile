FROM python:3.10

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "$PATH:/root/.local/bin"

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000

COPY . ./
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]