from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import string
movie_app = FastAPI()
class review(BaseModel):
    input: str
import pickle, numpy
#we are loading the model using pickle
import os
import onnxruntime as rt
dir_path = os.path.dirname(os.path.realpath(__file__))
model_name = "model.onnx"
preprocess_name = "stop_words_tfidf.pkl"
preprocess = pickle.load(open(f"{dir_path}/{preprocess_name}", 'rb'))
sess = rt.InferenceSession(f"{dir_path}/{model_name}")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name
@movie_app.get("/")
def home():
 return {'ML model for review classification'}
@movie_app.post('/make_predictions')
async def make_predictions(features: review):
    lower = str(review).lower()
    no_punct = lower.translate(str.maketrans('', '', string.punctuation))
    transformed = numpy.array(preprocess.transform([no_punct]))
    prediction = str(sess.run([label_name], {input_name:transformed})[0][0])
    return({"prediction":prediction})
if __name__ == "__main__":
 uvicorn.run("movie_app:movie_app", host="0.0.0.0", port=80, reload=True)
