import pickle
import pandas as pd
import numpy as np
import names

# Load the model from the file
with open('server/models/trained/knn/pretrained.pkl', 'rb') as file:
    trained_model = pickle.load(file)


df = pd.read_csv('storage/datasets/ecommerce.csv')
df = df.dropna()
df_preprocessed = pd.read_csv('storage/datasets/datasetpredictvente.csv', delimiter=";")

class Model:
    def __init__(self, ):
        pass

    def will_purchase_product(self, user_id, product_id):
        get_user_info = df_preprocessed[df_preprocessed['user_id'] == user_id]
        get_product_info = get_user_info[get_user_info['product_id'] == product_id]
        get_product_info = get_product_info.drop(
            columns=['Date', 'Time', 'event_type', 'user_session', 'product_id', 'user_id', 'is_purchase'])

        if not get_product_info.empty:
            get_prediction = trained_model.predict(get_product_info)
        else:
            get_prediction = np.array([0])

        return get_prediction

    def get_user_record(self, limit=500):
        user_record = df[['user_id']][:limit]
        user_record['username'] = [names.get_first_name() for _ in range(0,len(user_record))]
        return user_record

    def get_product_record(self, limit=500):

        return df[['product_id','event_type','category_code','brand']][:limit]
