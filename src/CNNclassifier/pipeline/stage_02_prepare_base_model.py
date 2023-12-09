from CNNclassifier.config import prepare_base_model
from CNNclassifier.components import prepare_basemodel
from CNNclassifier import logger



logger.info(f"Base Mosel Preparation stage started")
config = ConfigurationManager()
prepare_base_model_config = config.get_prepare_base_model_config()
prepare_base_model = PrepareBaseModelConfig(config=prepare_base_model_config)

prepare_base_model.get_base_model()

prepare_base_model.update_base_model()

logger.info(f"Base Model stage completed")