import time
import openai
from openai import OpenAI
client = OpenAI(api_key='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')
def GPT_Connceting():
	completion = client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Hello!"}])
	ans = completion.choices[0].message
while True:
	#try:
	GPT_Connceting()
	#except openai.APITimeoutError:
	#	print('网络错误')
	time.sleep(0.5)