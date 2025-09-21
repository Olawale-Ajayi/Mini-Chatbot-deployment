import numpy as np
import pandas as pd
from openai import AzureOpenAI
import os
from dotenv import load_dotenv
load_dotenv()




def OpenAIresponse(UserQuestion):
    client = AzureOpenAI(
        azure_endpoint= os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION") 
    )




    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are an AI assistant that helps people find information. You should be able to keep memory of your previous questions to do chat continuity on previous chats"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": UserQuestion
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "As of my last knowledge update in October 2023, the Managing Director/Chief Executive Officer (MD/CEO) of **Wema Bank** is **Moruf Oseni**. He officially assumed the role on **April 1, 2023**, succeeding **Ademola Adebise**.\n\nMoruf Oseni had previously served as the bank's Deputy Managing Director before being elevated to the MD/CEO position. Please verify this information with the latest updates from Wema Bank's official website or recent news sources, as leadership positions can change."
                }
            ]
        }
    ]


    messages = chat_prompt

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=500,
        temperature=0.2,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )

    code = completion.choices[0].message.content

    return code

























print(OpenAIresponse("Who is the President of Nigeria"))





























