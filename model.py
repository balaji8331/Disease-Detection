import tensorflow as tf
import cv2
import numpy as np
import streamlit as st

def classify(img):
    im = img
    lt = ["other","Bone","Brain","eye","kidney","chest","skin"] 
    im = cv2.resize(im,(52,52))
    model = tf.keras.models.load_model("all-in-one.h5",compile=False)
    result = model.predict(np.array([im]))
    a = np.argmax(result)
    c=""
    
    if a==0:
        st.write('________________________________________________')
        return "Provide the medical Imaging of the mentioned categories",""
        # st.write('________________________________________________')
    if a==1:
        st.write('________________________________________________')
        c= bone_net(im)
        # st.write('________________________________________________')
    if a==2:
        st.write('________________________________________________')
        c= brain_net(im)
        # st.write('________________________________________________')
    if a==3:
        st.write('________________________________________________')
        c= Eye_net(im)
        # st.write('________________________________________________')
    if a==4:
        st.write('________________________________________________')
        c= kidney_net(im)
        # st.write('________________________________________________')
    if a==5:
        st.write('________________________________________________')
        c= chest_net(im)
        # st.write('________________________________________________')
    if a==6:
        st.write('________________________________________________')
        c= skin_net(im)
    return c



def bone_net(img):
    # img = cv2.resize(img,(224,224))
    lt = ["Normal",'Fractured']
    model = tf.keras.models.load_model("fracture.h5",compile=False)
    result = model.predict(np.array([img]))
    ans = np.argmax(result)
    a=""
    b=""
    if ans==0:
        a="Normal "
        b="There is no bone facture detected"
    if ans==1:
         a="Fractured"
         b="There is  bone facture.\nconsult doctor Immediately\nApply ice: Apply ice to the affected area to reduce swelling and pain. Wrap the ice in a cloth or towel and apply it to the area for 15-20 minutes at a time, several times a day."
    return a,b

def brain_net(img):
    lt = ['pituitary', 'notumor', 'meningioma', 'glioma']
    # img = cv2.resize(img,(52,52))
    model = tf.keras.models.load_model("brain.h5",compile=False)
    result = model.predict(np.array([img]))
    ans = np.argmax(result)
    b = ""
    c = ""
    if ans==3:
        b = f"Glioma: Can range from low-grade (mild) to high-grade (severe)."
        c = "\n\nAvoid activities that could cause head injury, such as contact sports.\nTake steps to manage seizures, which can be a common symptom of gliomas.\nAvoid exposure to radiation, as this can increase the risk of developing a glioma.\nTake steps to reduce stress, which can exacerbate symptoms and affect overall health.\nWork with a healthcare provider to manage any other underlying medical conditions that could impact treatment."
    if ans==2:
        b = f"Meningioma: Most are low-grade."
        c = "\n\nAvoid activities that could cause head injury, such as contact sports.\nWork with a healthcare provider to manage any underlying medical conditions, such as high blood pressure, that could impact treatment.\nBe aware of potential symptoms, such as headaches or changes in vision, and seek medical attention promptly if they occur.\nTake steps to reduce stress, which can exacerbate symptoms and affect overall health.\nFollow a healthy lifestyle, including a balanced diet, regular exercise, and adequate sleep."
    if ans==1:
        b = "No tumor: N/A \n\n Enjoy the Life "
        c = "No Tumor has been detected \n Follow the precautions be healthy"
    if ans==0:
        b = f"Pituitary: Can be either benign or malignant."
        c = "\n\n Work with a healthcare provider to manage any underlying medical conditions, such as diabetes, that could impact treatment.\nBe aware of potential symptoms, such as headaches or changes in vision, and seek medical attention promptly if they occur.\nFollow a healthy lifestyle, including a balanced diet, regular exercise, and adequate sleep.\nTake steps to manage any hormonal imbalances that may result from the tumor.\nAvoid exposure to radiation, as this can increase the risk of developing pituitary tumors"
    return b,c

def chest_net(img):
    lt = ['PNEUMONIA', 'NORMAL']
    # img = cv2.resize(img,(224,224))
    model = tf.keras.models.load_model("chest.h5",compile=False)
    result = model.predict(np.array([img]))
    ans = np.argmax(result)
    d=""
    e=""
    if ans==0:
        d=f" Might be you are effected by pneumonia  "
        e=f"Vaccination is the best protection against pneumonia."
    if ans==1:
        d=f"Normal"
        e=f"Practice good hygiene by washing your hands frequently and avoiding touching your face"
    return d,e

def Eye_net(img):
    lt = ['glaucoma', 'normal', 'diabetic_retinopathy', 'cataract']
    # img = cv2.resize(img,(224,224))
    model = tf.keras.models.load_model("eye.h5",compile=False)
    result = model.predict(np.array([img]))
    f=""
    g=""
    if ans==3:
        f=f"You are Effected by Cataract"
        g=f'Protect your eyes from harmful UV rays with sunglasses or a hat.'
    if ans==2:
        f=f"Diaetic Retinopathy"
        g='Control your blood sugar levels to prevent diabetic retinopathy.'
    if ans==1:
        f=f"normal CONDITION"
        g='You are in Normal condition , Maintain same '
    if ans==0:
        f=f'glaucoma detected'
        g="Follow your doctor's instructions for taking glaucoma medications."
    ans = np.argmax(result)
    return f,g

def kidney_net(img):
    lt = ['Cyst', 'Tumor', 'Stone', 'Normal']
    # img = cv2.resize(img,(224,224))
    model = tf.keras.models.load_model("kidney.h5",compile=False)
    result = model.predict(np.array([img]))
    ans = np.argmax(result)
    h=""
    i=""
    if ans==0:
        h="Cyst"
        i="Avoid drinking alcohol, as it can irritate the kidneys and cause cysts to form.\nMaintain a healthy weight to reduce the risk of developing cysts."
    if ans==1:
        h="Tumor"
        i="Quit smoking to reduce the risk of kidney tumors.\nMaintain a healthy diet, rich in fruits and vegetables, to prevent the development of tumors.\nStay physically active to reduce the risk of developing tumors."
    if ans==2:
        h="Stone"
        i="Drink plenty of water to prevent the formation of kidney stones.\nLimit your intake of salt and animal protein to reduce the risk of developing stones.\nEat a diet rich in fruits and vegetables to prevent the formation of stones."
    if ans==3:
        h="Normal"
        i="You are in Normal Condition\n Be safe"
    return h,i

def skin_net(img):
    lt = ['pigmented benign keratosis', 'melanoma', 'vascular lesion', 'actinic keratosis', 'squamous cell carcinoma', 'basal cell carcinoma', 'seborrheic keratosis', 'dermatofibroma', 'nevus']
    # img = cv2.resize(img,(224,224))
    model = tf.keras.models.load_model("skin.h5",compile=False)
    result = model.predict(np.array([img]))
    ans = np.argmax(result)
    l=""
    m=""
    if ans==0:
        l="pigmented benign keratosis"
        m="Protect your eyes from excessive exposure to sunlight or other sources of UV radiation.\nAvoid rubbing or scratching the affected area to prevent irritation or injury."
    if ans==1:
        l="melanoma"
        m="Regular eye exams with a qualified healthcare professional can help detect early signs of melanoma in the eye.\nWearing UV-protective eyewear and avoiding prolonged exposure to sunlight can help reduce the risk of developing melanoma in the eye."
    if ans==2:
        l="vascular lesion"
        m="Vascular lesions in the eye can be fragile and prone to bleeding, so it is important to avoid any activities that can increase intraocular pressure, such as heavy lifting or straining."
    if ans==3:
        l="actinic keratosis"
        m="Protect your eyes from UV radiation by wearing UV-blocking sunglasses or a hat with a brim.\nAvoid prolonged exposure to sunlight, especially during peak hours when the sun's rays are strongest."
    if ans==4:
        l="squamous cell carcinoma"
        m="Avoid smoking and limit alcohol consumption as they increase the risk of developing squamous cell carcinoma in the eye."
    if ans==5:
        l="basal cell carcinoma"
        m="Wear protective eyewear.\nMonitor your skin for any changes or abnormalities."
    if ans==6:
        l="seborrheic keratosis"
        m="Seborrheic keratosis near the eye should be examined by a healthcare professional to rule out the possibility of malignant growth.\nAvoid rubbing or scratching the affected area around the eye to prevent irritation or injury."
    if ans==7:
        l="dermatofibroma"
        m="Avoid scratching or picking at the dermatofibroma to prevent infection and further irritation.\nProtect the dermatofibroma from direct sunlight or excessive heat exposure to prevent discoloration or changes in texture."
    if ans==8:
        l="nevus"
        m="Regularly monitor the nevus and report any changes to your healthcare provider.\nProtect your eyes from excessive sun exposure by wearing sunglasses and a hat with a brim."
    return l,m