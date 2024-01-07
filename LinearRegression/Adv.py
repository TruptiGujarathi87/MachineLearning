import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def Advertising():
	
	data = pd.read_csv("Advertising.csv")
	X = data[["TV","radio","newspaper"]]
	Y = data["sales"]

	print(X.head())
	print(Y.head())

	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)
	
	obj = LinearRegression()
	obj.fit(X_train, Y_train)
	Y_pred = obj.predict(X_test)


	r_square = r2_score(Y_test,Y_pred)
	print('Predict Rsquare',r_square)


def main():
	Advertising()

if __name__ =="__main__":
	main()
