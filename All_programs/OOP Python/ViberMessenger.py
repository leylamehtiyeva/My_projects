class Viber:
    """
    Messenger class
    """
    messages = dict()

    @classmethod
    def add_message(cls, msg):
        """
        adding a new message to the message list;
        :param msg: a new message we want to add
        """
        cls.messages[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        """
        deleting a message from the list;
        :param msg: the message we want to delete
        """
        cls.messages.pop(id(msg))

    @classmethod
    def set_like(cls, msg):
        """
        put/remove a like for the msg message
        (i.e. change the fl_like attribute of the msg object:
        if there is no like, then it is put, if there is already, then it is removed);
        :param msg: the message to be liked/unliked
        """
        obj = cls.messages.get(id(msg))
        if obj.fl_like == False:
            obj.fl_like = True
        else:
            obj.fl_like = False

    @classmethod
    def show_last_message(cls, num):
        """
        display of recent messages;
        :param num: how many recent posts we want to see
        :return: list of recent messages
        """
        return list(cls.messages.values())[-num:]

    @classmethod
    def total_messages(cls):
        """
        Counts the total number of messages currently.
        :return: returns the total number of messages from the dictionary of messages
        """
        return len(cls.messages)


class Message:
    """
    Allows you to create message objects
    """

    def __init__(self, text):
        if type(text) == str:
            self.text = text
        self.fl_like = False

