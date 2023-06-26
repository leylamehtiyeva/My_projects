class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj

    
