import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception
import os
import sys

from dataclasses import dataclass
from pathlib import Path ## System independent path

@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.inf()
            raise customexception(e,sys)
    
