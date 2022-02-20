from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import os
import pandas as pd
import pickle

# Create your views here.
def home(request):
    context = {
        "title": "Home",
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        "title": "About Us"
    }
    return render(request, 'blog/about.html', context)

def load_from_file(request):
    context = {
        "title": "Load data - File",
        "files": os.listdir("filesDb")
    }
    return render(request, 'blog/load_from_file.html', context)

def load_from_file_result(request):
    context = {
        "title": "Load data - File",
        "datas": []
    }
    if request.method == "POST":
        # print(request.POST)
        # print("File Name is", type(request.POST.get('entered_file_name')))
        filename = "/home/defcon/Personal/credit_default_django/clone/credit_default/filesDb/" + request.POST.get('entered_file_name')
        test_data = pd.read_excel(filename)

        test_data = test_data[:100]

        test_data.columns = ['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2',
       'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
        features = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2',
       'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']

        with open("models/randomForestModel", "rb") as f:
            model = pickle.load(f)
        # print(model.predict(test_data[features]))
        predicted_result = pd.DataFrame(columns=['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'DEFAULT_NONDEFAULT'])
        predicted_result['ID'] = test_data['ID']
        predicted_result['LIMIT_BAL'] = test_data['LIMIT_BAL']
        predicted_result['SEX'] = test_data['SEX']
        predicted_result['EDUCATION'] = test_data['EDUCATION']
        predicted_result['MARRIAGE'] = test_data['MARRIAGE']
        predicted_result['AGE'] = test_data['AGE']
        predicted_result['DEFAULT_NONDEFAULT'] = model.predict(test_data[features])
        
        n = 0
        while n < len(predicted_result):
            context['datas'].append(
                {
                    "ID": predicted_result["ID"].iloc[n],
                    "LIMIT_BAL": predicted_result["LIMIT_BAL"].iloc[n],
                    "SEX": predicted_result["SEX"].iloc[n],
                    "EDUCATION": predicted_result["EDUCATION"].iloc[n],
                    "MARRIAGE": predicted_result["MARRIAGE"].iloc[n],
                    "AGE": predicted_result["AGE"].iloc[n],
                    "DEFAULT_NONDEFAULT": predicted_result["DEFAULT_NONDEFAULT"].iloc[n]
                }
            )
            n += 1
        # print(context)
    return render(request, 'blog/load_from_file_result.html', context)