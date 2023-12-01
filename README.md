# This is my end to end project

# First initialize the git
```
git init 
```

```
git add .
```
```
git commit -m "First commit"
```

```
bash your_file_name.sh
```


```
python setup.py install
```

# another way you can mentions -e . in your requirement file and you can run

```
pip install -r requirements.txt
```


# two ways to setup the environment 
1) By running init_setup.sh in git
2) Step by step creating vitual environment in command prompt


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### local cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ritikabhandari049/Dimond-Price-Prediction.mlflow \
MLFLOW_TRACKING_USERNAME=ritikabhandari049 \
MLFLOW_TRACKING_PASSWORD=7496815613371e670187e44120b6d3e90c96fabb \
python script.py

Run this to set as env variables:

```cmd

set MLFLOW_TRACKING_URI=https://dagshub.com/ritikabhandari049/Dimond-Price-Prediction.mlflow

set MLFLOW_TRACKING_USERNAME=ritikabhandari049

set MLFLOW_TRACKING_PASSWORD=7496815613371e670187e44120b6d3e90c96fabb

```


### DVC cmd
- dvc init
- dvc repro
- dvc dag
