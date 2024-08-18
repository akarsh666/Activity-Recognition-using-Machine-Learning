from django.shortcuts import render
import numpy as np
import pandas as pd
import pickle


# Create your views here.
LogisticRegressionModel = pickle.load(open("app/model/LRactivity.pkl", "rb"))
RandomForestModel = pickle.load(open("app/model/RFactivity.pkl", "rb"))

FILTERactivity = pickle.load(open("app/model/FILTERactivity.pickle", "rb"))
RFEactivity = pickle.load(open("app/model/RFEactivity.pickle", "rb"))

dupdata = ['tBodyAccMag-sma()', 'tGravityAccMag-mean()', 'tGravityAccMag-std()', 'tGravityAccMag-mad()',
           'tGravityAccMag-max()', 'tGravityAccMag-min()',
           'tGravityAccMag-sma()', 'tGravityAccMag-energy()', 'tGravityAccMag-iqr()',
           'tGravityAccMag-entropy()', 'tGravityAccMag-arCoeff()1',
           'tGravityAccMag-arCoeff()2', 'tGravityAccMag-arCoeff()3', 'tGravityAccMag-arCoeff()4',
           'tBodyAccJerkMag-sma()', 'tBodyGyroMag-sma()',
           'tBodyGyroJerkMag-sma()', 'fBodyAccMag-sma()', 'fBodyBodyAccJerkMag-sma()', 'fBodyBodyGyroMag-sma()',
           'fBodyBodyGyroJerkMag-sma()']

def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def abstract(request):
    return render(request, "abstract.html")


def prediction(request):
    if request.method == 'POST':
        file_path = request.FILES['file']
        df = pd.read_csv(file_path)
        df = df.drop(dupdata, axis=1)
        data = np.array([df.iloc[0].values])
        print(data)
        predicted = LogisticRegressionModel.predict(data)
        print("predicted:", predicted)

        if predicted == 0:
            pred = "LAYING"
        elif predicted == 1:
            pred = "SITTING"
        elif predicted == 2:
            pred = "STANDING"
        elif predicted == 3:
            pred = "WALKING"
        elif predicted == 4:
            pred = "WALKING_DOWNSTAIRS"
        elif predicted == 5:
            pred = "WALKING_UPSTAIRS"
        labels = pred
        return render(request, "prediction.html", {'prediction_text': labels})
    return render(request, "prediction.html")


def prediction2(request):
    if request.method == 'POST':
        file_path = request.FILES['file']
        df = pd.read_csv(file_path)
        df = df.drop(dupdata, axis=1)
        data = np.array([df.iloc[0].values])
        print(data)
        FILTERactivitydata = FILTERactivity.transform(data)
        RFEactivitydata = RFEactivity.transform(FILTERactivitydata)
        predicted2 = RandomForestModel.predict(RFEactivitydata)
        print("predicted:", predicted2)

        if predicted2 == 0:
            pred2 = "LAYING"
        elif predicted2 == 1:
            pred2 = "SITTING"
        elif predicted2 == 2:
            pred2 = "STANDING"
        elif predicted2 == 3:
            pred2 = "WALKING"
        elif predicted2 == 4:
            pred2 = "WALKING_DOWNSTAIRS"
        elif predicted2 == 5:
            pred2 = "WALKING_UPSTAIRS"
        labels2 = pred2
        return render(request, "prediction2.html", {'prediction_text2': labels2})
    return render(request, "prediction2.html")


def performance(request):
    return render(request, "performance.html")
