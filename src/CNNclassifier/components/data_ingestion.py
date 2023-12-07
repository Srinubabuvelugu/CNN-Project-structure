import os
import urllib.request as request
from zipfile import ZipFile
from CNNclassifier import logger
from pathlib import Path
from tqdm import tqdm
from CNNclassifier.entity import DataIngestionConfig
from CNNclassifier.utils import utils


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        pass 

    def download_file(self):
        pass

    def get_updated_list_of_files(self):
        pass

    def preprocessor(self):
        pass 

    def unzip_and_clean(self):
        pass
