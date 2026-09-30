FROM debian:stable-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential clang make gdb strace python3 procps iproute2 ca-certificates \
 && rm -rf /var/lib/apt/lists/*

COPY student-oci/student-env-info /usr/local/bin/student-env-info
COPY student-oci/student-check /usr/local/bin/student-check
RUN chmod 0755 /usr/local/bin/student-env-info /usr/local/bin/student-check
WORKDIR /course
CMD ["student-check"]
