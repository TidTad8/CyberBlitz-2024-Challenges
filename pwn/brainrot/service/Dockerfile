FROM ubuntu:23.04

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean

RUN useradd -m -g users -s /bin/bash pwn

WORKDIR /home/pwn

USER pwn

COPY --chown=pwn:users ./brainrot /home/pwn

RUN echo "CyberBlitz{wh0_kn3w_8uff32_0v32f10w5_c4n_937_7h15_c0mp11c473d}" > /home/pwn/flag.txt

EXPOSE 30000

CMD ["socat", "tcp-l:30000,fork,reuseaddr", "exec:/home/pwn/brainrot"]
