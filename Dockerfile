FROM gcr.io/distroless/static:nonroot

WORKDIR /nonroot
COPY ./target/index.txt /webapp/index.txt
