# auth.py

def validateLogin(username, password):
    if not username:
        return False
    if not password:
        return False
    print("Login validated")
    return True
