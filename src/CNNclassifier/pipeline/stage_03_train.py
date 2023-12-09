from CNNclassifier.config import ConfigurationManaager
from CNNclassifier.components.train import Training
from CNNclassifier import logger


config = ConfigurationManaager()

training_config = config.get_training_config()

training = Training(config=training_config)

training.get_base_model()

training.train_valid_generator()