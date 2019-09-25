numPupil = int(input())
listPupilLang = []
for i in range(numPupil):
    numberLang = int(input())
    n = 0
    setLang = set()
    while n < numberLang:
        lang = input()
        setLang.add(lang)
        n += 1
    listPupilLang.append(setLang)
# print(listPupilLang)
# listPupilLang = [{'ru', 'en', 'jp'}, {'ru', 'en'}, {'en'}]

setAllLang = set()
setCommonLang = listPupilLang[0]
for i in listPupilLang:
    setAllLang = setAllLang | i
    setCommonLang = setCommonLang & i

print(len(setCommonLang))
for lang in setCommonLang:
    print(lang)

print(len(setAllLang))
for lang in setAllLang:
    print(lang)
