import pandas as pd
from numbers import Number
import json
import os
# digunakan agar schema warna dapat di tampilkan di comand promp windows 10
os.system("")
# load json file yang berisi factor reagent
with open("D:/Git Repositori/Belajar-Python/reagent factor.json") as f:
    factor = json.load(f)
# merubah jason file yang berisi factor reagent ke dalam data frame
table_factor = pd.DataFrame(factor)
# scema warna yang di gunakan untuk di tampilkan di comand promp
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# variable untuk menyimpan hasil analisa
hasil_pengecekan = {}
# variable untuk menyimpan
keys_alkaline = 0
keys_acid = 0
keys_chromating = 0
keys_nickle_plating = 0
keys_tin_plating = 0
keys_cyanid_zinc = 0
# kelas untuk menampilkan hasil perhitungan dan menambahkan hasil analisa pada dictionary hasil_pengecekan
class Rumus:
    def __init__(self, hasil_pertama=0.0, hasil_kedua=0.0, hasil_ketiga=0.0, hasil_keempat=0.0):
        self.hasil_pertama = hasil_pertama
        self.hasil_kedua = hasil_kedua
        self.hasil_ketiga = hasil_ketiga
        self.hasil_keempat = hasil_keempat
    def alkaline_zinc(self):
        zinc = self.hasil_pertama * 3.27 * table_factor.Factor[3]
        naoh = self.hasil_kedua * 8 * table_factor.Factor[1]
        carbonate = self.hasil_ketiga * 10.6 * table_factor.Factor[1]
        print(bcolors.OKGREEN + '\nZN = {:.2f} g/l \nNaOH = {:.2f} g/l \nSodium Carbonate = {:.2f} g/l '.format(zinc, naoh, carbonate) + bcolors.ENDC)
        global keys_alkaline
        # merubah variable keys_alkaline jika key yang akan di tambahkan ke dictionary hasil_pengecekan sudah ada
        if ('Alkaline ' + str(keys_alkaline)) not in hasil_pengecekan:
            hasil_pengecekan['Alkaline ' + str(keys_alkaline)] = [{'Zinc':  zinc, 'Sodium Hydroxide': naoh, 'Sodium Carbonate': carbonate}]
        else:
            keys_alkaline += 1
            hasil_pengecekan['Alkaline ' + str(keys_alkaline)] = [{'Zinc':  zinc, 'Sodium Hydroxide': naoh, 'Sodium Carbonate': carbonate}]
    def acid_zinc(self):
        zinc = self.hasil_pertama * 3.27 * table_factor.Factor[3]
        zinc_cl = zinc * 2.09
        cl = self.hasil_kedua * 14.2 * table_factor.Factor[4]
        amonium = (cl * 1.5) - (zinc_cl * 0.7846)
        potasium = (cl * 2.0986) - (zinc_cl * 1.0925)
        print(bcolors.OKGREEN + '\nZn = {:.2f} g/l \nZinc Chlorite = {:.2f} g/l \nChlorite = {:.2f} g/l \nAmmonium Chlorite = {:.2f} g/l \nPottasium Chlorite = {:.2f} g/l '.format(
            zinc, zinc_cl, cl, amonium, potasium) + bcolors.ENDC)
        global keys_acid
        # merubah variable keys_acid jika key yang akan di tambahkan ke dictionary hasil_pengecekan sudah ada
        if ('Acid Zinc ' + str(keys_acid)) not in hasil_pengecekan:
            hasil_pengecekan['Acid Zinc ' + str(keys_acid)] = [{'Zinc':  zinc, 'Zinc Chlorite': zinc_cl, 'Chlorite': cl, 'Ammonium Chlorite': amonium, 'Potasium Chlorite': potasium, 'Boric Acid': 2}]
        else:
            keys_acid += 1
            hasil_pengecekan['Acid Zinc ' + str(keys_acid)] = [{'Zinc':  zinc, 'Zinc Chlorite': zinc_cl,'Chlorite': cl, 'Ammonium Chlorite': amonium, 'Potasium Chlorite': potasium, 'Boric Acid': 2}]
    def chromating(self):
        zn = self.hasil_pertama * 3.27 * table_factor.Factor[0]
        cr = self.hasil_kedua * 0.8667 * table_factor.Factor[2]
        print(bcolors.OKGREEN +
            '\nZn = {:.2f} g/l \nCr = {:.2f} g/l '.format(zn, cr) + bcolors.ENDC)
        global keys_chromating
        # merubah variable keys_chromating jika key yang akan di tambahkan ke dictionary hasil_pengecekan sudah ada
        if ('Chromating ' + str(keys_chromating)) not in hasil_pengecekan:
            hasil_pengecekan['Chromating ' + str(keys_chromating)] = [{'Zinc':  zn, 'Chrome Trivalent': cr}]
        else:
            keys_chromating += 1
            hasil_pengecekan['Chromating ' + str(keys_chromating)] = [{'Zinc':  zn, 'Zinc Chlorite': cr}]
    def nickle_plating(self):
        ni = self.hasil_pertama * 5.87 * table_factor.Factor[0]
        cl = self.hasil_kedua * 3.75 * table_factor.Factor[4]
        hbo3 = self.hasil_ketiga * 6.18 * table_factor.Factor[1]
        nicl = cl * 3.35
        niso4 = (ni * 4.48) - (nicl * 1.105)
        print(bcolors.OKGREEN + '\nNickle Content = {:.2f} g/l \nChlorite = {:.2f} g/l \nNickle Chlorite = {:.2f} g/l \nNickle Sulfate = {:.2f} g/l \nBoric Acid = {:.2f} g/l '.format(ni, cl, nicl, niso4, hbo3) + bcolors.ENDC)
        global keys_nickle_plating
        # merubah variable keys_nickle_plating jika key yang akan di tambahkan ke dictionary hasil_pengecekan sudah ada
        if ('Nickle Plating ' + str(keys_nickle_plating)) not in hasil_pengecekan:
            hasil_pengecekan['Nickle Plating ' + str(keys_nickle_plating)] = [{'Nickle Content': ni, 'Nickle Chlorite': nicl, ' Nickle Sulfate': niso4, 'Chlorite': cl, 'Boric Acid': hbo3}]
        else:
            keys_nickle_plating += 1
            hasil_pengecekan['Nickle Plating ' + str(keys_nickle_plating)] = [{'Nickle Content': ni, 'Nickle Chlorite': nicl, ' Nickle Sulfate': niso4, 'Chlorite': cl, 'Boric Acid': hbo3}]
    def tin_plating(self):
        sn = self.hasil_pertama * 1.19
        snso4 = sn * 2.15
        sulfat_gram = self.hasil_kedua * 9.8 * table_factor.Factor[1]
        sulfat_ml = sulfat_gram / 1.84
        print(bcolors.OKGREEN + '\nTin Content = {:.2f} g/l \nTin Sulfat {:.2f} g/l \nAsam Sulfat = {:.2f} g/l \nAsam Sulfte = {:.2f} ml/l '.format(sn, snso4, sulfat_gram, sulfat_ml) + bcolors.ENDC)
        global keys_tin_plating
        # merubah variable keys_tin_plating jika key yang akan di tambahkan ke dictionary hasil_pengecekan sudah ada
        if ('Tin Plating ' + str(keys_tin_plating)) not in hasil_pengecekan:
            hasil_pengecekan['Tin Plating ' + str(keys_tin_plating)] = [{'Tin': sn, 'Tin Sulfat': snso4, ' Asam Sulfat (gr)': sulfat_gram, 'Asam Sulfat (ml)': sulfat_ml}]
        else:
            keys_tin_plating += 1
            hasil_pengecekan['Tin Plating ' + str(keys_tin_plating)] = [{'Tin': sn, 'Tin Sulfat': snso4, ' Asam Sulfat (gr)': sulfat_gram, 'Asam Sulfat (ml)': sulfat_ml}]
    def cyanid_zinc(self):
        zn = self.hasil_pertama * 3.27 * table_factor.Factor[0]
        nacn = self.hasil_kedua * 4.9 * table_factor.Factor[2]
        naoh = self.hasil_ketiga * 8 * table_factor.Factor[1]
        carbonat = self.hasil_keempat * 10.6 * table_factor.Factor[0]
        print(bcolors.OKGREEN + '\nzn = {:.2f} g/l \nNaCn = {:.2f} g/l \nNaOH = {:.2f} g/l \nSodium Carbonat = {:.2f} g/l '.format(zn, nacn, naoh, carbonat) + bcolors.ENDC)
        global keys_cyanid_zinc
        # merubah variable keys_cyanid_zinc jika key yang akan di tambahkan ke dictionary hasil_pengecekan sudah ada
        if ('Cyanid Zinc ' + str(keys_cyanid_zinc)) not in hasil_pengecekan:
            hasil_pengecekan['Cyanid Zinc ' + str(keys_cyanid_zinc)] = [{'Zinc': zn, 'Sodium Cyanide': nacn, ' Sodium Hydroxide': naoh, 'Sodium Carbonate': carbonat}]
        else:
            keys_cyanid_zinc += 1
            hasil_pengecekan['Cyanid Zinc ' + str(keys_cyanid_zinc)] = [{'Zinc': zn, 'Sodium Cyanide': nacn, ' Sodium Hydroxide': naoh, 'Sodium Carbonate': carbonat}]
    def degreasing(self):
        pn_36 = self.hasil_pertama * 6.76 * table_factor.Factor[0]
        dasshi_39 = self.hasil_pertama * 7.66 * table_factor.Factor[0]
        ds_13a = 1.61 * (12.42 - (self.hasil_pertama - table_factor.Factor[0]))
        ds_13b = ds_13a / 4
        print(bcolors.OKGREEN + '\nPn 36 = {:.2f} g/l \nDasshi 39 = {:.2f} g/l \nDs 13 A = {:.2f} g/l \nDs 13 B = {:.2f} g/l '.format(
            pn_36, dasshi_39, ds_13a, ds_13b) + bcolors.ENDC)

print(bcolors.FAIL + '''
___  ___     _     _____          _        ______         _                   
|  \/  |    | |   |_   _|        | |       | ___ \       | |                  
| .  . | ___| |_    | | _ __   __| | ___   | |_/ /__ _ __| | ____ _ ___  __ _ 
| |\/| |/ _ \ __|   | || '_ \ / _` |/ _ \  |  __/ _ \ '__| |/ / _` / __|/ _` |
| |  | |  __/ |_   _| || | | | (_| | (_) | | | |  __/ |  |   < (_| \__ \ (_| |
\_|  |_/\___|\__|  \___/_| |_|\__,_|\___/  \_|  \___|_|  |_|\_\__,_|___/\__,_|
''' + bcolors.ENDC)
print('****   Perhitungan PT. Metindo Perkasa   ****')
print('code  Nama')
print('''1.    Perhitungan Alkaline Zinc         11.     
2.    Perhitungan Acid Zinc             12.     
3.    Perhitungan Chromating            13.
4.    Perhitungan Nickle Plating        14.     
5.    Perhitungan Tin Plating           15.     
6.    Perhitungan Cyanid Zinc           16.     Perhitungan Degreasing
7.                                      17.     Print Hasil Pengecekan
8.                                      18.     Print Factor Reagent
9.                                      19.     Rubah Factor Reagent
10.                                     20.     Exit
''')
print('Masukan Kode perhitungan.....')

def hasil_perhitungan(codex):
    global hasil_pengecekan
    hasil_pengecekan_sort = dict(sorted(hasil_pengecekan.items(), key=lambda kv: kv[0]))
    global code
    if codex == 1:
        print('Perhitungan alkaline Zinc')
        hasil_zinc = float(input('Masukan Hasil Titrasi EDTA 0.1 M:   '))
        hasil_naoh = float(input('Masukan Hasil Titrasi Hcl 1 N pertama:   '))
        hasil_carbonate = float(input('Masukan Hasil Titrasi Hcl 1 N kedua:   '))
        alkaline = Rumus(hasil_zinc, hasil_naoh, hasil_carbonate)
        alkaline.alkaline_zinc()
    elif codex == 2:
        print('Perhitungan Acid Zinc')
        hasil_zinc = float(input('Masukan Hasil Titrasi EDTA 0.1M:   '))
        hasil_chlorite = float(input('Masukan Hasil Titrasi AgNO3 0.1 N:   '))
        hasil_boric = float(input('Masukan Hasil Titrasi NaOH 1 N:   '))
        acid = Rumus(hasil_zinc, hasil_chlorite, hasil_boric)
        acid.acid_zinc()
    elif codex == 3:
        print('perhitungan Chromating')
        hasil_zinc_cr = float(input('Masukan Hasil Titrasi EDTA 0.1 M:   '))
        hasil_cr = float(input('Masukan Hasil Titrasi Na2SO4 0.1 N:   '))
        chromat = Rumus(hasil_zinc_cr, hasil_cr)
        chromat.chromating()
    elif codex == 4:
        print('Perhitungan Nickle Plating')
        ni = float(input('Masukan Hasil Titrasi EDTA 0.1 M:   '))
        cl = float(input('Masukan Hasil Titrasi AgNO3 0.1 N:   '))
        boric = float(input('Masukan Hasil Titrasi NaOH 0.1 N:   '))
        nickle = Rumus(ni, cl, boric)
        nickle.nickle_plating()
    elif codex == 5:
        print('Perhitungan Tin Plating')
        sn = float(input('Masukan Hasil Titrasi I2 0.1 N:  '))
        h2so4 = float(input('Masukan Hasil Titrasi NaOH 1N:   '))
        tin = Rumus(sn, h2so4)
        tin.tin_plating()
    elif codex == 6:
        zn = float(input('Masukan Hasil Titrasi EDTA 0.1 M:  '))
        cn = float(input('Masukan Hasil Titrasi AgNO3 0.1 N:  '))
        naoh = float(input('Masukan Hasil Titrasi HCL 1 N pertama:  '))
        carbonat = float(input('Masukan Hasil Titrasi HCl 1 N kedua:   '))
        cyanide = Rumus(zn, cn, naoh, carbonat)
        cyanide.cyanid_zinc()
    elif codex == 16:
        print('Perhitungan Degrasing')
        hasil_degreasing = float(input('Masukan Hasil Titrasi HCl 1 N:   '))
        degreas = Rumus(hasil_degreasing)
        degreas.degreasing()
    elif codex == 17:
        space = ''
        for i in hasil_pengecekan_sort:
            if 'Alkaline' in i:
                for x in hasil_pengecekan_sort[i]:
                    result = []
                    test = []
                    text = i
                    for y in x:
                        test.append(y)
                        result.append(x[y])
                    print(space.center(85, '-'))
                    print('|', space.center(22, ' '), '|', test[0].center(22, ' '), '|', '{:.3f}'.format(result[0]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', str(text).center(22, ' '), '|', test[1].center(22, ' '), '|', '{:.3f}'.format(result[1]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[2].center(22, ' '), '|', '{:.3f}'.format(result[2]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
            elif 'Acid Zinc' in i:
                for x in hasil_pengecekan_sort[i]:
                    result = []
                    test = []
                    text = i
                    for y in x:
                        test.append(y)
                        result.append(x[y])
                    print(space.center(85, '-'))
                    print('|', space.center(22, ' '), '|', test[0].center(22, ' '), '|', '{:.3f}'.format(result[0]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[1].center(22, ' '), '|', '{:.3f}'.format(result[1]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', str(i).center(22, ' '), '|', test[2].center(22, ' '), '|', '{:.3f}'.format(result[2]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[3].center(22, ' '), '|', '{:.3f}'.format(result[3]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[4].center(22, ' '), '|', '{:.3f}'.format(result[4]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
            elif 'Chromating' in i:
                for x in hasil_pengecekan_sort[i]:
                    result = []
                    test = []
                    text = i
                    for y in x:
                        test.append(y)
                        result.append(x[y])
                    print(space.center(85, '-'))
                    print('|', str(text).center(22, ' '), '|', test[0].center(22, ' '), '|', '{:.3f}'.format(result[0]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[1].center(22, ' '), '|', '{:.3f}'.format(result[1]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
            elif 'Nickle Plating' in i:
                for x in hasil_pengecekan_sort[i]:
                    result = []
                    test = []
                    text = i
                    for y in x:
                        test.append(y)
                        result.append(x[y])
                    print(space.center(85, '-'))
                    print('|', space.center(22, ' '), '|', test[0].center(22, ' '), '|', '{:.3f}'.format(result[0]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[1].center(22, ' '), '|', '{:.3f}'.format(result[1]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', str(i).center(22, ' '), '|', test[2].center(22, ' '), '|', '{:.3f}'.format(result[2]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[3].center(22, ' '), '|', '{:.3f}'.format(result[3]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[4].center(22, ' '), '|', '{:.3f}'.format(result[4]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
            elif 'Tin Plating' in i:
                for x in hasil_pengecekan_sort[i]:
                    result = []
                    test = []
                    text = i
                    for y in x:
                        test.append(y)
                        result.append(x[y])
                    print(space.center(85, '-'))
                    print('|', space.center(22, ' '), '|', test[0].center(22, ' '), '|', '{:.3f}'.format(result[0]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', str(i).center(22, ' '), '|', test[1].center(22, ' '), '|', '{:.3f}'.format(result[1]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[2].center(22, ' '), '|', '{:.3f}'.format(result[2]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[3].center(22, ' '), '|', '{:.3f}'.format(result[3]).center(17, ' '), '|', 'ml/l'.center(11, ' '), '|')
            elif 'Cyanid Zinc' in i:
                for x in hasil_pengecekan_sort[i]:
                    result = []
                    test = []
                    text = i
                    for y in x:
                        test.append(y)
                        result.append(x[y])
                    print(space.center(85, '-'))
                    print('|', space.center(22, ' '), '|', test[0].center(22, ' '), '|', '{:.3f}'.format(result[0]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', str(i).center(22, ' '), '|', test[1].center(22, ' '), '|', '{:.3f}'.format(result[1]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[2].center(22, ' '), '|', '{:.3f}'.format(result[2]).center(17, ' '), '|', 'g/l'.center(11, ' '), '|')
                    print('|', space.center(22, ' '), space.center(60, '-'))
                    print('|', space.center(22, ' '), '|', test[3].center(22, ' '), '|', '{:.3f}'.format(result[3]).center(17, ' '), '|', 'ml/l'.center(11, ' '), '|')
        # untuk menampilakan garis table terakhir
        if len(hasil_pengecekan) == len(hasil_pengecekan_sort):
            print(space.center(85, '-'))
    elif codex == 18:
        print(bcolors.OKGREEN, table_factor, bcolors.ENDC, '\n')
    # looping jika code yang di input bukan integer
    while True:
        try:
            code = int(input('\nperhitungan selanjutnya \nMasukan code perhitungan:  '))
            if isinstance(code, int):
                break
        except:
            pass
        print('\nCode Salah, Masukan Code Yang Valid')
def rubah_factor():
    global code
    while True:
        try:
            code_factor = int(input('Masukan Code reagent yang ingin di rubah factornya:  '))
            if isinstance(code_factor, int):
                break
        except:
            pass
        print('\nCode Salah, Masukan Code Yang Valid')
    if code_factor == 1:
        factor_baru = float(input('Masukan Factor Hcl 1N yang baru:  '))
        factor["Factor"][0] = factor_baru
    elif code_factor == 2:
        factor_baru = float(input('Masukan Factor NaOH 1N yang baru:  '))
        factor["Factor"][1] = factor_baru
    elif code_factor == 3:
        factor_baru = float(input('Masukan Factor Na2SO3 0.1 N yang baru:  '))
        factor["Factor"][2] = factor_baru
    elif code_factor == 4:
        factor_baru = float(input('Masukan Factor EDTA 0.1M yang baru:  '))
        factor["Factor"][3] = factor_baru
    elif code_factor == 5:
        factor_baru = float(input('Masukan Factor AgNo3 0.1N yang baru:  '))
        factor["Factor"][4] = factor_baru
    elif code_factor == 6:
        print(bcolors.OKGREEN, table_factor, bcolors.ENDC, '\n')
    elif code_factor == 7:
        code = int(input('Masukan Code Perhitungan:  '))
        hasil_perhitungan(code)
    # dump hasil perubahan dictionary ke dalam file json
    with open('reagent factor.json', 'w') as f:
        json.dump(factor, f)

while True:
    try:
        code = int(input())
        if isinstance(code, int):
            break
    except:
        pass
    print('\nCode Salah, Masukan Code Yang Valid')

while code > 0 and code <= 18:
    hasil_perhitungan(code)
while code == 19:
    print('''
Code  Reagent
1.    Hcl 1 N
2.    NaOH 1 N
3.    Na2SO3 0.1 N
4.    EDTA 0.1M
5.    AgNo3 0.1N
6.    print factor reagent
7.    selesai
        ''')
    rubah_factor()
