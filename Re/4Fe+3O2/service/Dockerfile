FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean

RUN useradd -m -g users -s /bin/bash re

WORKDIR /home/re

COPY --chown=root:root ./ironoxide /home/re

RUN echo "CyberBlitz{youtu.be/watch?v=03H1cWj2Kfc}" \
         > /home/re/flag.txt

USER re

EXPOSE 30001

CMD ["socat", "tcp-l:30001,fork,reuseaddr", "exec:timeout 30 /home/re/ironoxide"]
