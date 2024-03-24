from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from pathlib import Path
import pandas as pd

path = Path.cwd() / "Fish.csv"

fishdata = pd.read_csv(path)
fishdata.head()

## I will be using MLR to see if I can predict fish weight from
## a linear combination of the other numerical variables present
fishx = fishdata.drop(['Weight','Species'],axis=1)
fishy = fishdata['Weight']

## I used training and testing sets because I was trying a classification method
## But I decided to keep the sets so that I could see how mlr would perform when only built through 
## a training set
x_train, x_test, y_train, y_test = train_test_split(fishx, fishy)
model = LinearRegression()
model.fit(x_train,y_train)

y_hat = model.predict(x_test)
print(r2_score(y_test,y_hat))
print(mean_squared_error(y_test,y_hat))
