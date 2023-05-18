# Gem Stone Price Predictor
The Diamond Price Predictor is a machine learning model designed to accurately predict the price of diamonds based on their characteristics. This project aims to provide a practical solution for jewelers, diamond traders, and consumers to make informed decisions about buying and selling diamonds.

The purpose of this project is to leverage machine learning algorithms to create a predictive model that can accurately estimate the price of diamonds. By analyzing various characteristics of diamonds, such as carat weight, cut, color, and clarity, the model can generate reliable price predictions. This can save time, reduce costs, and increase transparency in the diamond market.

## Features
- Predicts the type of gem stone based on input parameters
- Simple and intuitive front-end interface
- Flask API for serving predictions
- Dockerized Flask API for easy deployment
- CI/CD pipeline with GitHub Actions
- Integration with AWS ECR and EC2 for deployment

## Technologies Used
- Python
- Scikit-learn
- Pandas
- Flask
- Docker
- Matplotlib / Seaborn
- GitHub Actions
- HTML/CSS
- AWS ECR
- AWS EC2

## Installation

1) clone the repository:
```
git clone https://github.com/dedeepya-M/Gem-Stone-Price-prediction.git
```
2) Install the necessary dependencies. 
```
pip install -r requirements.txt
```
3) Run Flask Api:
```
python application.py
```
4) Open your web browser and visit http://localhost:8000 to access the front-end interface.

![Screenshot of the diamond price predictor](https://github.com/SahilApte/DimondPrice-prediction/blob/main/static/Screenshot%202023-04-26%20at%206.31.53%20PM.png?raw=true)

## Docker Deployment

1) Build the Docker image:
```
docker build -t gem-stone-predictor .
```
2) Run Docker Container
```
docker run -p 8000:8000 gem-stone-predictor
```
3) Open your web browser and visit http://localhost:8000 to access the deployed application.

## CI/CD Pipeline

The CI/CD pipeline has been set up using GitHub Actions. It includes the following stages:

- Build: Builds the Docker image and tags it with the appropriate version.

- Test: Runs tests to ensure the application functions as expected.

- Deploy: Pushes the Docker image to Amazon Elastic Container Registry (ECR) and triggers a deployment to the Amazon EC2 instance.

