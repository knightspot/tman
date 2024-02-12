from datetime import datetime

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        
def create_user(name: str, email: str):
    print(f"DB: creating user database entry for {name} ({email}).")
    new_user = User(name, email)
    return new_user

def log(msg: str):
    print(f"{datetime.now()} - {msg}")