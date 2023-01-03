favorite_languages_poll= {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

pollers = ['james','jen','emelia','edward','phil','mulenga','jen','grand','sarah']

for poller in sorted(pollers):
    if poller in favorite_languages_poll:
        print(f'{poller.title()}, thank you so much for participating')
    else:
        print(f'{poller.title()}, would you also like to participate in the poll?')