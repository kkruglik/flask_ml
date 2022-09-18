import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

model_file = 'models_weights/model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

def make_churn_prediction(customer:dict):
    """
    make prediction if user churn or not
    """
    X = dv.transform([customer])
    pred = model.predict_proba(X)[0,1]
    churn = bool(pred >=0.5)
    return {"churn_proba": float(pred), "churn": churn}