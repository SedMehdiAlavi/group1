#!/usr/bin/env  python3
import logging
import argparse
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("HW.log", mode="a")

file_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.WARNING)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged = False
    def login(self ,username , password):
        if  self.is_logged:
            logger.warning(f"User {self.username} logged in")
            # return f" you are already logged in. {self.username}"

        else:

            # input_username = input("Username: ")
            # input_password = input("Password: ")

            if username == self.username and password == self.password:
                self.is_logged = True
                logger.info(f"User {self.username} logged in")
            else :
                logger.warning(f"User {self.username} try with wrong password")

    def logout(self):
        if self.is_logged:
            self.is_logged = False
            logger.info(f"User {self.username} log out ")
        else:
            logger.warning(f"User {self.username} not logging")
            # return f" you are not logged in. {self.username}"

parser = argparse.ArgumentParser(description="login menu")
sub = parser.add_subparsers(dest="command")
login = sub.add_parser("login")
login.add_argument("-u", "--username", required=True)
login.add_argument("-p", "--password", required=True)
parser.add_argument("--logout")
parser.add_argument("--show")
parser.add_argument("--exit" )



logout  = sub.add_parser("logout")
show = sub.add_parser("show")
exit = sub.add_parser("exit")

user1 = User("akbar", "123")
args = parser.parse_args()
if args.command == "login":
    user1.login(args.username, args.password)
elif args.command == "logout":
    user1.logout()
elif args.command == "show":
    print(user1.is_logged)
elif args.command == "exit":
    user1.logout()


























# user2 = User("Ali_akbar", "456")
# print(f"Username : {user1.username}")
# print(f"Password : {user1.password}")
# print(f"Username : {user2.username}")
# print(f"Password : {user2.password}")
#
# user1.login()
# user2.login()







