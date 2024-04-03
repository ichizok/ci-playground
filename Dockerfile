FROM gcr.io/distroless/static:nonroot

WORKDIR /nonroot
COPY app/index.txt /webapp/index.txt
