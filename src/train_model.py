import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Simulate data
np.random.seed(42)
n_samples = 1000
pressure = np.random.uniform(0.5, 2.0, n_samples)
moisture = np.random.uniform(0.5, 1.5, n_samples)
chemical = np.random.uniform(0.5, 1.5, n_samples)

# Create labels (leak if sum of signals > 3.5)
leak = (pressure + moisture + chemical > 3.5).astype(int)

data = pd.DataFrame({
    'pressure': pressure,
    'moisture': moisture,
    'chemical': chemical,
    'leak': leak
})

# Split and train
X = data[['pressure', 'moisture', 'chemical']]
y = data['leak']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'leak_model.pkl')

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
