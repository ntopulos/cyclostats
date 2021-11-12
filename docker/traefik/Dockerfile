FROM traefik:v2.4.8

ARG STAGE=development

COPY ${STAGE}/traefik.yml /etc/traefik/traefik.yml
COPY ${STAGE}/http.yml /etc/traefik/http.yml
