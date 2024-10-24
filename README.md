# object_detection_yolo


## Workflows

- constants
- entity
    1. config_entity
    2. artifact_entity #return path of data
- components 
    1. data_ingestion
    2. data_validation
    3. model-pusher
    4.model_trainer
- pipeline
- app.py


## How to run:

```bash
conda create -n obj python=3.7 -y
```

```bash
conda activate obj
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```