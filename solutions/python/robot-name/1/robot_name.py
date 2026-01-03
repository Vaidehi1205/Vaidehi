import random
import string

class Robot:
    _used_names = set()

    def __init__(self):
        self.name = None
        self.reset()

    def reset(self):
        self.name = self._generate_unique_name()
        Robot._used_names.add(self.name)


    def _generate_unique_name(self):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            digits = ''.join(random.choices(string.digits, k=3))
            candidate = f"{letters}{digits}"
            
            if candidate not in Robot._used_names:
                return candidate

