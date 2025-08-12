import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from random import seed
from random import randrange
from csv import reader
import csv
from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
def process():
    data = pd.read_csv('./data.csv',delimiter=",")
    #Seperating features and labels
    X = np.array(data.iloc[: , :-1])
    Y = np.array(data.iloc[: , -1])

    X_train,X_test, y_train, y_test = train_test_split(X,Y, test_size=0.101)
    #Fitting the RandomForestClassifier to the training set

    rfc = RandomForestClassifier()
    rfc.fit(X_train, y_train)

    #Making prediction and checking the test set

    y_pred = rfc.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)
    result2=open("results/resultRF.csv","w")
    result2.write("ID,Predicted Value" + "\n")
    for j in range(len(y_pred)):
        result2.write(str(j+1) + "," + str(y_pred[j]) + "\n")
    result2.close()

    mse=mean_squared_error(y_test, y_pred)
    mae=mean_absolute_error(y_test, y_pred)
    r2=r2_score(y_test, y_pred)


    print("---------------------------------------------------------")
    print("MSE VALUE FOR Random Forest IS %f "  % mse)
    print("MAE VALUE FOR Random Forest IS %f "  % mae)
    print("R-SQUARED VALUE FOR Random Forest IS %f "  % r2)
    rms = np.sqrt(mean_squared_error(y_test, y_pred))
    print("RMSE VALUE FOR Random Forest IS %f "  % rms)
    ac=accuracy_score(y_test,y_pred)
    print ("ACCURACY VALUE Random Forest IS %f" % ac)
    print("---------------------------------------------------------")


    result2=open('results/RFMetrics.csv', 'w')
    result2.write("Parameter,Value" + "\n")
    result2.write("MSE" + "," +str(mse) + "\n")
    result2.write("MAE" + "," +str(mae) + "\n")
    result2.write("R-SQUARED" + "," +str(r2) + "\n")
    result2.write("RMSE" + "," +str(rms) + "\n")
    result2.write("ACCURACY" + "," +str(ac) + "\n")
    result2.close()


    df =  pd.read_csv('results/RFMetrics.csv')
    acc = df["Value"]
    alc = df["Parameter"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    explode = (0.1, 0, 0, 0, 0)  

    fig = plt.figure()
    plt.bar(alc, acc,color=colors)
    plt.xlabel('Parameter')
    plt.ylabel('Value')
    plt.title('Random Forest Metrics Value')
    fig.savefig('results/RFMetricsValue.png') 
    plt.pause(5)
    plt.show(block=False)
    plt.close()
process()
