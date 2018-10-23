leet = {
    'A': '4',
    'B': '8',
    'C': '<',
    'D': '[)',
    'E': '&',
    'F': 'ph',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': 'j',
    'K': '|<',
    'L': '|_',
    'M': '|\/|',
    'N': '/\/',
    'O': '0',
    'P': '|*',
    'Q': '9',
    'R': 'l2',
    'S': '5',
    'T': '7',
    'U': 'v',
    'V': 'V',
    'W': 'vv',
    'X': '><',
    'Y': '`/',
    'Z': '2'
}
#admito que o alfabeto aq eu peguei de outro cara rsrs, mó preguissa de fazer um.
texto = input('Texto: ')
for i in texto.upper():
    if i in leet:
        print(leet[i], end='')
