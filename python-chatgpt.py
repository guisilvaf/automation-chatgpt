import requests
import argparse
import os

parser = argparse.ArgumentParser(description="Sets a question.")
parser.add_argument("content", help="The prompt to send to the OpenAI API.")
parser.add_argument("file_name", help="Name of the file of the generated code.")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers={
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data={
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"Write python script to {args.content}, add '#' in the comments, also add a comment about what the code do."}],
    "max_tokens": 4000,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]['message']["content"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")