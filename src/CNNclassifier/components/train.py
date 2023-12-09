from CNNclassifier.entity import TrainingConfig
import tensorflow as tf
from pathlib import Path


class Training:
    def __init__(self, config: TrainingConfig):
        self.config =config


    def get_base_model(self):
        self.model =tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale =1./255,
            validation_split = 0.20
        )

        dataflow_kwargs = dict(
            target_size =self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory= self.config.training_data,
            subset= "validation",
            shuffle=False,
            **dataflow_kwargs
        )
        