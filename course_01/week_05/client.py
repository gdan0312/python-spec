import time
import socket


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        request = 'get {key}\n'.format(key=key)
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(request.encode())
                data = sock.recv(1024).decode().strip()
                return self.parse(data)
            except socket.timeout:
                raise ClientError('timeout error')
            except socket.error as err:
                raise ClientError('socket error:', err)

    def put(self, name, value, timestamp=None):
        request = 'put {name} {value} {timestamp}\n'.format(name=name, value=value,
                                                            timestamp=timestamp or str(int(time.time())))
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(request.encode())
                sock.recv(1024).decode()
            except socket.timeout:
                raise ClientError('timeout error')
            except socket.error as err:
                raise ClientError('socket error:', err)

    def parse(self, data):
        metrics = {}
        try:
            for line in data.split('\n')[1:]:
                name, value, timestamp = line.split(' ')
                if name not in metrics:
                    metrics[name] = [(int(timestamp), float(value))]
                else:
                    metrics[name].append((int(timestamp), float(value)))
        except ValueError as err:
            raise ClientError('parsing error:', err)
        return metrics


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
