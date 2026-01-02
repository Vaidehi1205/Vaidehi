class Luhn:
    def __init__(self, card_num):
        self.raw = card_num

        # Remove spaces
        cleaned = card_num.replace(" ", "")

        # Must be only digits and length > 1
        if not cleaned.isdigit() or len(cleaned) <= 1:
            self.valid_number = False
            self.c_list = []
            return

        self.valid_number = True
        self.c_list = [int(d) for d in cleaned]

        # Apply Luhn doubling from the right
        for i in range(len(self.c_list) - 2, -1, -2):
            self.c_list[i] *= 2
            if self.c_list[i] > 9:
                self.c_list[i] -= 9

    def valid(self):
        if not self.valid_number:
            return False

        return sum(self.c_list) % 10 == 0
