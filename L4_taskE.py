list = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['M', 'MM', 'MMM']
        ]

def f(string):
    sum = 0
    for k,i in enumerate(reversed(list)):
        for l,j in  enumerate(reversed(i)):
            if string.startswith(j):
                if k != 0:
                    sum += 10 ** (3 - k) * (9 - l)
                else:
                    sum += 10 ** (3 - k) * (3 - l)
                string = string.replace(j,"")
    print(sum)

f('MMMCMV')
