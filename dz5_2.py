with open('text_4.txt', 'r', encoding='utf-8') as f_obj:
    useful = [f'{line_number}) {line.strip()} - {len(line.split())} '
              f'слов(а)' for line_number, line in enumerate(f_obj, 1)]
    print(*useful, f'Всего строк - {len(useful)}', sep='\n  -***-\n')
