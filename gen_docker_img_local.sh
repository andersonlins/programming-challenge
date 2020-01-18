#!/bin/bash
push=$1
TAG=t1.0
#gerar imagem local com o codigo fonte ---back end
docker pull aandersonlins/back-python-dependences:latest
cd api
name_back=aandersonlins/api:${TAG}
docker build -f Dockerfile  -t $name_back .

#gerar imagem local com o codigo fonte ---front end

cd ..
docker pull aandersonlins/node-modules:latest
cd movies-frontend
name_front=aandersonlins/frontend:${TAG}


docker build -f Dockerfile -t $name_front .


if [ $push == "push" ]; then
	docker push $name_back
	docker push $name_front
fi
