import os
from openai import OpenAI

messages = []

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def completion(message):
    global messages
    messages.append(
            {  
                "role":"user",
                "content": message
            }
        )
    
    chat_completion = client.chat.completions.create( messages=messages,
                         model="gpt-4o"
                        )

    #print(chat_completion)

    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }

    messages.append(message)
    print(f"Assistant:{message['content']}")

if __name__ == "__main__":
    print("Assistant: Hi I am assistant, How may I help you....\n")
    while True: 
        user_question = input("You: \n")
        completion(user_question)