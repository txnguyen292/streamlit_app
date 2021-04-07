import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

from config import CONFIG

#load data
data = pd.read_csv(CONFIG.data / "diabetes.csv")

data[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]] = data[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]].replace(0, np.NaN)

#function to impute the missing values with median bsed on Outcome class
def impute_median(data, var):
    temp = data[data[var].notnull()]
    temp = temp[[var, "Outcome"]].groupby(["Outcome"])[[var]].median()
    data.loc[(data["Outcome"] == 0) & (data[var].isnull()), var] = temp.loc[0, var]
    data.loc[(data["Outcome"] == 1) & (data[var].isnull()), var] = temp.loc[1, var]
    return data

# Impute values using the function
data = impute_median(data, "Glucose")
data = impute_median(data, "BloodPressure")
data = impute_median(data, "SkinThickness")
data = impute_median(data, "Insulin")
data = impute_median(data, "BMI")

# Separate features and target as x & y
y = data["Outcome"]
x = data.drop("Outcome", axis=1)
columns = x.columns

# Scale the values using StandardScaler
scaler = StandardScaler()
scaler = scaler.fit(x)
X = scaler.transform(x)

features = pd.DataFrame(X, columns=columns)

X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.2, random_state=42)

# define the model
model = RandomForestClassifier(n_estimators=300, bootstrap=True, max_features="sqrt")
# fit model to training data
model.fit(X_train, y_train)
# predict on test data
y_pred = model.predict(X_test)

# evaluate performance
print(classification_report(y_test, y_pred))
dump(scaler, CONFIG.models / "scaler.joblib")
dump(model, CONFIG.models / "model.joblib")


# ingerence input data
