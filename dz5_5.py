from random import randint

with open('text_5.txt', 'w+', encoding='utf-8') as file_5:
    file_5.write(' '.join([str(randint(1, 100)) for _ in range(1000)]))
    file_5.seek(0)
    print(sum(map(int, file_5.readline(). split())))
