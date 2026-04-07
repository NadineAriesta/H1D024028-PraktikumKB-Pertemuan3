import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

barang_terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'barang_terjual')
permintaan     = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
harga_per_item = ctrl.Antecedent(np.arange(0, 100001, 1), 'harga_per_item')
profit         = ctrl.Antecedent(np.arange(0, 4000001, 100), 'profit')
stok_makanan   = ctrl.Consequent(np.arange(0, 1001, 1), 'stok_makanan')

barang_terjual['rendah'] = fuzz.trapmf(barang_terjual.universe, [0, 0, 0, 40])
barang_terjual['sedang'] = fuzz.trimf(barang_terjual.universe, [30, 50, 70])
barang_terjual['tinggi'] = fuzz.trapmf(barang_terjual.universe, [60, 100, 100, 100])

permintaan['rendah'] = fuzz.trapmf(permintaan.universe, [0, 0, 0, 100])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['tinggi'] = fuzz.trapmf(permintaan.universe, [200, 300, 300, 300])

harga_per_item['murah']  = fuzz.trapmf(harga_per_item.universe, [0, 0, 0, 40000])
harga_per_item['sedang'] = fuzz.trimf(harga_per_item.universe, [30000, 50000, 80000])
harga_per_item['mahal']  = fuzz.trapmf(harga_per_item.universe, [60000, 100000, 100000, 100000])

profit['rendah'] = fuzz.trapmf(profit.universe, [0, 0, 0, 1000000])
profit['sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 2500000])
profit['tinggi'] = fuzz.trapmf(profit.universe, [1500000, 2500000, 4000000, 4000000])

stok_makanan['sedang'] = fuzz.trimf(stok_makanan.universe, [100, 500, 900])
stok_makanan['banyak'] = fuzz.trapmf(stok_makanan.universe, [600, 1000, 1000, 1000])

rule1 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_per_item['murah'] & profit['tinggi'], stok_makanan['banyak'])
rule2 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_per_item['murah'] & profit['sedang'], stok_makanan['sedang'])
rule3 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['sedang'] & harga_per_item['murah'] & profit['sedang'], stok_makanan['sedang'])
rule4 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_per_item['murah'] & profit['sedang'], stok_makanan['sedang'])
rule5 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_per_item['murah'] & profit['tinggi'], stok_makanan['banyak'])
rule6 = ctrl.Rule(barang_terjual['rendah'] & permintaan['rendah'] & harga_per_item['sedang'] & profit['sedang'], stok_makanan['sedang'])

stok_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
simulasi = ctrl.ControlSystemSimulation(stok_ctrl)

simulasi.input['barang_terjual'] = 80
simulasi.input['permintaan']     = 255
simulasi.input['harga_per_item'] = 25000
simulasi.input['profit']         = 3500000

simulasi.compute()

hasil_stok = simulasi.output['stok_makanan']

print("="*40)
print("       UDIN PET SHOP - FUZZY SYSTEM")
print("="*40)
print(f"INPUT:")
print(f"  > Barang Terjual : 80 unit")
print(f"  > Permintaan     : 255 unit")
print(f"  > Harga Per Item : Rp 25.000")
print(f"  > Profit         : Rp 3.500.000")
print("-" * 40)
print(f"OUTPUT:")
print(f"  > Stok Optimal   : {hasil_stok:.2f} unit")
print("="*40)

barang_terjual.view()
plt.title("Membership: Barang Terjual")

permintaan.view()
plt.title("Membership: Permintaan")

harga_per_item.view()
plt.title("Membership: Harga per Item")

profit.view()
plt.title("Membership: Profit")

stok_makanan.view(sim=simulasi)
plt.title("Membership: Stok Makanan (Output)")

plt.show()
