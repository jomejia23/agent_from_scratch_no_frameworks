from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print("mi primer agente!")

client = OpenAI()

Messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]
while True:
    user_input = input("You: ")
    
    #Validations
    if not user_input:
        continue
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    
    #History user update
    Messages.append({"role": "user", "content": user_input})
    
    response = client.responses.create(
        model="gpt-4o",
       input=Messages
    )
    
    #History agent update
    assistant_reply = response.output_text
    Messages.append({"role": "assistant", "content": assistant_reply})
    
print(response.output_text)
