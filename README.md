🩺 Health Vision – AI-Powered Medical Diagnosis
📚 Project Overview
Health Vision is an AI-powered web application developed using Streamlit that analyzes medical images and predicts possible diseases. It covers a wide range of medical conditions such as brain tumors, pneumonia, bone fractures, skin infections, kidney stones, and eye infections. The application processes uploaded images and uses pre-trained CNN models to classify them and suggest appropriate precautions.

🎯 Key Features
✅ Disease Detection:
Detects diseases from various medical categories such as brain, chest, bones, skin, kidneys, and eyes.
Provides classification results with high accuracy using deep learning models.
Frontend: Streamlit
Backend: Python (TensorFlow, OpenCV, NumPy)
Machine Learning Models: CNN models trained for different medical conditions

🧠 Model Details
The application utilizes several pre-trained CNN models for different categories:
All-in-One Model: Determines the category of the uploaded image.
Bone Model: Detects fractures and provides suggestions.
Brain Model: Identifies tumors such as glioma, meningioma, pituitary, or no tumor.
Chest Model: Detects pneumonia or normal condition.
Eye Model: Recognizes glaucoma, diabetic retinopathy, cataract, and normal conditions.
Kidney Model: Detects cysts, tumors, stones, or normal conditions.
Skin Model: Identifies various skin conditions such as melanoma, keratosis, and carcinoma.

🚀 Installation and Setup
Step 1: Clone the Repository
git clone https://github.com/your-username/health-vision.git
cd health-vision
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Run the Application
streamlit run app.py

📸 Usage Instructions
Launch the Application: Run app.py using Streamlit.
Upload Medical Images: Upload images in .jpg, .png, or .jpeg format.
View Predictions: Get possible disease predictions along with precautionary advice.

📂 Project Structure
/health-vision
├── /models
│   ├── all-in-one.h5
│   ├── brain.h5
│   ├── bone.h5
│   ├── chest.h5
│   ├── eye.h5
│   ├── kidney.h5
│   └── skin.h5
├── /assets
│   └── logo.png
├── /templates
│   └── index.html
├── app.py
├── model.py
├── requirements.txt
└── README.md

📦 Dependencies
1.streamlit
2.tensorflow
3.opencv-python
4.numpy
5.pillow
Install all dependencies using:
pip install -r requirements.txt

📧 Contact
For any queries or feedback, feel free to reach out to:
📩 Email: arigalabalaji@example.com
🔗 LinkedIn: Arigala Balaji

