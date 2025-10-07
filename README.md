# 🏦 Loan Approval Prediction App

This is a **Streamlit web application** that predicts whether a **loan application will be approved or rejected** based on user-provided details such as number of dependents, education, employment status, CIBIL score, and asset values.  

The app uses a **machine learning model** trained on loan applicant data and applies a **scaling + SVM (Support Vector Machine)** pipeline to make predictions.

---

## 🚀 Features

- ✅ User-friendly **Streamlit interface**
- 📊 Real-time loan approval prediction
- ⚙️ **Data validation** using `pydantic`
- 💾 Pre-trained **Scaler** and **SVM model** integration (`scalar_svm.pkl`, `grid_model.pkl`)
- ⚡ Fast and interactive predictions

---

## 🧠 Tech Stack

| Component | Description |
|------------|-------------|
| **Python** | Core programming language |
| **Streamlit** | Web app framework |
| **Pydantic** | Input validation |
| **Pandas** | Data handling and preprocessing |
| **Scikit-learn** | ML model (SVM) and scaler |
| **Pickle** | Model serialization |

---

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Anashwar00/loan-predict
cd loan-approval-prediction

p
