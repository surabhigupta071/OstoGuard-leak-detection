import random
import time
import csv
import joblib
import argparse
import pandas as pd  # add this import

model = joblib.load('leak_model.pkl')

def get_prediction(pressure, moisture, chemical):
    features = pd.DataFrame([[pressure, moisture, chemical]], columns=['pressure', 'moisture', 'chemical'])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    return prediction, probability

def simulate_sensor_reading():
    pressure = round(random.uniform(0.5, 2.0), 2)
    moisture = round(random.uniform(0.5, 1.5), 2)
    chemical = round(random.uniform(0.5, 1.5), 2)
    return pressure, moisture, chemical

def run_simulation(n_readings=10, delay=1.0):
    with open("sensor_log.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Reading #", "Pressure", "Moisture", "Chemical", "Leak Predicted", "Confidence"])
        
        for i in range(n_readings):
            pressure, moisture, chemical = simulate_sensor_reading()
            leak, confidence = get_prediction(pressure, moisture, chemical)
            result = "Leak Predicted!" if leak else "No Leak"
            print(f"Reading {i+1}: P={pressure}, M={moisture}, C={chemical} -> {result} (Confidence: {confidence:.2f})")
            writer.writerow([i+1, pressure, moisture, chemical, result, f"{confidence:.2f}"])
            time.sleep(delay)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_readings", type=int, default=10)
    parser.add_argument("-d", "--delay", type=float, default=1.0)
    args = parser.parse_args()
    
    run_simulation(n_readings=args.num_readings, delay=args.delay)
