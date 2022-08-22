import os
from api import ReactWebSock, VueWebSock
from utils import Customer, Admin


def client_code():
    customer = Customer("DiscoMan777")
    admin = Admin("Martin")

    ENV = os.getenv("CurrentFront")
    if ENV == "React":
        web_sock = ReactWebSock(customer)
        web_sock.authorize()
    elif ENV == "Vue":
        web_sock = VueWebSock(admin)
    else:
        raise ValueError("Current frontend framewokr is not supported :(")

    web_sock.send_user_data()


client_code()
