import os
from pathlib import Path
proj_name = "us_visa"
list_of_files = [
    f"{proj_name}/__init__.py",
    f"{proj_name}/components/__init__.py",
    f"{proj_name}/components/data_ingestion.py",
    f"{proj_name}/components/data_validation.py",
    f"{proj_name}/components/data_transformation.py",
    f"{proj_name}/components/model_trainer.py",
    f"{proj_name}/components/model_evalution.py",
    f"{proj_name}/components/model_pusher.py",
    f"{proj_name}/configuration/__init__.py",
    f"{proj_name}/constant/__init__.py",
    f"{proj_name}/entity/__init__.py",
    f"{proj_name}/entity/config_entity.py",
    f"{proj_name}/entity/artifact_entity.py",
    f"{proj_name}/exception/__init__.py",
    f"{proj_name}/logger/__init__.py",
    f"{proj_name}/pipeline/__init__.py",
    f"{proj_name}/pipeline/training_pipeline.py",
    f"{proj_name}/pipeline/prediction_pipeline.py",
    f"{proj_name}/utils/__init__.py",
    f"{proj_name}/utils/main_ utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "config/model.yaml",
    "research/trials.ipynb",
    "templates/index.html",
    "templates/result.html",
    

]
for filepath in  list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print("File is already there")