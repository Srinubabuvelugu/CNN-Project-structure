from CNNclassifier.utils.utils import read_yaml, create_directory
from CNNclassifier.entity.config_entity import DataIngestionConfig
from CNNclassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
#from configs import config
from pathlib import Path
import os


class ConfigurationManager:
    def __init__(self,
                config_filepath = CONFIG_FILE_PATH,
                params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directory([self.config.artifacts_root])
        
        
        

    def  get_data_ingestion_config(self):
        config =self.config.data_ingestion
        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir = config.unzip_dir

        )
        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directory([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LERANING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weight = self.params.WEIGHTS


        )
        
        retrun prepare_base_model_config


    def get_validation_config(self) ->EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model = self.config.training.trained_model_path,
            training_data = self.config.data_ingestion.unzip_dir,
            params_image_size = self.params.IMAGE_SIZE,
            params_batch_size = self.params.BATCH_SIZE
        )
        return eval_config


    