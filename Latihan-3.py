tahun_awal=int(input("Masukan tahun awal: "))
tahun_akhir=int(input("Masukan tahun akhir: "))#pastikan input tahun_akhir>tahun_awal

while tahun_awal<tahun_akhir:
	tahun_awal=tahun_awal+1
	
	if(tahun_awal%4)==0:
		if(tahun_awal%100)==0:
			if(tahun_awal%400)==0:
				print(str(tahun_awal)+" Tahun Kabisat")
			else:
				print(str(tahun_awal)+" Bukan Tahun kabisat")
		else:
			print(str(tahun_awal)+" Tahun Kabisat")
	else:
		print(str(tahun_awal)+" Bukan Tahun kabisat")