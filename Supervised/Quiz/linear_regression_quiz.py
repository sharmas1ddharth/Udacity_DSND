import pandas as pd
from sklearn.linear_model import LinearRegression

data_to_predict = [[21.07931]]
bmi_data = pd.read_csv("data/bmi_and_lifr_expectancy.csv")
model = LinearRegression()
model.fit(bmi_data[['BMI']], bmi_data[['Life_expectancy']], )
pred = model.predict(data_to_predict)

print(pred)