import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load env vars
load_dotenv()

# Initialize the client once
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION") 
)

# Store conversation history globally
conversation_history = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information. "
                        "You should remember previous questions and answers to maintain continuity."

                        
            }
        ]
    }
]

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]


def OpenAIresponse(UserQuestion):
    global conversation_history

    # Add user message to history


    messages.append({"role": "user", "content": UserQuestion})
    
    
    conversation_history.append({
        "role": "user",
        "content": [{"type": "text", "text": UserQuestion}]
    })

    # Send conversation history to Azure OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation_history,
        max_tokens=500,
        temperature=0.2,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )

    response_text = completion.choices[0].message.content

    # Save assistant response to history (for continuity)
    conversation_history.append({
        "role": "assistant",
        "content": [{"type": "text", "text": response_text}]
    })

    return response_text



#print(OpenAIresponse("Who is the President of Ghana?"))

print(OpenAIresponse("How long has he been presient?"))


#print(OpenAIresponse("who did he succeed?"))

#print(np.arange(10))

