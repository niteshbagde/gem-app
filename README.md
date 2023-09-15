# For Azure DEPLOYMENT
> The configuration is for Azure deployment through Github actions CICD flow

## END to END ML Project ##

This repository contains an end-to-end machine learning project, showcasing the steps involved in building, training, and deploying a machine learning model.

### Setup ###

1. **Create and Activate a Virtual Environment:**

   It's recommended to work within a virtual environment to manage project dependencies.

   Using conda:

   ```bash
   conda create -n venv python=3.8
   conda activate venv    OR    conda activate path_to_venv
   ```

2. Installing libraries via requirment.txt
    Installing the dependancies. 

    ```bash
    pip install -r requirmement.txt
    ```

3. Build Project package
    Executing setup.py
    ```bash
    python setup.py install
    ```
    Note - This need's to be run after the package folder and files are created. Because in the package source file i.e SOURCE.txt the entries are made for linking those .py files.

4. The src is the folder for application runtime. It contain all the necessary files and API code for your ML model. 

5. 











# DEv OPS

# End to End MAchine Learning Project
    1. Docker Build checked
    2. Github Workflow
    3. Iam User In AWS
    4. Docker Setup In EC2 commands to be Executed

# to update OS libs

    sudo apt-get update -y

    sudo apt-get upgrade 

# Docker deployment

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# Configure EC2 as self-hosted runner:

    Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 

    ECR_REPOSITORY_NAME = 









