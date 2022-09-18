Docker command to run the server with port mapping:

`sudo docker run -it --rm -p 9696:9696 --entrypoint=bash ml_flask_app:latest`

without port mapping:

`sudo docker run -it --rm --entrypoint=bash ml_flask_app:latest`

To biuld the image:

`sudo docker build -t ml_flask_app .`

Run gunicorn server inside docker image:

`gunicorn --bind 0.0.0.0:9696 web_app:app`