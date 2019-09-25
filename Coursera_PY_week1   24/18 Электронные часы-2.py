n = int(input())

secunds_total = n % (24 * 60 * 60)

hours = secunds_total // 3600
minut = (secunds_total % 3600) // 60
min_dec = minut // 10
min_min = minut % 10
secunds = secunds_total % 60
sec_dec = secunds // 10
sec_sec = secunds % 10


print(hours, ':', min_dec, min_min, ':', sec_dec, sec_sec, sep='')
