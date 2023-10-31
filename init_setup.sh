#!/bin/bash

echo [$(date)]: "START"


echo [$(date)]: "creating env with python 3.9 version" 


conda create --prefix ./project_env python=3.9 -y


echo [$(date)]: "activating the environment" 

conda activate ./project_env

echo [$(date)]: "installing the development requirements" 

pip install -r requirements.txt

echo [$(date)]: "END"