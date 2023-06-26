"""Необходимо написать программу мобильных телефонов, в которые можно добавлять приложения"""

class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)

class AppVK:
    def __init__(self, name = "ВКонтакте"):
        self.name = name

class AppYouTube:
    def __init__(self, memory_max, name = "YouTube"):
        self.name = name
        self.memory_max = memory_max

class AppPhone:
    def __init__(self, phone_list, name = "Phone"):
        self.phone_list = phone_list
        self.name = name

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)

