FROM python:3.8.14-slim
RUN pip install pipenv
WORKDIR /app
RUN mkdir models_weights
COPY /models_weights/* ./models_weights/
COPY *.py ./
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --deploy --system 
EXPOSE 9696
ENTRYPOINT [ "gunicorn" "--bind" "0.0.0.0:9696" "web_app:app"]