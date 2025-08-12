import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from mlxtend.preprocessing import minmax_scaling
from sklearn.feature_selection import mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.svm import SVC


#from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
def process():
    data = pd.read_csv('./data.csv',delimiter=",")
    #Seperating features and labels
    X = np.array(data.iloc[: , :-1])
    y = np.array(data.iloc[: , -1])
   
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=42,stratify = y, shuffle=True)
    model = LinearSVC()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_valid)
    acc_model = round(accuracy_score(y_pred, y_valid) * 100, 2)
    #acc_scores.append(acc_model)
    result2=open("results/resultsvm.csv","w")
    result2.write("ID,Predicted Value" + "\n")
    for j in range(len(y_pred)):
        result2.write(str(j+1) + "," + str(y_pred[j]) + "\n")
    result2.close()
    mse=mean_squared_error(y_valid, y_pred)
    mae=mean_absolute_error(y_valid, y_pred)
    ps=precision_score(y_valid, y_pred, average='macro')
    rs=recall_score(y_valid, y_pred, average='macro')
    f1=f1_score(y_valid, y_pred, average='macro')
    r2=r2_score(y_valid, y_pred)
    print("---------------------------------------------------------")
    print("MSE VALUE FOR SVM IS %f "  % mse)
    print("MAE VALUE FOR SVM IS %f "  % mae)
    print("R-SQUARED VALUE FOR SVM IS %f "  % r2)
    rms = np.sqrt(mean_squared_error(y_valid, y_pred))
    print("RMSE VALUE FOR SVM IS %f "  % rms)
    ac=accuracy_score(y_valid,y_pred.round())
    print ("ACCURACY VALUE SVM IS %f" % (ac))
    print("Precision Score SVM IS %f "  % ps)
    print("Recall Score SVM IS %f "  % rs)
    print("F1 Score MV IS %f "  % f1)
    print("---------------------------------------------------------")
    result2=open('results/SVMMetrics.csv', 'w')
    result2.write("Parameter,Value" + "\n")
    result2.write("ACCURACY" + "," +str(ac) + "\n")
    result2.write("Precision" + "," +str(ps) + "\n")
    result2.write("Recall" + "," +str(rs) + "\n")
    result2.write("F1" + "," +str(f1) + "\n")
    result2.close()
    df =  pd.read_csv('results/SVMMetrics.csv')
    acc = df["Value"]
    alc = df["Parameter"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    explode = (0.1, 0, 0, 0, 0)  
    fig = plt.figure()
    plt.bar(alc, acc,color=colors)
    plt.xlabel('Parameter')
    plt.ylabel('Value')
    plt.title('SVM Metrics Value')
    fig.savefig('results/SVMMetricsValue.png') 
    plt.pause(5)
    plt.show(block=False)
    plt.close()
process()
