CURRENT_OS = 'linux'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        return cls.create_windows_filedialog(*args) if CURRENT_OS == 'windows' \
            else cls.create_linux_filedialog(*args)

    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
print(dlg)



