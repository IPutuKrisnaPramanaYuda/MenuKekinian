import os
import pandas as pd
import requests
from datetime import datetime

print(">>> Mengekstrak data Menu Kopi via API...")

# Menembak JSON API Publik
response = requests.get("https://api.sampleapis.com/coffee/hot")
data = response.json()

data_hasil = []
# Mengambil 30 data pertama
for item in data[:30]:
    data_hasil.append({
        "tanggal_update": datetime.now().strftime("%Y-%m-%d"),
        "nama_menu": item.get("title", ""),
        "deskripsi": item.get("description", ""),
        "bahan_dasar": ", ".join(item.get("ingredients", []))
    })

df = pd.DataFrame(data_hasil)
df.to_csv('dataset_menu_kopi.csv', index=False)
print(f"  Berhasil menyimpan {len(df)} baris data ke CSV.")

os.system('git add .')
os.system(f'git commit -m "Update dataset menu kopi: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')
os.system('git push origin main >nul 2>&1')
print("✅ Repo MenuKekinian berhasil di-push!")