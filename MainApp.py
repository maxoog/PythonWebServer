from flask import Flask
from flask import request
from UserBank import *
import User

import json

app = Flask(__name__)

bank = UserBank.random_bank(capacity=100)


@app.get("/get_user/<id>")
def get_user(id: int):
    try:
        resp = Flask.make_response(app, json.dumps(bank.get(int(id)).__dict__))
        resp.headers.set("Content-Type", "json")
        print(resp.headers)
        return resp
    except User.NoSuchUserException:
        return "no such user"


@app.get("/get_all_users")
def get_all_users():
    users =list(map(lambda x: x.__dict__, bank.get_all()))
    return json.dumps(users)


@app.post("/change_user_name/<id>")  # curl -d "" "http://127.0.0.1:8000/change_user_name/3?new_name=maxooooon"
def change_user_name(id: int):
    new_name = request.args.get("new_name")
    try:
        print(id, new_name)
        bank.change_name(int(id), new_name)
        return get_user(id)
    except User.NoSuchUserException:
        print("exception")
        return "no such user"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)


