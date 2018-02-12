import vk
import sys
from getpass import getpass


APP_ID = 5724110  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input('Input your email: ')


def get_user_password():
    return getpass('Input your password: ')


def open_vk_session(login, password):
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
    return api
    

def input_choice():
    return input('''Enter your choice:
    1. Print friends online
    2. Print top apps from friends\n''')


def get_online_friends(api_session):
    return api_session.users.get(user_ids=api_session.friends.getOnline())


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


def get_apps_of_friends(api_session):
    top_apps = []
    amount_apps = 100
    list_apps = api_session.apps.getCatalog(
        sort='visitors', 
        count=amount_apps, 
        return_friends=1
        )
    for app in range(1, amount_apps+1):
        top_apps.append(
            (list_apps[str(app)]['title'], len(list_apps[str(app)]['friends']))
            )
    top_apps.sort(key=lambda amount: amount[1], reverse=True)
    return top_apps         


def output_top_apps_of_friends(top_apps):
    for app in top_apps[:11]:
        print(app[0])


def main():
    choice = input_choice()
    login = get_user_login()
    password = get_user_password()
    api_vk = open_vk_session(login, password) 
    if choice == '1':
        friends_online = get_online_friends(api_vk)
        output_friends_to_console(friends_online)
    else:
        top_apps = get_apps_of_friends(api_vk)
        output_top_apps_of_friends(top_apps)


if __name__ == '__main__':
    main()
