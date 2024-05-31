FROM ubuntu:23.04

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean

RUN useradd -m -g users -s /bin/bash pwn

WORKDIR /home/pwn

COPY --chown=root:root ./brainrot /home/pwn

RUN echo "CyberBlitz{you_are_the_alpha_wolf_and_your_level_10_gyatt_is_mewing_at_me}" \
         > /home/pwn/flag.txt

USER pwn

EXPOSE 30000

CMD ["socat", "tcp-l:30000,fork,reuseaddr", "exec:timeout 30 /home/pwn/brainrot"]
