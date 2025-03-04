from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Listas o nome do produtos, sem considerar descrição"
        },{
            "role": "user",
            "content": "Liste três produtos sustentaveis"
        }
    ], model="gpt-4"
)
print(resposta.choices[0].message.content)