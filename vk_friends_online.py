import vk
from getpass import getpass

APP_ID = 6460978
VK_API_VERSION = 5.74


def get_user_login():
    return input("Please, input user id: ")


def get_user_password():
    return getpass("Please, input password: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session, v=VK_API_VERSION)

    friends_online_ids = api.friends.getOnline()

    friends_online = api.users.get(
        user_ids=friends_online_ids,
        fields=["first_name", "last_name"]
    )

    return friends_online


def output_friends_to_console(friends_online):
    for friend_record in friends_online:
        print(
            friend_record['first_name'],
            friend_record['last_name']
        )


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
