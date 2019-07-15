import socket


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        pass

    def put(self, name, value, timestamp=None):
        pass


class ClientError(Exception):
    pass
