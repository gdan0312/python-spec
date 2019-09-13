import asyncio


class ClientServerProtocol(asyncio.Protocol):
    metrics = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        if data.startswith('put'):
            _, name, value, timestamp = data.split(' ')
            if name not in ClientServerProtocol.metrics:
                ClientServerProtocol.metrics[name] = [(timestamp, value)]
            else:
                ClientServerProtocol.metrics[name].append((timestamp, value))
            return 'ok\n\n'
        elif data.startswith('get'):
            _, name = data.split(' ')
            return self.get_metrics(name)
        else:
            return 'error\nwrong command\n\n'

    def get_metrics(self, key):
        if key == '*':
            return 'ok\n\n'
        if key not in ClientServerProtocol.metrics:
            return 'ok\n\n'
        resp = 'ok'
        for tuple_ in ClientServerProtocol.metrics[key]:
            resp += '\n{key} {value} {timestamp}'.format(key=key, value=tuple_[1], timestamp=tuple_[0])
        resp += '\n\n'
        return resp


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server('127.0.0.1', 8888)
