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
Now to the FastAPI folder, we will create a Rest API for our model. We start by loading the model and the tfidf transformer, and create<br>
the GET and POST methods inside the movie_app.py file.<br>


