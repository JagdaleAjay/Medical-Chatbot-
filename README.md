# Medical-Chatbot-
# Building a Complete Medical Chatbot with LLMs, LangChain, Pinecone, Flask &amp; AWS 

# How to run?
### STEPS:

```bash
Project repo : https://github.com/JagdaleAjay/Medical-Chatbot-.git 
```

### STEP 01 - Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

### STEP 02 - Install the requirements

```bash
pip install -r requirements.txt
```

### Techstack Used:
- Python
- LangChain
- Flask
- GPT
- Pinecone


# AWS-CICD-Deploment with Github Actions

## STEP 01 - Login with AWS console

## STEP 02 - Create IAM user for deployment

```bash
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

## STEP 03 - Create ECR repo to store/save docker image

```bash
- Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot
```

## STEP 04 - Create EC2 machine (Ubuntu)

## STEP 05 - Open EC2 and Install docker in EC2 Machine

```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

## STEP 06 - Configure EC2 as self-hosted runner:

```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

## STEP 07 - Setup github secrets:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO
- PINECONE_API_KEY
- GROQ_API_KEY

