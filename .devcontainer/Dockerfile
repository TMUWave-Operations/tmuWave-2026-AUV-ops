FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    sudo \
    curl \
    wget \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN git clone https://github.com/ArduPilot/ardupilot.git

WORKDIR /opt/ardupilot

RUN git submodule update --init --recursive

RUN Tools/environment_install/install-prereqs-ubuntu.sh -y || true

ENV PATH="/opt/ardupilot/Tools/autotest:${PATH}"

WORKDIR /workspaces/tmuWave-2026-AUV-ops
