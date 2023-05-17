from flask import Flask,request,render_template
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from src.pipeline.pred_pipeline import CustomData,PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/predict',methods=['GET',"POST"])
def predict_data():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            carat = request.form.get('carat'), 
            cut = request.form.get('cut'),
            color = request.form.get('color'), 
            clarity = request.form.get('clarity'),
            depth = request.form.get('depth'), 
            table = request.form.get('table'), 
            x = request.form.get('x'),
            y = request.form.get('y'),
            z = request.form.get('z')
        )
        print(data)
        prediction = data.get_data_as_dataframe()
        print(prediction)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(prediction)
        print(results[0])
        return render_template('home.html',results = results[0])
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug = True,port = 8000 )    