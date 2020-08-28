subj = {}
with open('./text_6.txt', encoding='utf-8') as init_f:
    a = init_f.readlines()
    for s in a:
        new_str = ''.join((i if i in '1234567890'else ' ') for i in s)
        new_2 = [int(i) for i in new_str.split()]
    print(f'{s.split()[0]} {sum(new_2)}')