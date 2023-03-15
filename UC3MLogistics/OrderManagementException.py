"""Order Management Exception File"""
class order_management_exception(Exception):
    """Order Management Exception Class"""
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """message function"""
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value
