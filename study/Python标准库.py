from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['peety'] = 'python'
favorite_language['dog'] = 'php'
favorite_language['eggor'] = 'java'
favorite_language['bigin'] = 'c'

for name, language in favorite_language.items():
    print(name + "'s favorite language is " + language + ".")
