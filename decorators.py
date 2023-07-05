# import webbrowser
# def pr(func):
#     def wrapper(url):
#         print('Do f')
#         func(url)
#         print('Posle f')
#     return wrapper
#
# @pr
# def open_url(url):
#     webbrowser.open(url)
#
# open_url('https://roadmap.sh/python')

import webbrowser

def pre(f):
    def wrap(url):
        if '/' in url:
            f(url)
        else:
            print('incorrect url')
    return wrap

@pre # вместо прописывания для каждой функции декортаора(обертку) делаем так собачка(название декоратора
def open_url(url):
    webbrowser.open(url)

open_url('https://roadmap.sh/python')