# MLOPS_Project
From models training to deployment<br>
1. First off, you need to download the IMDB movie review dataset from Kaggle at:<br>
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
and put it on the root folder of the project.<br>
1. Now head into the ML_Flow folder and run the ML_Flow.ipynb notebook, you'll need to install the necessary packages,<br>
which are listed in requirements.txt located at the root folder, install them using pip install -r requirements.txt,<br>
it is advised to use Python 3.9.<br>
1. After training the models, at the same directory ML_Flow, run the command: mlflow ui, and head into the server created to<br>
acces the MlFlow graphical web interface, and there you can compare your runs and see the best model's score and parameters,<br>
you can see examples of it on the screenshots folder. After that you can export the best model as .onnx, which is a universal format,<br>
plus the .pkl of the tfidf transformer that got trained on the training data, which also removes stop words.<br>
1. Now to the FastAPI folder, we will create a Rest API for our model. We start by loading the model and the tfidf transformer, and create<br>
the GET and POST methods inside the movie_app.py file.<br>
On the root folder, with the Dockerfile we build an image then a container of our API using Docker, and expose it on port 80.<br>
1. Since the API is created inside a container, we can now consume it using Postman, take a look at FastAPI/Screenshots to see execution examples.<br>
1. Using Json format is impractical for users, to simplify the process we create a form using Flask, see more details in the Flask/app/movie_app_html.py<br>
file. We also create a container for Flask, by using Flask/Dockerfile<br>
You can see a running example in the Flask/Screenshots folder.<br>
N.B: For the two containers to communicate, you will need to create a bridge network: docker network create network_name --driver bridge, then run the two<br>
containers in the newly created network by adding --network network_name to the docker run command.<br>


