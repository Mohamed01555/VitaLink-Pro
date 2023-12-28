# import gpt3
from utils import *
import base64
from time import sleep
from asyncio import run
from langchain.prompts import PromptTemplate
import streamlit as st
from pathlib import Path
from streamlit_option_menu import option_menu
import g4f
# import freeGPT as fgpt

# async def get_answer_from_youbot(question):
#     try:
#         resp = await fgpt.gpt4.Completion().create(question)
#         return resp
#     except:
#         st.info('Service may be stopped or you are disconnected with internet. Feel free to open an issue here "https://github.com/Mohamed01555/VideoQuERI"')
#         st.stop()

# async def get_answer_from_GPT3(question):
#     try:
#         resp = await fgpt.gpt3.Completion().create(question)
#         return resp
#     except:
#         st.info('Service may be stopped or you are disconnected with internet. Feel free to open an issue here "https://github.com/Mohamed01555/VideoQuERI"')
#         st.stop()

# async def get_answer_from_alpaca(question):
#     try:
#         resp = await fgpt.alpaca_7b.Completion().create(question)
#         return resp
#     except:
#         st.info('Service may be stopped or you are disconnected with internet. Feel free to open an issue here "https://github.com/Mohamed01555/VideoQuERI"')
#         st.stop()

question_prompt_template = """
            Role: Personalized Virtual Health Assistant (PVHA)

            Main Task: Act like a physical fitness trainer with 30 years of experience and
                       provide actionable health advice and recommendations based on the my profile.

            My Profile:
            - Prefered language of answer: {lang}
            - Current Fitness Level: {cfl} (0 is the lowest, 10 is the heighest)
            - Health Goals: {hg}
            - Protein Supplement Use: {psu}
            - Chronic Diseases/Health Conditions: {cd}
            - Physical Disabilities/Limitations: {pd}
            - Age: {age} years
            - Free Time for Physical Activity: {ft}
            - Gender: {g}
            - pregnance status if Female: {ps}
            - you may take other parameters. Take them also into consiration while generating the response.

            My query is : {q}

            Your previous answer is : {prev_answer}

            Based on my profile provide an answer to my query with a plan to implement it.
            1- First help me accomplishing my Health Goal.
            2- Second guide with a detailed diet with examples of food, vegitables and fruit  with appointments.
            3- Third
                1. Identify aerobic sports suitable for me.
                2. Provide guidance on increasing the effectiveness of the my physical activity.
                3. Recommend types of sports activities suitable for me.
                4. Suggest ways to incorporate physical activity into the my daily routine.
                5. Outline the minimum amount of physical activity suitable for me.
                6. Offer general tips for a healthy lifestyle.
                

            Constraints: You must must must provide the answer my Prefered language

            Additionally, provide your answer with links to resources that helped u answering my question.
            
            Please don't meantion your Identity in the answer,e.g. don't say I am GPT 3.5 or GPT4 or whatever u r, instead act like a physical fitness trainer.
            
            Your answer in bullet points:
        """

prompt = PromptTemplate(input_variables=['lang', "cfl","hg", "psu", "cd", "pd", "age", "ft", "g", "ps", 'q', 'prev_answer'], template=question_prompt_template)

# async def get_answer_from_chatgpt(question):
#     try:
#         resp = await gpt3.Completion().create(question)
#         return resp
#     except:
#         st.info('Service may be stopped or you are disconnected with internet. Feel free to open an issue here "https://github.com/Mohamed01555/Waai_physicalHealth"')
#         st.stop()

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def main():
    # setup streamlit page
    st.set_page_config(
        page_title="VitaLink Pro",
        page_icon="logo.jpeg")
    
    option = option_menu(
    menu_title=None,
    options=["Home", "FAQs", "Contact"],
    icons=["house-check", "patch-question-fill", "envelope"],
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important", "background-color": "#333"},        
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#ff9900"},
        "nav-link-selected": {"background-color": "#6c757d"},
    }
    )   

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown(html_code, unsafe_allow_html=True)

    # initialize responses.
    if "responses" not in st.session_state:
        st.session_state.responses = []
    
    if "question" not in st.session_state:
        st.session_state.question = None

    with st.sidebar:
        title = st.markdown("""**"Hello, Welcome to `Vitalink Pro!` To provide you with a personalized health and fitness experience,
                                we'd like to gather some information. Please take a few minutes to answer the following questions:**""")
        
        language = st.radio('What is your prefered language?', ['العربية','English'])
        
        # model = st.radio('Please choose form our models', ['Model 1','Model 2', 'Model 3'])

        selected_value = st.slider("Please, rate your current fitness level", min_value=0, max_value=10, value=5, step=1)
        
        # Define a list of health goal options
        health_goal_options = ["Weight Loss", "Muscle Gain", "Overall Well-being"]

        # Display a multiselect for users to choose multiple health goals
        selected_health_goals = st.multiselect("What are your primary health and fitness goals?", health_goal_options)
    
        selected_protein_supplements = st.radio('Are you taking Protein supplements?', ['No','Yes'])
        
        selected_chronic_disease = st.radio('Do you suffer from chronic diseases?',  ['No','Yes'])
        if selected_chronic_disease == 'Yes':
            selected_chronic_disease = st.text_input('Please, mention your chronic diseases')
        
        selected_disability = st.radio('Do you suffer from a disability?', ['No','Yes'])
        if selected_disability == 'Yes':
            selected_disability = st.text_input('Please, mention your disability.')

        age = st.number_input('Enter your age, please.')

        free_time = st.text_input('When is your free time?')

        gender = st.radio('Please, Enter your gender.', ['Male', 'Female'])
        
        is_pregnant = None
        if gender == 'Female':
            is_pregnant = st.radio('Are you pregnant?', ['I am pregnant', 'I am not pregnant'])

    if option == 'Home':
        for response in st.session_state.responses:
            with st.chat_message(response['role']):
                st.markdown(response['content'], unsafe_allow_html=True)
        
        st.session_state.question = st.chat_input('Ask for nutritional guidance, AI-generated workouts, seek advice and ask questions about health.', key = 'giving a question')
        if st.session_state.question:
            with st.chat_message('user'):
                st.markdown(st.session_state.question, unsafe_allow_html=True)

            st.session_state.responses.append({'role':"user", 'content': st.session_state.question})
            with st.spinner("Please, don't enter a new question or change anything in the sidebar while the answer is being generated!"):
                with st.chat_message('assistant'):
                    st.session_state.message_placeholder = st.empty()

                    query = prompt.format(lang = language, cfl = selected_value, hg = selected_health_goals, psu = selected_protein_supplements, cd = selected_chronic_disease,
                                        pd = selected_disability, age = age, ft = free_time, g = gender, ps = is_pregnant,
                                        q = st.session_state.question, prev_answer = st.session_state.responses[-2]['content']if len(st.session_state.responses) >= 2 else '')
                    print(query)
                    # response = g4f.ChatCompletion.create(
                    #     model=g4f.models.gpt_35_turbo_0613,
                    #     messages=[{"role": "user", "content": query}],
                    # )

                    # ai_response = run(get_answer_from_chatgpt(query))     

                    response = g4f.ChatCompletion.create(model=g4f.models.gpt_4_32k, messages=[{"role": "user", "content": query}], stream=True)  # Alternative model setting
                  
                    # if model == 'Model 1':
                    #     response = run(get_answer_from_youbot(query))
                        
                    # if model == 'Model 2':
                    #     response = run(get_answer_from_GPT3(query))
                    
                    # if model == 'Model 3':
                    #     response = run(get_answer_from_alpaca(query))
                    # print(response)
                    # st.session_state.message_placeholder.markdown(response, unsafe_allow_html=True)                   

                    res = ''
                    for r in response:
                        res += r
                        st.session_state.message_placeholder.markdown(res, unsafe_allow_html=True)                   
            
                st.session_state.responses.append({'role' : 'assistant', 'content' : res})
           
    elif option == 'FAQs':
        FAQs()
    elif option == 'Contact':
        contact()
    else:
        donate()

if __name__ == '__main__':
    main()