FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean

RUN useradd -m -g users -s /bin/bash pwn

WORKDIR /home/pwn

COPY --chown=root:root ./babypwn /home/pwn

RUN echo "CyberBlitz{i_am_no_longer_a_baby}" \
         > /home/pwn/flag.txt

USER pwn

EXPOSE 30004

CMD ["socat", "tcp-l:30004,fork,reuseaddr", "exec:timeout 30 /home/pwn/babypwn"]
