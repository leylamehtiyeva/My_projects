"""From the list, selects only those files that are in the tuple with extensions"""


class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions



    def __call__(self, name, *args, **kwargs):
        start = name.rfind('.')
        ext = '' if start == -1 else name[start + 1:]
        return ext in self.extensions

"""Note!! filter function returns elements for which the function passed to it returns True"""

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

