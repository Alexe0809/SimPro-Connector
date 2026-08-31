from openai import OpenAI   
import config

client = OpenAI(
    base_url='https://openrouter.ai/api/v1',
    api_key=config.OPENROUTER_API_KEY
)


if __name__ == '__main__':
    response = client.chat.completions.create(
        model = config.MODEL,
        messages = [{"role": "user", "content": "Привет! Ответь одним словом."}],
    )
    print(response.choices[0].message.content)