#input tiga bilangan
bil1=int(input('Masukan bilangan pertama :'))
bil2=int(input('Masukan bilangan kedua :'))
bil3=int(input('Masukan bilangan ketiga :'))

#hitung digit paling kanan=> dengan modulo 10W
digit_kanan1=bil1%10
digit_kanan2=bil2%10
digit_kanan3=bil3%10

#bandingkan apakah sama semua
if digit_kanan1==digit_kanan2 and digit_kanan2==digit_kanan3:
    print('Semua digit paling kananya sama')
else :
    print('Tidak semuanya sama')
