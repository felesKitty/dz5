eng_ru_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_44.txt', 'w', encoding='utf-8') as frst_file, \
        open('text_4.txt', encoding='utf-8') as snd_file:
    frst_file.writelines([line.replace(line.split()[0],
                         eng_ru_dic.get(line.split()[0])) for line in snd_file])
