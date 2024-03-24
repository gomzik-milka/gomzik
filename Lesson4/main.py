def input_int
while True:
    try:
        def input_int(message):
            result = int(input(message))
            return result

    number = input_int('Введіть число:')
    print(number)
    break
    except ValueError:
        print('Введіть число')


