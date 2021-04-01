from .models import User, DB
import pandas as pd
from tensorflow.keras.models import load_model


def predict_user():
    dict = {col.name: [getattr(User.query.all()[-1], str(col.name))] for col in User.__table__.columns}
    df = pd.DataFrame(dict).set_index('id')
    df = df.values.tolist()
    reconstructed_model = load_model('app/final_model')
    return str(reconstructed_model.predict(df, batch_size=10))
