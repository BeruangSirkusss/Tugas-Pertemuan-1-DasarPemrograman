gaji_bulanan = int(input("gaji bulanan : "))
masuk_kerja = int(input("berapa hari anda masuk kerja :"))
uang_transport = 10000 * masuk_kerja
uang_makan = 50000 * masuk_kerja
if uang_lembur < 2:
    total_lembur = uang_lembur *100000
else :
    total_lembur = 2 *100000 + (uang_lembur - 2) * 150000
honor = gaji_bulanan + uang_transport + uang_makan + total_lembur
print  ("uang honor yang didapat Rp.%i"%honor)       

    
    

