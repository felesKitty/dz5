print('Введите ваши данные, уважаемый  \nКогда захотите '
      'закончить, введите пустую строку ')
with open('dz_file1.txt', 'x', encoding='utf-8') as dz_file1:
    while (data := input()) != '':
        dz_file1.write(f'{data}\n')
