#!/usr/bin/env python3

# Copyright(C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: MIT

import torch

print(torch.cuda.is_available())
# True
print(torch.cuda.get_device_name(0))
# Device name
