# Kidney Disease Classification with MLflow and DVC

This repository provides a comprehensive framework for classifying kidney disease using a deep learning pipeline integrated with MLflow for experiment tracking and DVC for version control of datasets and pipelines.

## Workflow Overview

Follow these steps for setting up, updating, and running the pipeline:

1. **Update `config.yaml`** - Adjust configuration settings for the project.
2. **Update `secrets.yaml` [Optional]** - Modify secrets if required (optional step).
3. **Update `params.yaml`** - Define and update hyperparameters and other configurations.
4. **Update the entity** - Modify the entity structure as per the project requirements.
5. **Update the configuration manager in `src/config`** - Adjust the configuration management in the source code.
6. **Update components** - Implement and update components based on the current iteration of the model.
7. **Update the pipeline** - Modify or add pipeline stages for your workflow.
8. **Update `main.py`** - Modify the entry point of the pipeline as needed.
9. **Update `dvc.yaml`** - Ensure the DVC pipeline is synchronized with your changes.
10. **Run `app.py`** - Execute the application to test the final workflow.

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
cd Kidney-Disease-Classification-
