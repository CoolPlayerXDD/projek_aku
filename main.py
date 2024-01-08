meme_dict = {
    "LOL": "Tanggapan terhadap sesuatu yang lucu", 
    "CRINGE": "Sesuatu yang aneh atau memalukan", 
    "ROFL": "Tanggapan terhadap lelucon", 
    "SHEESH": "Sedikit ketidaksetujuan", 
    "CREEPY": "Menakutkan, tidak menyenangkan", 
    "AGGRO": "Untuk menjadi agresif/marah"
    }
word = input("Ketik kata yang tidak kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print("Arti dari", word , "adalah", meme_dict[word])
else:
    print("Kata", word ,"tidak ditemukan dalam kamus meme.")
