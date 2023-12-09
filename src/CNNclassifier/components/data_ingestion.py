import os
import urllib.request as request
from zipfile import ZipFile
from CNNclassifier import logger
from pathlib import Path
from tqdm import tqdm
from CNNclassifier.entity.config_entity import DataIngestionConfig
from CNNclassifier.utils import utils


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config 

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info("Try to download the data from google")
            url, header = request.urlretrieve(
                            url = self.config.source_URL,
                            filename = self.config.local_data_file
                        )
        
        else:
            logger.info("File already exists")

    def get_updated_list_of_files(self,list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") or f.endswith(".jpeg")]
        

    def preprocessor(self,zf,file,working_dir):
        target_filepath = os.path.join(working_dir,file)
        if not os.path.exists(target_filepath):
            zf.extract(file, working_dir)

    def unzip_and_clean(self):
        with ZipFile(file = self.config.local_data_file,mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self.get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self.preprocessor(zf, f, self.config.unzip_dir)
