class Number:

    def __init__(self, num, base):

        # check base
        
        if not isinstance(base, int) or base <= 0:
            raise ValueError("Base must be a positive integer.")

        supported_systems = [2, 8, 10, 16]

        if base not in supported_systems:
            raise ValueError(f"Unsupported numeral system: base {base}.")

        self.base = base

        self.num = str(num).upper()

        # clean input

        if self.base == 10:
            self.num = self.num.replace(',', '')

        self.__sign = ''
        if self.num.startswith('-'):
            self.__sign = '-'
            self.num = self.num[1:]
        elif self.num.startswith('+'):
            self.num = self.num[1:]

        # check decimal points
            
        if self.num.count('.') > 1:
            raise ValueError("Number cannot have more than 1 decimal point.")

        if '.' in self.num:
            self.__int_part, self.__frac_part = self.num.split('.')
            self.__has_frac = True

        else:
            self.__int_part = self.num
            self.__frac_part = ''
            self.__has_frac = False

        # divide number to int part and frac part

        self.__int_part_digits = list(self.__int_part)
        if self.__has_frac:
            self.__frac_part_digits = list(self.__frac_part)
        else:
            self.__frac_part_digits = []

        alphabet = self.__alphabet()

        for d in self.__int_part_digits + self.__frac_part_digits:
            if d not in alphabet:
                raise ValueError(f"Invalid symbol [{d}] for base {self.base}.")

        if self.base == 16:
            self.__int_part_digits = self.__hex_digits(self.__int_part_digits)
            self.__frac_part_digits = self.__hex_digits(self.__frac_part_digits)

    def __alphabet(self):
        if self.base == 2:
            return list('01')
        elif self.base == 8:
            return list('01234567')
        elif self.base == 10:
            return list('0123456789')
        elif self.base == 16:
            return list('0123456789ABCDEF')

    def __hex_digits(self, listed_digits):
        hex_map = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
        for i,d in enumerate (listed_digits):
            listed_digits[i] = hex_map.get(d, d)
        return listed_digits

    def __int_to_dec(self):
        if self.base == 10:
            return int(self.__int_part)
        value = 0
        for i, d in enumerate(self.__int_part_digits[::-1]):
            value += int(d) * (self.base ** i)
        return value

    def __frac_to_dec(self):
        if self.base == 10:
            return self.__frac_part
        value = 0.0
        for i, d in enumerate(self.__frac_part_digits):
            value += int(d) * (self.base ** -(i + 1))
        
        return str(value)[2::]

    def __int_to_base(self, target_base):
        if self.base == target_base:
            return self.__int_part
        value = self.__int_to_dec()
        if value == 0:
            return '0'
        digits = ''
        while value > 0:
            digit = value % target_base
            if digit >= 10:
                digits = chr(ord('A') + digit - 10) + digits
            else:
                digits = str(digit) + digits
            value //= target_base
        return digits

    def __frac_to_base(self, target_base, precision=3):
        if not self.__has_frac:
            return ''
        if self.base == target_base:
            return self.__frac_part
        frac_value = float("0." + self.__frac_to_dec())
        result = ''
        for _ in range(precision):
            frac_value *= target_base
            digit = int(frac_value)
            if digit >= 10:
                result += chr(ord('A') + digit - 10)
            else:
                result += str(digit)
            frac_value -= digit
        return result

    # public API

    def to_dec(self):
        if self.__has_frac:
            return f"{self.__sign}{self.__int_to_dec()}.{self.__frac_to_dec()}"
        return f"{self.__sign}{self.__int_to_dec()}"

    def to_bin(self):
        if self.__has_frac:
            return (f"{self.__sign}{self.__int_to_base(2)}.{self.__frac_to_base(2)}")
        return (f"{self.__sign}{self.__int_to_base(2)}")

    def to_oct(self):
        if self.__has_frac:
            return f"{self.__sign}{self.__int_to_base(8)}.{self.__frac_to_base(8)}"
        return f"{self.__sign}{self.__int_to_base(8)}"

    def to_hex(self):
        if self.__has_frac:
            return f"{self.__sign}{self.__int_to_base(16)}.{self.__frac_to_base(16)}"
        return f"{self.__sign}{self.__int_to_base(16)}"