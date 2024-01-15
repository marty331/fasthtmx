FROM python:3.8

WORKDIR /code

COPY . /code/

ENV SQLALCHEMY_DATABASE_URL "sqlite:////code/sql_app.db"

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH "/code:${PYTHONPATH}"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
