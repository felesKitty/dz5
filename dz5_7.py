import json

with open('text_77.json', 'w', encoding='utf=8') as json_f:
    with open('text_7.txt', encoding='utf=8') as txt_f:
        revenue = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in txt_f}
        firms = [v for v in revenue.values() if v > 0]
        res_list = [revenue, {'Average revenue': round(sum(firms) / len(firms))}]

        json.dump(res_list, json_f, ensure_ascii=False)
