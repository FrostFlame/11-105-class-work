async def log(msg):
    print(msg)


class AsyncManager:
    def __init__(self, msg):
        self.msg = msg

    async def __aenter__(self):
        print('')

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass