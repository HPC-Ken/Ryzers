# Copyright(C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT

ARG BASE_IMAGE
FROM ${BASE_IMAGE}  

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /ryzers

# Install Vulkan
RUN apt update 
RUN apt upgrade -y
RUN apt install -y python3 python3-pip python3-virtualenv
RUN virtualenv .venv
ENV PATH=/ryzers/.venv/bin:$PATH


# Copy test script
COPY test.py /ryzers/test_rocm.py
RUN chmod +x /ryzers/test_rocm.py

RUN cd /ryzers

# Install ROCM and Pytorch
RUN pip3 install \
  --index-url https://d2awnip2yjpvqn.cloudfront.net/v2/gfx110X-dgpu/ \
  rocm[libraries,devel]

RUN pip3 install \
  --index-url https://d2awnip2yjpvqn.cloudfront.net/v2/gfx110X-dgpu/ \
  torch

CMD /ryzers/test_rocm.py
