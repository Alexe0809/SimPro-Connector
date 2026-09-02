from openai import OpenAI   
import config
import json
from tools import tools, available_functions

client = OpenAI(
    base_url='https://openrouter.ai/api/v1',
    api_key=config.OPENROUTER_API_KEY
)

def run(user_message):
    messages = [
        {"role": "system", "content": "You are assistant who are worjing with Simpro system"},
        {'role':'user', 'content':user_message}]

    while True:
        response = client.chat.completions.create(
            model = config.MODEL,
            messages = messages,
            tools=tools
                )
        msg = response.choices[0].message
        messages.append(msg)

        if not msg.tool_calls:
            return msg.content

        for call in msg.tool_calls:
            name = call.function.name
            args = json.loads(call.function.arguments)
            func = available_functions[name]
            result = func(**args)
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": json.dumps(result, ensure_ascii=False),
            })

        


if __name__ == '__main__':
       print(run("Найди клиента ABC и найди его работу"))