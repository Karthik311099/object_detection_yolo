from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys

import torch
if torch.cuda.is_available():
    print('yes')
else:
    print('no')