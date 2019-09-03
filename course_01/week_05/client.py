import time
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


if __name__ == '__main__':
    client = Client('127.0.0.1', 8888, timeout=15)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)

    print(client.get("*"))
