# Team 7 RTS Codes

## Description

This is a project developed for RTS preventable accidents analysis.In this capstone project generously sponsored by Regional Transit Service, we have the chance to investigate the operation of public transportation operations and service improvement in Rochester, NY.

Regional Transit Service is the main public body providing public Monroe County (where Rochester city lies in). It provides public transportation services for the city as well as Monro community college and Rochester Institute of Technology. 

The goal of our project is to identify causality related to preventable accidents and make predictions for future ones. This information will be used to help the service improvement team to take actions. And in the end, help improving the quality of service, decrease cost, and avoid unnecessary injuries and damages for RTS.

## Installation

You do not need to install this project.

## Requirements

Python environment with Jupyter-notebook supporting is the basic requirement.

Other requirements of running this project and python libraries are described in detail at the beginning of each code file. Please refer to those files.

## Usage

###  1. Where to find the code files

In the "Code" directory of the "Final Deliverables" folds, there are several subdirectories. Each of the subdirectories contains codes of different parts of our analysis model. The name of the files indicates their usage. Please refer to their names to find the corresponding code.

### 2. Feature Engineering and Modeling

#### Code Files:

This part is consist of six files:
    feature engineer
    decision tree
    random-forest
    AdaBoost
    GBDT
    XGBOOST

#### How to run the code:

Please first run feature engineer before running the other five files. The order of executing decision tree, random forest, AdaBoost, GBDT, XGBOOST is up to you as they work independently. You can choose one of them for all of them according to your requirement.

#### Required data files:

Feature engineer: Encode.csv, accident_w_hotspot.csv, lag.csv
decision tree: accident_selected.csv
random forest: accident_selected.csv
adaboost: accident_selected.csv
GBDT: accident_selected.csv
XGBOOST: accident_selected.csv

### 4.3 Model Evaluation and Comparison

#### Code files:

./Code/Machine Learning Model Comparison/preprocess.py
./Code/Machine Learning Model Comparison/model.ipynb

#### How to run the code:

You do not need to run preprocess.py.
Just execute code blocks in model.ipynb sequentially and do not miss or jump any code blocks.

#### Required data files:

accident_selected.csv

### 4.4 Causal Reasoning

#### Code files:

./Code/data processing/data_preprocessing.ipynb
./Code/Causal Analysis/causal analysis - logistic regression.ipynb
./Code/Causal Analysis/Causal Analysis – covariance terms.ipynb

#### How to run the code:
Run every block in data_preprocessing.ipynb sequentially.

For the logistic regression caulsal reasoning part:
Then run causal analysis - logistic regression.ipynb

For the logistic regression caulsal reasoning after covariance terms:
Then run causal analysis - covariance terms.ipynb


#### Required data files:

Encode.csv
Decode.csv(Not used for running the code, but finding the corresponding variables in the encoded data and analyzig the final results)

## Authors and acknowledgment

There are four members in our project team, Xiaoran Li (Project Manager), Weiran Lin (Algorithm Engineer), Melissa Chan (Algorithm Engineer), and Weinan Hu (Algorithm Engineer). We are all second-year MS Data science students at the University of Rochester.