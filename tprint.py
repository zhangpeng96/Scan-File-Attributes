import datetime

def tprint(*param):
    data = datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S.%f')
    data += '> '
    for c in param:
        data += str(c) + ' '
    print(data)
