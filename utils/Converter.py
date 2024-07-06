import requests
import json

def converter(content):
    url = "https://js2ts.com/api/chat"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "prompt": "Act as an expert programmer in Javascript and Typescript. \nYou Translate code from Javascript to Typescript. \n- Add types to all variables and functions (string, boolean etc.)\n- The user can alternatively ask to create a function or a UI component.\nIf the user provided a request to write code, create the function or code and return it.\nNever return a question or your personal comment. \n\n- Never include ``` in your responses. Never no include your own comments. \n- If no code was provided, or no function created - return #####.\n\nExample translating from JavaScript to Typescript:\n// React code in Javascript:\nimport React from 'react';\n\nfunction Greeting(props) {\n  return <h1>Hello, {props.name}!</h1>;\n}\n\nexport default Greeting;\n\n// React code in Typescript: \nimport React, { FC } from 'react';\n\ninterface GreetingProps {\n  name: string;\n}\n\nconst Greeting: FC<GreetingProps> = (props) => {\n  return <h1>Hello, {props.name}!</h1>;\n}\n\nexport default Greeting;"
    }

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,vi;q=0.8",
        "origin": "https://js2ts.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Content-Type": "text/plain; charset=utf-8"
    }

    response = requests.request("POST", url, data=json.dumps(payload, indent=2), headers=headers)

    return response.text