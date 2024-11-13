import os
import requests


PORT = os.environ.get('PORT', 4000)
HOST = os.environ.get('HOST', '0.0.0.0')
URL = f"http://{HOST}:{PORT}/"


if __name__ == "__main__":
    add_payload = {
        "jsonrpc": "2.0",
        "method": "add",
        "params": [2, 2],
        "id": 1
    }
    echo_payload = {
        "jsonrpc": "2.0",
        "method": "echo",
        "params": ["Hello, jRPC!"],
        "id": 1
    }
    response = requests.post(URL, json=add_payload)

    print("POST", URL, response.json())
