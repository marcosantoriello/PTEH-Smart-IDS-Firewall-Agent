#!/usr/bin/env python3

"""
NTLFlowLyzer Wrapper
"""

import os
import subprocess
import sys
import json
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'output/extractor_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

subprocess.run(['ntlflowlyzer', '-c', 'config.json'], check=True)

