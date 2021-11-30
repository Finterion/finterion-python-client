class ClientException(Exception):

    def __init__(self, message):
        super(ClientException, self).__init__(message)
