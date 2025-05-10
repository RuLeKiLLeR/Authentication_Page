# auth.py

def validateSignup(username, password):
    if username and password:
        return {"status": "success"}
    return {"status": "failure"}
