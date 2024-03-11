uang_awal = int(input("masukan uang anda : "))
pengeluaran = int(input("masukan pengeluaran anda : "))

if pengeluaran > 60000:
    pengeluaran -= 10000

total = pengeluaran 
kembalian = uang_awal - pengeluaran

print("total belanjaan anda rp.%i dan kembalian rp.%i" %(total,kembalian))