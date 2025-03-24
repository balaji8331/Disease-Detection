# 🩺 Health Vision – AI-Powered Medical Diagnosis

## 📚 Project Overview
**Health Vision** is an AI-powered **web application** built with **Streamlit** that analyzes medical images and predicts possible diseases. It identifies conditions related to the brain, chest, bones, skin, kidneys, and eyes. By leveraging deep learning models, the application offers accurate predictions and precautionary suggestions.

---

## 🎯 Key Features
✅ **Disease Classification:**
- Detects diseases from various medical categories such as:
    - Brain tumors (Glioma, Meningioma, Pituitary, No Tumor)
    - Pneumonia detection from chest X-rays
    - Bone fractures detection
    - Skin disease classification
    - Kidney stone detection
    - Eye infections analysis

✅ **Precautionary Advice:**
- Provides suggestions and precautions based on the detected condition.

✅ **User-Friendly Interface:**
- Built with **Streamlit** for an intuitive, simple, and responsive interface.
- Allows easy image uploads and instant predictions.

---

## ⚙️ Technology Stack
- **Frontend:** Streamlit  
- **Backend:** Python (TensorFlow, OpenCV, NumPy)  
- **Machine Learning Models:** CNN models trained for:
    - Brain MRI classification
    - Chest X-ray classification
    - Bone fracture classification
    - Skin disease classification
    - Kidney and eye analysis

---

## 🛠️ Installation Guide
1. **Clone the repository:**
git clone https://github.com/your-username/health-vision.git
cd health-vision
2.  Create a virtual environment:
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
3.  Install dependencies:
pip install -r requirements.txt
4.  Run the application:
streamlit run app.py

---

Project Structure
/health-vision
├── /models
│   ├── all-in-one.h5
│   ├── brain.h5
│   ├── chest.h5
│   ├── fracture.h5
│   ├── eye.h5
│   ├── kidney.h5
│   └── skin.h5
├── /assets
│   └── sample_images/
├── app.py
├── classify.py
├── requirements.txt
└── README.md
