import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
import os

data = pd.read_excel("flood dataset.xlsx")  

X = data[['Temp', 'Humidity', 'Cloud Cover', 'ANNUAL', 'Jan-Feb', 'Mar-May',
          'Jun-Sep', 'Oct-Dec', 'avgjune', 'sub']]

transformer = StandardScaler()
transformer.fit(X)

if not os.path.exists("models"):
    os.makedirs("models")

with open("models/transform.save", "wb") as f:
    pickle.dump(transformer, f)

print("transform.save has been created successfully!")
