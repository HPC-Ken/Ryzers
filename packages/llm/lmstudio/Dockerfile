# Copyright(C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT

ARG BASE_IMAGE
FROM ${BASE_IMAGE}  

# Use an argument to get GPU architecture
ARG HSA_OVERRIDE_GFX_VERSION
ARG GFXSTRING

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl  

# Install Vulkan
RUN wget -qO- https://packages.lunarg.com/lunarg-signing-key-pub.asc | tee /etc/apt/trusted.gpg.d/lunarg.asc
RUN wget -qO /etc/apt/sources.list.d/lunarg-vulkan-noble.list http://packages.lunarg.com/vulkan/lunarg-vulkan-noble.list
RUN apt update
RUN apt install -y vulkan-sdk

# Clone and build LlamaCPP
WORKDIR /ryzers
RUN curl https://installers.lmstudio.ai/linux/x64/0.3.27-4/LM-Studio-0.3.27-4-x64.AppImage -o LM-Studio-0.3.27-4-x64.AppImage && \
chmod +x LM-Studio-0.3.27-4-x64.AppImage && \
./LM-Studio-0.3.27-4-x64.AppImage --appimage-extract-and-run --no-sandbox

# Copy test script
COPY test.sh /ryzers/test_lmstudio.sh
RUN chmod +x /ryzers/test_lmstudio.sh

# Set entrypoint to test script
CMD ["/ryzers/test_lmstudio.sh"]
