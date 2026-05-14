import pandas as pd
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "Attendance": [60, 70, 75, 85, 95]
}

df = pd.DataFrame(data)
print(df)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

#learn dataset stats-mean and sd
#applying scaling formula
scaled_data = scaler.fit_transform(df)
print(scaled_data)

#Features (x)
X = df[["StudyHours", "Attendance"]]

#Target(y)
y = df["Marks"]

#Perform TrainTest split

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
print(X_train.shape)
print(X_test.shape)