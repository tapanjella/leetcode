def romanToInt(self, s: str) -> int:
    roman = {}
    roman['I'] = 1
    roman['V'] = 5
    roman['X'] = 10
    roman['L'] = 50
    roman['C'] = 100
    roman['D'] = 500
    roman['M'] = 1000
    total = curr = prev = 0
    for i in range(len(s)):
        curr = roman[s[i]]
        if curr > prev:
            total = total + curr - 2*(prev)
        else:
            total += curr
        prev = curr
    return total