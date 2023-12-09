from CNNclassifier.config import ConfigurationManaager
from CNNclassifier.components.evaluation_model import Evaluation
from CNNclassifier import logger


config = ConfigurationManaager()

evaluation_config = config.get_validation_config()

evaluation = Evaluation(config=evaluation_config)

evaluation.evaluation()

evaluation.save_score()