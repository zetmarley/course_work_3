import json

"""Ниже пишем функцию, возвращающая и переводящая текст в норм формат"""
def transactions():
    with open("operations.json", 'r') as f:
        return json.loads(f.read())

"""Ниже функция возвращает параметры последних 5-и транзакций"""
def last_five():
    topfive_id = []
    result = []
    mylist = {}

    """Ниже чистим базу от некорректных данных"""
    for operation in transactions():
        if operation == {}:
            continue
        if 'from' not in operation.keys():
            continue
        if operation['state'] == 'EXECUTED':
            mylist[f'{operation['date'][:10]}'] = operation['id']

    """Думал ниже подключить datetime для сортировки по времени"""
    """Однако попробовав такой метод сортировки"""
    """Получил нужный результат"""
    mylist = sorted(mylist.items(), reverse=True)[:5]

    """Ниже добавляем id последних 5-и транзакций"""
    for i in mylist:
        topfive_id.append(i[1])

    """Тут мы находим id нужных транзакций во всей базе"""
    """И добавляем всю информацию по ним в наш список"""
    for id in topfive_id:
        for operation in transactions():
            if operation == {}:
                continue
            if operation['id'] == id:
                result.append(operation)
    return result

"""Ниже функция возвращает информацию"""
"""О пяти последних транзакций в обработаном виде"""
def last_five_result():
    text = ''
    count = 0
    hiden_from_info = ''
    for operation in last_five():
        from_info = operation['from'].split(' ')[-1]
        for i in from_info:
            count += 1
            if count == 4:
                hiden_from_info += f'{i} '
                count = 0
                continue
            hiden_from_info += f'{i}'
        hiden_from_info = hiden_from_info[:-1]
        hiden_from_info = hiden_from_info[::-1].replace(hiden_from_info[::-1][5:9], "****")
        hiden_from_info = hiden_from_info.replace(hiden_from_info[10:12], "**")
        hiden_from_info = hiden_from_info[::-1]
        hiden_from_info = " ".join((operation['from'].split(' ')[:-1])), hiden_from_info

        toinfo = operation['to']
        toinfo = toinfo.split(' ')[0] + ' ' + toinfo.split(' ')[-1].replace(toinfo.split(' ')[-1][:-4], '**')
        text += f'{operation['date'][8:10]}.{operation['date'][5:7]}.{operation['date'][:4]} {operation['description']}\n{' '.join(hiden_from_info)} -> {toinfo}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n\n'
        hiden_from_info = ''
    return text