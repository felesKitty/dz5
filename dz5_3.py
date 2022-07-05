def dz_zp():
    zp = {}
    try:
        with open('text_3.txt', 'r', encoding='utf-8') as zp_surname:
            for line in zp_surname:
                zp[line.split()[0]] = float(line.split()[1])
        print('Less than 20000 - ')
        for surname, wage in zp.items():
            if wage < 20000:
                print(surname)
        print(f'Average wage is - {sum(zp.values()) / len(zp)}')
    except:
        print('Critical bookkeeping error')


dz_zp()