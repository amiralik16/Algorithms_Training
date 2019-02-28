class Hashmap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size
    
    def _hash(self,key):
        h = sum([ord(char) for char in key])
        return h % self.size

    def add(self,key,value):
        h = self._hash(key)
        if self.map[h]:
            for pair in self.map[h]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[h].append([key,value])
            return True
        else:
            self.map[h] = [[key,value]]
            return True

    def get(self,key):
        h = self._hash(key)
        if self.map[h]:
            for pair in self.map[h]:
                if pair[0] == key:
                    return pair[1]
        else:
            raise KeyError
        
    def delete(self,key):
        h = self._hash(key)
        if self.map[h]:
            for i,pair in enumerate(self.map[h]):
                if pair[0] == key:
                    self.map[h].pop(i)
                    if self.map[h] == []:
                        self.map[h] = None
                    return True
            raise KeyError

        else:
            raise KeyError

    def __str__(self):
        lines = []
        lines.append("____MAP____")
        for el in self.map:
            if el:
                lines.append(str(el))
        return '\n'.join(lines)

            

if __name__ == "__main__":
    testmap = Hashmap()
    testmap.add('absent', 53)
    testmap.add('absent', 122)
    testmap.add('a', 51)
    testmap.add('c', 21)
    testmap.add('barbra', 212)
    print(testmap.get('absent'))
    print(testmap)
    print(testmap.map)
    testmap.delete('barbra')
    print(testmap)
    print(testmap.map)