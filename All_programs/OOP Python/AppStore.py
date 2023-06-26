"""
Online app store for iOS devices
"""

class AppStore:
    apps = dict()

    @classmethod
    def add_application(cls, app):
        cls.apps[id(app)] = app

    @classmethod
    def remove_application(cls, app):
        cls.apps.pop(id(app))

    @classmethod
    def block_application(cls, app):
        obj = cls.apps.get(id(app))
        obj.blocked = True

    @classmethod
    def total_apps(cls):
        return len(cls.apps)


class Application:
    def __init__(self, name):
        if type(name) == str:
            self._name = name

        self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.total_apps)
