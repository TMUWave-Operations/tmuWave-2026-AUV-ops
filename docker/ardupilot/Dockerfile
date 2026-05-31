FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    sudo \
    curl \
    wget \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    python3-pexpect \
    python3-future \
    build-essential \
    net-tools \
    iproute2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN git clone https://github.com/ArduPilot/ardupilot.git

WORKDIR /opt/ardupilot

RUN git submodule update --init --recursive

RUN Tools/environment_install/install-prereqs-ubuntu.sh -y || true

RUN python3 -m pip install \
    empy==3.3.4 \
    MAVProxy \
    future \
    --break-system-packages

ENV PATH="/opt/ardupilot/Tools/autotest:${PATH}"

EXPOSE 14550/udp
EXPOSE 5760/tcp
EXPOSE 5501/tcp

CMD ["bash"]