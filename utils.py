import streamlit as st
from langchain.docstore.document import Document
from langchain.text_splitter import TokenTextSplitter
import re
import base64

def decode_unicode(text):
    return bytes(text, "utf-8").decode("unicode-escape")

# Define your FAQ questions and answers
def FAQs():
    faq = {
        "What is VitaLink Pro?":"A: VitaLink Pro is a personalized virtual health assistant (PVHA) designed to help you achieve your health and fitness goals. It provides tailored advice, workout plans, and nutrition guidance based on your individual profile.",
        "What key capabilities does VitaLink Pro offer?<ul>" :
        " <li>**Personalized Health Plans: **: Tailored workout routines and nutrition guidance based on your unique profile.</li>"
        " <li>**Adaptive Algorithms: **Advanced algorithms that adjust recommendations over time to match your progress.</li>"
        " <li>**Dietary Guidance:**: Customized nutritional advice to support your health and fitness goals.</li>"
        " <li>**User Privacy:**: Strict adherence to privacy and data protection regulations to ensure the security of your personal information.</li>" ,
    
        "How can I benefit from using VitaLink Pro?":
        "A: VitaLink Pro offers personalized health plans, exercise routines, and nutrition advice to help you reach your fitness goals. It adapts to your current fitness level and preferences, making it a valuable tool for anyone seeking a healthier lifestyle.",
        
        "What makes VitaLink Pro different from other health apps?":
        "A: VitaLink Pro stands out with its advanced language models and personalized approach. It takes into account your unique health profile, providing tailored advice and recommendations for a more effective fitness journey.",
        "How does VitaLink Pro generate personalized health plans?":"    A: VitaLink Pro uses advanced algorithms and user-provided information, such as fitness level, health goals, and preferences, to generate personalized health plans. It adapts over time, ensuring the recommendations stay relevant to your progress.",
        
        "Can VitaLink Pro help with specific health conditions or fitness goals?" :
        "A: Yes, VitaLink Pro is designed to assist users with a variety of health conditions and fitness goals. Whether you're looking to lose weight, build muscle, or manage specific health concerns, the app tailors its recommendations to meet your needs.",
        
        "Is my personal information safe and secure on VitaLink Pro?":
        "A: Yes, we prioritize user privacy and data security. Your personal information is kept confidential, and we adhere to strict privacy and data protection regulations to ensure a secure user experience." ,

        "Can I use VitaLink Pro if I'm a beginner in fitness?" : 
        "A: Absolutely! VitaLink Pro is designed for users of all fitness levels, from beginners to advanced. The app adapts to your current fitness level and provides guidance suitable for your experience and goals.",
        
        "How often should I use VitaLink Pro for optimal results?":
        "A: For optimal results, aim to incorporate VitaLink Pro into your daily routine. Follow the personalized plans, engage in regular physical activity, and make healthy lifestyle choices. Consistency is key to seeing positive changes.",
        
        "Can I use VitaLink Pro for dietary guidance?":
        "A: Yes, VitaLink Pro includes dietary guidance as part of its personalized approach. It provides recommendations on nutrition based on your goals and preferences, helping you make informed choices for a balanced diet.",

        "How does VitaLink Pro ensure user engagement and motivation?":
        "A: VitaLink Pro fosters engagement through personalized plans, progress tracking, and regular updates. The app's adaptive nature and variety in recommendations keep users motivated on their fitness journey.",
    }
    # with st.expander("FAQs"):
    for i, faq_key in enumerate(faq.keys()):
        # with st.sidebar.expander(faq_key):
        st.write(f"**Q{i+1}. {faq_key}**\n \n**Answer** : {faq[faq_key]}", unsafe_allow_html=True)
        st.write('-'*50)

def contact():
    mail = """<h2><a href="mailto:nemo45627@gmail.com">Email</a></h2>"""
    linkedin = """<h2><a href="https://www.linkedin.com/in/mohamed-algebali-213672173/">Linkedin</a></h2>"""

    con = f"""
        <h1>We can contact via :
        <ul>
            <li>{mail}</li>
            <li>{linkedin}</li>
        </ul>
        </h1>
"""
    st.markdown(con, unsafe_allow_html=True)

def donate():
    pass

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo='logo.jpeg'
img = get_img_as_base64(logo)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
# background-image: url("data:image/jpeg;base64,{img}");
# background-size: auto;
# # opacity:0.8;
# background-position: center;
# background-repeat: no-repeat;
# background-attachment: local;

}}

[data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/jpeg;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
margin-top: 0px;

background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

[data-testid="stExpander"]{{
margin-top:50px
}}


[data-testid="stVerticalBlock"]{{
margin-top: -5px;
# margin-top:30px
}}
</style>
"""

html_code = """
<div style="display: flex;justify-content: center;align-items: center;">
    <h2 style="text-align: center;color:'#547859'">VitaLink Pro!</h2>
    <h3 style='text-align: center; color: '#FFFFFF';'>Your Personalized Health Assistant</h3>
    <img style="width: 75px; margin-right: 10px; border-radius:50px "" src="data:image/jpeg;base64,{}" alt="Image Description">
</div>
""".format(img)


