FROM gcr.io/distroless/static:nonroot

WORKDIR /nonroot
COPY build/index.txt /webapp/index.txt
