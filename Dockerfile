FROM alpine:3.10
RUN apk add libusb-dev stlink python3
COPY . .
ENTRYPOINT ["python3"]
CMD ["flashStm.py"]


