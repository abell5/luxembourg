FROM python:3.12.4
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./api /src/api
COPY ./.env /src/.env
CMD ["fastapi", "run", "api/api.py", "--port", "8000", "--workers", "-1"]
