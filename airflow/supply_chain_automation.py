from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import joblib

def run_supply_chain_prediction():

    df = pd.read_csv("/opt/airflow/dags/L_SCM_Dataset.csv", encoding="latin1")

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

    model = joblib.load("/opt/airflow/dags/lr_supply_chain_model.pkl")

    predictions = model.predict(X)

    df['Predicted_Late_Delivery_Risk'] = predictions

    df.to_csv("/opt/airflow/dags/predictions_output.csv", index=False)

    print("Supply chain prediction completed successfully.")

with DAG(
    dag_id="supply_chain_automation",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["supply_chain", "logistic regression", "mlpipeline"]
) as dag:

    run_prediction_task = PythonOperator(
        task_id="run_supply_chain_prediction",
        python_callable=run_supply_chain_prediction
    )
