import joblib

model = joblib.load("marks_model")

s = input("Enter how many hours you studied : ")

print(model.predict( [[ int(s) ]] ) )