FROM python:3.12

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# docker build -t projectname .                                 (normal case)
# docker build -t projectname -f Dockerfile.extension .         (When custom docker file name )
# docker run projectname                                        (normally run docker image)
# docker run -p 8000:8000 projectname                           (run for django)
# docker system prune -a --volumes --force
# docker images
# docker tag 2fdcb7e7b2f7 samratpro/docker-test
# docker push samratpro/docker-test
