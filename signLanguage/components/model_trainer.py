import os,sys
import yaml
import zipfile
import shutil
from signLanguage.utils.main_utils import read_yaml_file
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ModelTrainerConfig
from signLanguage.entity.artifacts_entity import ModelTrainerArtifact



class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config


    
    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            # os.system("unzip sign_language_project.v2i.yolov5pytorch.zip")
            # os.system("rm sign_language_project.v2i.yolov5pytorch.zip")
            with zipfile.ZipFile("sign_language_project.v2i.yolov5pytorch.zip", 'r') as zip_ref:
                zip_ref.extractall()  # Extracts all files in the current directory

            # Remove the zip file
            os.remove("sign_language_project.v2i.yolov5pytorch.zip")

            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)


            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            shutil.copy("yolov5/runs/train/yolov5s_results/weights/best.pt", "yolov5/best.pt")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            shutil.copy("yolov5/runs/train/yolov5s_results/weights/best.pt", f"{self.model_trainer_config.model_trainer_dir}/")

           
            # os.system("rm -rf yolov5/runs")
            # os.system("rm -rf train")
            # os.system("rm -rf test")
            # os.system("rm -rf data.yaml")


            # Delete the directories if they exist
            dirs_to_remove = ["yolov5/runs", "train", "test"]
            for directory in dirs_to_remove:
                if os.path.exists(directory):
                    shutil.rmtree(directory)  # Deletes directory and all its contents

            # Delete the file if it exists
            file_to_remove = "data.yaml"
            if os.path.exists(file_to_remove):
                os.remove(file_to_remove)  # Deletes the file

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise SignException(e, sys)



