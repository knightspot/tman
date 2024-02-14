from lib.log import log
from event import subscribe, unsubscribe

def handle_url_check_event(url):
    log(f"User registered with email address {url.content}")

def setup_url_event_handlers():
    subscribe("url_check", handle_url_check_event)
    
def unset_url_event_handlers():
    unsubscribe("user_password_forgotten", handle_user_password_forgotten_event)