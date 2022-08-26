#10.Съставете програма на Python с използването на клас за преобразуване на цяло десетично число в римския му еквивалент и обратно.
class RomanNumeric:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        if type(self.number) == int:
            num = [1, 4, 5, 9, 10, 40, 50, 90,
                   100, 400, 500, 900, 1000]
            sym = ["I", "IV", "V", "IX", "X", "XL",
                   "L", "XC", "C", "CD", "D", "CM", "M"]
            i = 12

            while self.number:
                div = self.number // num[i]
                self.number %= num[i]

                while div:
                    print(sym[i], end="")
                    div -= 1
                i -= 1
        else:
            print(self.number)

    def to_numeric(self):
        if type(self.number) != int:
            rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            int_val = 0
            for i in range(len(self.number)):
                if i > 0 and rom_val[self.number[i]] > rom_val[self.number[i - 1]]:
                    int_val += rom_val[self.number[i]] - 2 * rom_val[self.number[i - 1]]
                else:
                    int_val += rom_val[self.number[i]]
            print(int_val)
        else:
            print(self.number)

roman_numeral = RomanNumeric(10)
roman_numeral.to_roman()
print("\n------------")
numeric = RomanNumeric("CM")
numeric.to_numeric()
