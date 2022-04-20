import requests


def rok2015():
    url = 'https://date.nager.at/api/v3/publicholidays/2015/PL'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        print(info)
        a = (info[0]['localName'], info[0]['date']),
        b = (info[2]['localName'], info[2]['date']),
        c = (info[4]['localName']), info[4]['date'],
        d = (info[7]['localName'], info[7]['date']),

        tup = (a, b, c, d)
        for i in tup:
            print(i)


rok2015()


def rok2016():
    url = 'https://date.nager.at/api/v3/publicholidays/2016/PL'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        print(info)
        a = (info[0]['localName'], info[0]['date']),
        b = (info[2]['localName'], info[2]['date']),
        c = (info[4]['localName']), info[4]['date'],
        d = (info[7]['localName'], info[7]['date']),

        tup = (a, b, c, d)
        for i in tup:
            print(i)


rok2016()


def rok2017():
    url = 'https://date.nager.at/api/v3/publicholidays/2017/PL'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        print(info)
        a = (info[0]['localName'], info[0]['date']),
        b = (info[2]['localName'], info[2]['date']),
        c = (info[4]['localName']), info[4]['date'],
        d = (info[7]['localName'], info[7]['date']),

        tup = (a, b, c, d)
        for i in tup:
            print(i)


rok2017()


def rok2018():
    url = 'https://date.nager.at/api/v3/publicholidays/2018/PL'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        print(info)
        a = (info[0]['localName'], info[0]['date']),
        b = (info[2]['localName'], info[2]['date']),
        c = (info[4]['localName']), info[4]['date'],
        d = (info[7]['localName'], info[7]['date']),

        tup = (a, b, c, d)
        for i in tup:
            print(i)


rok2018()


def rok2019():
    url = 'https://date.nager.at/api/v3/publicholidays/2019/PL'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        print(info)
        a = (info[0]['localName'], info[0]['date']),
        b = (info[2]['localName'], info[2]['date']),
        c = (info[4]['localName']), info[4]['date'],
        d = (info[7]['localName'], info[7]['date']),
        tup = (a, b, c, d)
        for i in tup:
            print(i)


rok2019()


def rok2020():
    url = 'https://date.nager.at/api/v3/publicholidays/2020/PL'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        print(info)
        a = (info[0]['localName'], info[0]['date']),
        b = (info[2]['localName'], info[2]['date']),
        c = (info[4]['localName']), info[4]['date'],
        d = (info[7]['localName'], info[7]['date']),

        tup = (a, b, c, d)
        for i in tup:
            print(i)


rok2020()


def rok2021():
    url = 'https://date.nager.at/api/v3/publicholidays/2021/PL'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        print(info)
        a = (info[0]['localName'], info[0]['date']),
        b = (info[2]['localName'], info[2]['date']),
        c = (info[4]['localName']), info[4]['date'],
        d = (info[7]['localName'], info[7]['date']),

        tup = (a, b, c, d)
        for i in tup:
            print(i)


rok2021()


def rok2022():
    url = 'https://date.nager.at/api/v3/publicholidays/2022/PL'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        print(info)
        a = (info[0]['localName'], info[0]['date']),
        b = (info[2]['localName'], info[2]['date']),
        c = (info[4]['localName']), info[4]['date'],
        d = (info[7]['localName'], info[7]['date']),

        tup = (a, b, c, d)
        for i in tup:
            print(i)
        for i in info:
            print(i)


rok2022()
