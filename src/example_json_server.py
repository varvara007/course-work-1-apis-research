import json

request_body = """
{
  "weight": 15,
  "age": 0.5,
  "sex": "male",
  "name": "Venya"
}
"""

response_body = """
{
  "status": "ok"
}

"""

def server(method: str, body: str) -> str:
    request = json.loads(body)
    if request["age"] >= 1:
        return json.dumps({"status": "ok"})
    else:
        return json.dumps({"status": "error", "reason": "too young"})


if __name__ == "__main__":
    response = server(method="PUT", body=request_body)
