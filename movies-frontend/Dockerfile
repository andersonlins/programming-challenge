FROM aandersonlins/node-modules:latest as build-stage
COPY . /app/
RUN npm run build --prod

FROM nginx:1.15.2-alpine

COPY --from=build-stage /app/dist/movies-frontend /usr/share/nginx/html

CMD ["/bin/sh", "-c", "nginx -g 'daemon off;'"]
