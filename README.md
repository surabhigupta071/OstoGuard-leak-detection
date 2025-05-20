# **OstoGuard-leak-detection**

### *Smart Leak Detection for Colostomy Care – AI & Sensor System*

---

## **Overview**

**OstoGuard** is an AI-powered prototype system designed to detect potential leaks in colostomy and ileostomy bags *before* they occur. By analyzing simulated sensor data, it aims to provide users with increased confidence and comfort.

---

## **Features**

- **Simulated sensor readings** for pressure, moisture, and chemical levels.  
- **Machine learning model** to predict potential leaks based on sensor data.  
- Modular codebase designed for **easy extension and integration**.  
- **Logging** of sensor readings and prediction results for further analysis.

---

## **Getting Started**

### **Prerequisites**

Ensure you have **Python 3.7+** installed on your system.

### **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/surabhigupta071/OstoGuard-leak-detection.git
   cd OstoGuard-leak-detection
Install the required dependencies:
pip install -r requirements.txt
Running the Simulation

Execute the leak detection simulation script:

python src/leak_detection.py
To customize the simulation, use the available command-line options for the number of sensor readings and delay between them:

python src/leak_detection.py --num_readings 20 --delay 0.5
