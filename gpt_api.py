import base64
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def gpt_api_image(image_path):
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    base64_image = encode_image(image_path)
    # Convert your entire request into a single message string
    user_message = f"Extract all details from this image: data:image/jpeg;base64,{base64_image}"

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or any model you have access to
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
    )

    return response.choices[0].message.content

def gpt_api_text(system_message, text):
    completion = openai.ChatCompletion.create(
        model="gpt-4", # or another model you have access to
        messages=[
            {"role": "system", "content": f"{system_message}"},
            {"role": "user", "content": f"{text}"}
        ]
    )
    return completion.choices[0].message.content

def gpt_api_solver(text):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You have been given a question. Determine the best option and provide the answer in full."
            },
            {"role": "user", "content": text}
        ]
    )
    return completion.choices[0].message.content
