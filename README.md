# OstoGuard-leak-detection
Smart Leak Detection for Colostomy Care - AI &amp; Sensor System

OstoGuard

OstoGuard is an AI-powered prototype system designed to detect potential leaks in colostomy and ileostomy bags before they occur. By analyzing simulated sensor data, it aims to provide users with increased confidence and comfort.

Features

Simulates sensor readings for pressure, moisture, and chemical levels.
Uses a machine learning model to predict potential leaks based on sensor data.
Modular codebase designed for easy extension and integration.
Logs sensor readings and prediction results for analysis.
Getting Started

Prerequisites
Make sure you have Python installed (version 3.7+ recommended).

Installation
Clone this repository:
git clone https://github.com/surabhigupta071/OstoGuard-leak-detection.git
cd OstoGuard-leak-detection
Install required dependencies:
pip install -r requirements.txt
Running the Simulation
Run the leak detection simulation script:

python src/leak_detection.py
You can customize the number of sensor readings and delay between readings with command-line options:

python src/leak_detection.py --num_readings 20 --delay 0.5
File Structure

src/leak_detection.py: Main simulation script for generating sensor data and leak predictions.
src/train_model.py: Script used to train the leak detection model.
src/leak_model.pkl: Serialized machine learning model file.
src/sensor_log.csv: Output log file of sensor readings and predictions.
License

This project is licensed under the MIT License. See the LICENSE file for details.


