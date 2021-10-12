a=(int(input( "masukkan nilai total belanja Rp."))) 
b=(int(input("masukkan uang yang diberikan Rp."))) 
uang = int(input('totalnya :Rp. '))
uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
sisa = uang
print('Input uang {},  Pecahan yang kita butuhkan yaitu: '.format(uang))
for pecahan in uang_pecahan:
    if sisa < pecahan:
        continue
    banyak_pecahan = int(sisa / pecahan)
    sisa = sisa - ( pecahan * banyak_pecahan )
    print('pecahan {} : {}'.format(pecahan, banyak_pecahan)) 
