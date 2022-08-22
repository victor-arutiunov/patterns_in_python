from abc import ABCMeta, abstractmethod


class WebSock(metaclass=ABCMeta):

    def __init__(self, user_implementation):
        self.user_implementation = user_implementation

    @abstractmethod
    def authorize():
        """some code which authorize the user"""

    @abstractmethod
    def send_user_data():
        """some code which sends data of current user"""


class ReactWebSock(WebSock):

    def authorize(self):
        creds: dict = self.user_implementation.get_credentials()
        print(f"Using user creds for authorization in React front: {creds}")

    def send_user_data(self):
        data: dict = self.user_implementation.get_data()
        print(f"Send data about user to the React front: {data}")


class VueWebSock(WebSock):

    def authorize(self):
        creds: dict = self.user_implementation.get_credentials()
        print(f"Using user creds for authorization in Vue front: {creds}")

    def send_user_data(self):
        data: dict = self.user_implementation.get_data()
        print(f"Send data about user to the Vue front: {data}")
