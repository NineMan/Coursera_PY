# def zamena(stroka, simbol):
#     index = stroka.find(simbol)
#     while index != -1:
#         stroka = stroka[:index] + stroka[index + 1:]
#         index = stroka.find(simbol)
#     return stroka
def transform(stroka):
    for j in ['-', '(', ')']:
        stroka = stroka.replace(j, '')
    if stroka[0:2] == '+7':
        stroka = stroka.replace('+7', '8', 1)
    if len(stroka) == 7:
        stroka = '8495' + stroka
    return stroka


    # for j in ['-', '(', ')']:
        # stroka = zamena(stroka, j)
    # if stroka[0:2] == '+7':
    #     stroka = '8' + stroka[2:]
    # if len(stroka) == 7:
    #     stroka = '8495' + stroka
    # return stroka


searchNumber = transform(input())
for _ in range(3):
    number = transform(input())
    if number == searchNumber:
        print('YES')
    else:
        print('NO')
