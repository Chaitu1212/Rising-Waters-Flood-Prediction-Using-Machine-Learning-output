import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# load excel dataset
data = pd.read_excel("flood dataset.xlsx")

X = data.drop("flood",axis=1)
y = data["flood"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

model=RandomForestClassifier()
model.fit(X_train,y_train)

pickle.dump(model,open("model.pkl","wb"))

print("MODEL CREATED SUCCESS")
