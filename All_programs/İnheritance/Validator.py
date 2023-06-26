class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, *args, **kwargs):
        return self.data
