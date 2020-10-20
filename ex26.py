class Roman_int:
    def convert(self, s):
        roman = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5 }
        int = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                int += roman[s[i]] - 2 * roman[s[i - 1]]
            else:
                int += roman[s[i]]
        return int

print(Roman_int().convert('V'))
