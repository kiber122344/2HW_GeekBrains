with open('text.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введи строку: ')
        if not line:
            f.write('\n')
            break
        f.write(line + '\n')
        print(line, file=f)