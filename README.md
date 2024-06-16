# MLDS Final Project: Milestone 2 - Project Notebook

## Project description

"The main topic of the notebook should be a preliminary
analysis on a data source (real data or simulations) relevant to the research idea formed in the first seven weeks
of the project."

## Data Download

### DVC: Preferred, fully replicating the contents of the notebook

The preferred method to retrieve the data is to run `dvc pull` in the CLI. This will ensure that the exact same samples are retrieved to the ones used in the report. See documentation for [DVC](https://dvc.org/doc/command-reference/pull) for reference. This depends on installing `dvc` and `dvc-s3` in the environment.

### boto3: Alternative Method, but not replicable

Run the following line once in order to retrieve the data samples from AWS S3. Below, we pass 100000 as the sample argument. Before doing so, please ensure that `boto3` and `s3fs` are installed. Refer to `requirements.txt` for further dependencies.
```{python}
%run scripts/s3_data_retrieval/retrieve_samples_from_s3.py 100000
```

## Python environment

Please refer to the `requirements.txt` and `environment.yml` files for installation via `pip` and `conda` respectively.