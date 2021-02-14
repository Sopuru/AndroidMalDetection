from sklearn.externals import joblib


loaded_model = joblib.load("RNNFINAL4_model.sav")
joblib.dump(loaded_model, '7Fclassifier.joblib')