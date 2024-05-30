
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


messages = [{"role": "system", "content": "Always answer in rhymes."}]



while True:
    user_input = input("Prompt : ")
    messages.append({"role": "user", "content": user_input})


    res = client.chat.completions.create(
        model="model-identifier",
        messages=messages,
        temperature=0.9,
        # max_token = -1
    )
    # print(res)
    print(res.choices[0].message)

    messages.append({'role':'assistant','content':res.choices[0].message.content})


