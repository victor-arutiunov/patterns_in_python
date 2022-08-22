from abc import ABCMeta, abstractmethod


class User(metaclass=ABCMeta):

    def __init__(self, username=None):
        self.username = username

    @abstractmethod
    def get_credentials():
        """return authorization data"""

    @abstractmethod
    def get_data():
        """return general and not sensitivity dat about user"""


class Admin(User):
    
    def get_credentials(self):
        print(f"Extracting {self.username} admin credentials from database...")
        return {"login": "admin", "password": "reliable_password"}

    def get_data(self):
        print(f"Extracting {self.username} admin data from database...")
        return {"favorite_color": "dark blue", "birthday": "09.28.1997"}


class Customer(User):
    def get_credentials(self):
        print(f"Extracting {self.username} user credentials from database...")
        return {"login": "typical_user", "password": "weak_password"}

    def get_data(self):
        print(f"Extracting {self.username} user data from database...")
        return {"favorite_color": "yellow", "birthday": "09.28.1984"}
