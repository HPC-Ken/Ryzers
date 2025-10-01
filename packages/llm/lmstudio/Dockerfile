# Copyright(C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT

ARG BASE_IMAGE
FROM ${BASE_IMAGE}  

# Use an argument to get GPU architecture
ARG HSA_OVERRIDE_GFX_VERSION
ARG GFXSTRING

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl libfuse2 

# Clone and build LlamaCPP
WORKDIR /ryzers
RUN curl https://installers.lmstudio.ai/linux/x64/0.3.27-4/LM-Studio-0.3.27-4-x64.AppImage -o LM-Studio-0.3.27-4-x64.AppImage && \
chmod +x LM-Studio-0.3.27-4-x64.AppImage && \
./LM-Studio-0.3.27-4-x64.AppImage

# Copy test script
COPY test.sh /ryzers/test_llstudio.sh
RUN chmod +x /ryzers/test_llstudio.sh

# Set entrypoint to test script
CMD ["/ryzers/test_lmstudio.sh"]
