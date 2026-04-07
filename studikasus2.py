import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_sarpras')

kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan_pelayanan')

kejelasan_informasi["tidak_memuaskan"] = fuzz.trapmf(kejelasan_informasi.universe, [0, 0, 60, 75])
kejelasan_informasi["cukup_memuaskan"] = fuzz.trimf(kejelasan_informasi.universe, [60, 75, 90])
kejelasan_informasi["memuaskan"] = fuzz.trapmf(kejelasan_informasi.universe, [75, 90, 100, 100])

kejelasan_persyaratan["tidak_memuaskan"] = fuzz.trapmf(kejelasan_persyaratan.universe, [0, 0, 60, 75])
kejelasan_persyaratan["cukup_memuaskan"] = fuzz.trimf(kejelasan_persyaratan.universe, [60, 75, 90])
kejelasan_persyaratan["memuaskan"] = fuzz.trapmf(kejelasan_persyaratan.universe, [75, 90, 100, 100])

kemampuan_petugas["tidak_memuaskan"] = fuzz.trapmf(kemampuan_petugas.universe, [0, 0, 60, 75])
kemampuan_petugas["cukup_memuaskan"] = fuzz.trimf(kemampuan_petugas.universe, [60, 75, 90])
kemampuan_petugas["memuaskan"] = fuzz.trapmf(kemampuan_petugas.universe, [75, 90, 100, 100])

ketersediaan_sarpras["tidak_memuaskan"] = fuzz.trapmf(ketersediaan_sarpras.universe, [0, 0, 60, 75])
ketersediaan_sarpras["cukup_memuaskan"] = fuzz.trimf(ketersediaan_sarpras.universe, [60, 75, 90])
ketersediaan_sarpras["memuaskan"] = fuzz.trapmf(ketersediaan_sarpras.universe, [75, 90, 100, 100])

kepuasan_pelayanan["tidak_memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [0, 0, 50, 75])
kepuasan_pelayanan["kurang_memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [50, 75, 100, 150])
kepuasan_pelayanan["cukup_memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250, 275])
kepuasan_pelayanan["memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325, 350])
kepuasan_pelayanan["sangat_memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [325, 350, 400, 400])

rule1 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['kurang_memuaskan'])
rule2 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule3 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule4 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule5 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule6 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule7 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule8 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule9 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])

rule10 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule11 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule12 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule13 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule14 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule15 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule16 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule17 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule18 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])

rule19 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule20 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule21 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule22 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule23 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule24 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule25 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule26 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule27 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])

rule28 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule29 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule30 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule31 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule32 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule33 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule34 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule35 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule36 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])

rule37 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule38 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule39 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule40 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule41 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule42 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule43 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule44 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule45 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])

rule46 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule47 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule48 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule49 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule50 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule51 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
rule52 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule53 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
rule54 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])

rule55 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule56 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule57 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule58 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule59 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule60 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule61 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule62 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule63 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])

rule64 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
rule65 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule66 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
rule67 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule68 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule69 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
rule70 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule71 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
rule72 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])

rule73 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule74 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule75 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
rule76 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
rule77 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
rule78 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
rule79 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
rule80 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
rule81 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])

rules_list = [
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
    rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
    rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27,
    rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36,
    rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45,
    rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54,
    rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63,
    rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72,
    rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81
]

kepuasan_ctrl = ctrl.ControlSystem(rules_list)

kepuasan_sim = ctrl.ControlSystemSimulation(kepuasan_ctrl)

kepuasan_sim.input["kejelasan_informasi"] = 80
kepuasan_sim.input["kejelasan_persyaratan"] = 60
kepuasan_sim.input["kemampuan_petugas"] = 50
kepuasan_sim.input["ketersediaan_sarpras"] = 90

kepuasan_sim.compute()

kejelasan_informasi.view()
kejelasan_persyaratan.view()
kemampuan_petugas.view()
ketersediaan_sarpras.view()
kepuasan_pelayanan.view(sim=kepuasan_sim)

hasil = kepuasan_sim.output["kepuasan_pelayanan"]

print("output:", hasil)

import matplotlib.pyplot as plt 
plt.show()
