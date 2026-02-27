from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import joblib
import os

def run_supply_chain_prediction():

    df = pd.read_csv("data/raw/L_SCM_dataset.csv", encoding="latin1")

    X = df.drop([
        'Late_delivery_risk',
        'Delivery Delay',
        'Days for shipping (real)'
    ], axis=1)

    X['urgency_ratio'] = X['Order Item Quantity'] / (X['Days for shipment (scheduled)'] + 1)
    X['profit_margin'] = X['Order Profit Per Order'] / (X['Sales'] + 1)
    X['discount_effect'] = X['Order Item Discount Rate'] * X['Sales']
    X['price_per_quantity'] = X['Order Item Product Price'] / (X['Order Item Quantity'] + 1)
    X['shipment_pressure'] = X['Days for shipment (scheduled)'] * X['Order Item Quantity']

    for col in X.select_dtypes(include=['object']).columns:
        X[col] = X[col].astype('category').cat.codes

    model = joblib.load("models/xgb_supply_chain_model.pkl")

    predictions = model.predict(X)

    df['Predicted_Late_Delivery_Risk'] = predictions

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/predictions_output.csv", index=False)

    print("Supply chain prediction completed successfully.")


with DAG(
    dag_id="shipguard_supply_chain_automation",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["shipguard", "xgboost", "ml_pipeline"]
) as dag:

    run_prediction_task = PythonOperator(
        task_id="run_supply_chain_prediction",
        python_callable=run_supply_chain_prediction
    )