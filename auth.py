# auth.py

def validateSignin(username, password):
    if username and password:
        return {"status": "success"}
    return {"status": "failure"}
