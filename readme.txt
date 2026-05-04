
🛒 Smart Retail Analytics System

📌 Overview

The **Smart Retail Analytics System** is a Python-based desktop application built using **Tkinter** for the GUI and **Machine Learning** techniques for retail data analysis. The system allows users to upload datasets, preprocess data, perform feature extraction, and build predictive models using LSTM.


🚀 Features

* 📂 Upload CSV/XLSX datasets
* 👀 View dataset in tabular format
* 🧹 Data preprocessing (handling null values)
* 🔍 Feature extraction from dataset
* 🤖 Build predictive model using LSTM
* 📊 Data visualization with Matplotlib



🛠️ Technologies Used

* **Python**
* **Tkinter** (GUI)
* **Pandas & NumPy** (Data Processing)
* **Matplotlib & Seaborn** (Visualization)
* **MySQL** (Database)
* **Scikit-learn** (Preprocessing & ML utilities)
* **Keras** (LSTM Model)



📁 Project Structure


SmartRetail/
│── main.py
│── retail.csv
│── README.md


 ▶️ How to Run

```bash
python main.py
```

🧠 Workflow

1. **Dataset Upload**

   * Upload `.csv` or `.xlsx` files
   * Data is stored database

2. **View Dataset**

   * Displays all records in GUI table format

3. **Preprocessing**

   * Removes null or empty values

4. **Feature Extraction**

   * Selects important columns for analysis

5. **Model Building**

   * Uses LSTM neural network
   * Performs time-series prediction


📊 Model Details

* Model Type: **LSTM (Long Short-Term Memory)**
* Activation: ReLU
* Loss Function: Mean Squared Error
* Optimizer: Adam


⚠️ Notes

* Ensure MySQL server is running
* Update MySQL credentials in code:

```python
user='root', password='root'
```

* Dataset path is currently hardcoded:

```python
D:/smart_retail/retail.csv
```

📌 Future Improvements

* Add real-time data analytics
* Improve UI design
* Add multiple ML models comparison
* Deploy as a web application
