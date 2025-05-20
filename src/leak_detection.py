# src/leak_detection.py

import random
import csv
import time
from datetime import datetime

class OstoGuard:
    def __init__(self, leak_threshold=2.5, log_file="sensor_log.csv"):
        self.leak_threshold = leak_threshold
        self.log_file = log_file
        # Initialize log file with headers
        with open(self.log_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Pressure", "Moisture", "Chemical", "Leak Predicted"])

    def simulate_sensor_data(self):
        """Simulate sensor readings with some variability"""
        pressure = round(random.uniform(0.5, 2.0), 2)
        moisture = round(random.uniform(0.5, 1.5), 2)
        chemical = round(random.uniform(0.5, 1.5), 2)

        return [pressure, moisture, chemical]

    def predict_leak(self, sensor_data):
        """Simple prediction: leak if sum of values exceeds threshold"""
        total = sum(sensor_data)
        return total > self.leak_threshold

    def log_reading(self, sensor_data, leak_predicted):
        """Append sensor data and prediction to CSV log file"""
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                f"{sensor_data[0]:.2f}",
                f"{sensor_data[1]:.2f}",
                f"{sensor_data[2]:.2f}",
                leak_predicted
            ])

    def run_simulation(self, num_readings=10, delay=1):
        """Simulate multiple sensor readings"""
        print(f"Starting OstoGuard simulation with {num_readings} readings...\n")
        for i in range(num_readings):
            data = self.simulate_sensor_data()
            leak = self.predict_leak(data)
            self.log_reading(data, leak)

            print(f"Reading {i+1}: Pressure={data[0]:.2f}, Moisture={data[1]:.2f}, Chemical={data[2]:.2f} -> "
                  f"{'Leak Predicted!' if leak else 'No Leak'}")
            time.sleep(delay)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run OstoGuard leak detection simulation.")
    parser.add_argument("-n", "--num_readings", type=int, default=10,
                        help="Number of sensor readings to simulate")
    parser.add_argument("-d", "--delay", type=float, default=1,
                        help="Delay between readings in seconds")
    args = parser.parse_args()

    detector = OstoGuard()
    detector.run_simulation(num_readings=args.num_readings, delay=args.delay)

