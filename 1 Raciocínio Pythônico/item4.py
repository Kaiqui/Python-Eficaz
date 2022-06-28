from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))

print('Red:', my_values.get('red'))
print('Green:', my_values.get('green'))
print('Opacity:', my_values.get('opacity'))

# Para a query string 'red=5&blue=0&green='

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print('Red: %r' % red)
print('Green: %r' % green)
print('Opacity: %r' % opacity)

red1 = int(my_values.get('red', [''])[0] or 0)  # expressão dificil de ler

red2 = my_values.get('red', [''])  # expressão mais facil de ler, porem ainda nao muito clara
red2 = int(red2[0]) if red[0] else 0

green1 = my_values.get('green', [''])  # claro no entendimento
if green1[0]:
    green1 = int(green1[0])
else:
    green1 = 0


# função auxiliar, sempre melhor

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


green3 = get_first_int(my_values, 'green')
print(green3)
