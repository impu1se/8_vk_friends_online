import vk
import sys
from getpass import getpass


APP_ID = 5724110  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input('Input your email: ')


def get_user_password():
    return getpass('Input your password: ')


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )

    except vk.exceptions.VkAuthError:
        sys.exit('Authorization error (incorrect password)')
    api = vk.API(session)
    return api.users.get(user_ids=api.friends.getOnline())


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
