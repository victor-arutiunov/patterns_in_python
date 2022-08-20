
class Pool():
    
    def __init__(self, cls, size, params: dict):
        self._reusables = [cls(**params) for _ in range(size)]
    
    def acquire(self):
        return self._reusables.pop()

    def release(self, reusable):
        self._reusables.append(reusable)


class GameTexture():
    
    def __init__(self, type, size):
        self.type = type
        self.size = size


def main():
    params = {
        "type": "voxel",
        "size": "32kb"
    }
    pool = Pool(GameTexture, 10, params)
    obj = pool.acquire()

    # use obj as you wish
    print(obj.type)
    print(obj.size)

    # return to poll
    pool.release(obj)


main()
