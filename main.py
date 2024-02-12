import http.client
from lib.log_listener import setup_log_event_handlers, unset_log_event_handlers
from event import post_event


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    

def create_user(name: str, email: str):
    # print(f"DB: creating user database entry for {name} ({email}).")
    new_user = User(name, email)
    return new_user

def send_events():
    user = create_user("J***s", "****@*******.se")
    post_event("user_registered", user)
    post_event("user_password_forgotten", user)
    post_event("user_upgrade_plan", user)
    
    
            
""" 
conn =  http.client.HTTPSConnection("h****rg.troman****k.**")
conn.request("GET", "/")
response = conn.getresponse()

response_bytes = response.read()
response.close()

response_text = response_bytes.decode("utf-8")

print(f"Text: {response_text}")
 """
setup_log_event_handlers()

send_events()

unset_log_event_handlers()

send_events()


    


