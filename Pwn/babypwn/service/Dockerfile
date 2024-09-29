FROM ubuntu:14.04

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y socat libc6:i386 && \
    apt-get clean

RUN useradd -m -g users -s /bin/bash pwn && \
    chown root:root /home/pwn && chmod 755 /home/pwn

WORKDIR /home/pwn

COPY --chown=root:root ./babypwn /home/pwn

RUN echo "CyberBlitz{i_am_no_longer_a_baby}" \
         > /home/pwn/flag.txt

USER pwn

EXPOSE 30004

CMD ["socat", "tcp-l:30004,fork,reuseaddr", "exec:timeout 30 /home/pwn/babypwn"]
