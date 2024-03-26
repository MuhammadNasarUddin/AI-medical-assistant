import streamlit as st
from openai import OpenAI, RateLimitError
import os
from dotenv import load_dotenv

load_dotenv()

st.title('🩺 Dr. AI')  # Added the st.title() with an emoji

client = OpenAI(api_key=os.environ['openai_api_key'])

medicine = st.text_input('Ask me about a medicine')
if st.button('Ask'):
    fetching_message = st.info('Processing...')
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Who are you?"},
                {"role": "assistant", "content": "As an AI language model, I am programmed to assist you with your queries and concerns to the best of my abilities"},
                {"role": "user", "content": "Where was it?"},
                {"role": "user", "content": f"Tell me about the details of this {medicine}, and its uses and side effects and how to use it?,and you can also tell me about the alternative of this medicine in just some not long paragraph,and if you don't know about this medicine just say i dont know about this."},
            ]
        )
        detail = response.choices[0].message.content
        fetching_message.empty()  # Remove the fetching message
        st.success(detail)
    except Exception as e:
        fetching_message.empty()  # Remove the fetching message if an error occurs
        st.error(f"An error occurred: {e}")
