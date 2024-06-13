# Test Case: Advertisement CTR Prediction

The challenge is to predict the Click-Through Rate (CTR) for advertisements using the provided dataset. The dataset includes anonymized advertising behavior data collected over seven consecutive days. Participants are required to build a model to predict the CTR and also analyze the CTR across different segments by evaluating the features in the dataset.

# Task

Develop a predictive model to forecast the Click-Through Rate (CTR) of advertisements and analyze the CTR across different segments by evaluating features from the dataset.

# Execution

The project was build using Python 3.9 and Anaconda Inc to manager packages and environments. 
For run the the analysis implemented in this repository you need to follow the steps below:

1. Create the `data/raw` in the root directory.

2. Download the dataset from Kaggle site and unzip the files inside the `data/raw`. See the Repository Structure section below for more details. The dataset can be access by [this link](https://www.kaggle.com/datasets/louischen7/2020-digix-advertisement-ctr-prediction).

3. Create a conda environment using the `envrironment.yml` file:

    ```
    conda env create -f environment.yml
    ```

4. Active the conda environment created before:

    ```
    conda activate ai_collaborator_ctr
    ```

5. Start Jupyter Lab using the command:
    
    ```
    jupyterlab
    ```

6. Go to `src/notebooks` directory and execute the Jupyter Notebooks in an order below:
    * 01-SamplingDataset.ipynb
    * 02-EDA.ipynb
    * 03-Modeling.ipynb

# Repository Structure

The repository should be structured as defined below:

```
AI_COLLABORATOR_AD_CTR_PREDICTION
├─ README.md
├─ .gitignore
├─ data
│   ├─ processed
│   │   |- eda_train_data.csv
|   |   └─ train_data.csv
│   ├─ raw
│   |   |- test_data_A.csv
│   |   |- test_data_B.csv
│   └─  └─ train_data.csv  
├─ src
│   ├─ __init__.py
│   ├─ utils.py
│   ├─ data
│   |   └─ build_data.py
│   ├─ model
│   |   └─ build_model.py
│   └─ notebooks
│   │   |- 01-SamplingDataset.html
│   |   |- 01-SamplingDataset.ipynb
│   |   |- 02-EDA.html
│   |   |- 02-EDA.ipynb
│   |   |- 03-Modeling.html
└─  └─  └─ 03-Modeling.ipynb
```

Below are detailed each directory:
* data/raw - Contains the raw dataset files download from Kaggle.
* data/processed - Contains the processed dataset files after run the Jupyter Notebooks
* src/data  - Contains python code to read the dataset.
* src/model - Contains python code to build the machine learning pipeline.
* src/notebooks - Contains Jupyter Notebooks with the analysis and implementation. 

**P.S.:** There are available HTML files for a fast view of the Jupyter Notebook execution.