#!/bin/bash
push=$1
TAG=test
#gerar imagem local com o codigo fonte ---back end
#docker pull aandersonlins/back-python-dependences:latest
name_back=aandersonlins/movies-api:${TAG}
docker build -f Dockerfile  -t $name_back .

if [ $push == "push" ]; then
	docker push $name_back
	docker push $name_front
fi
