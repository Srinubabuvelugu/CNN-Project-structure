from pathlib import Path
from CNNclassifier.entity import PrepareBaseModelConfig
import tensorflow as tf

class PreparationModel:
    def __init__(self,config:PrepareBaseModelConfig):
        self.config = config
        
    def get_base_model(self):
        self.model =tf.keras.applications.vgg16.VGG16(
            input_shapes = self.config.params_image_size,
            weights= self.config.params_weight,
            include_top= self.config.include_top
        )

        self.save_model(path:self.config.base_model_path,model = self.model)


    @staticmethod
    def prepare_full_model(model,classes,freeze_all,freeze_till,learning_rate):
        if freeze_all:
            model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                