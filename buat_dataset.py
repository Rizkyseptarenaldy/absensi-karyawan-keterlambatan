import pandas as pd
import numpy as np

np.random.seed(42)
n = 300
jam_masuk_resmi = 8.00

df = pd.DataFrame({
    "Nama": [f"Karyawan {i+1}" for i in range(n)],
    "Usia": np.random.randint(20, 50, n),
    "Jenis Kelamin": np.random.choice(["Laki-laki", "Perempuan"], n),
    "Status Perkawinan": np.random.choice(["Menikah", "Belum Menikah"], n),
    "Jarak ke Kantor (km)": np.round(np.random.uniform(1, 30, n), 1),
    "Rata-rata Jam Tidur": np.round(np.random.normal(6.5, 1, n), 1),
    "Waktu Berangkat (jam)": np.round(np.random.normal(6.8, 0.5, n), 2),
    "Waktu Masuk (jam)": np.round(np.random.normal(8.05, 0.15, n), 2),
    "Transportasi": np.random.choice(["Motor", "Mobil", "Transportasi Umum", "Jalan Kaki"], n),
    "Cuaca": np.random.choice(["Cerah", "Hujan", "Berawan"], n)
})

df["Terlambat (menit)"] = np.maximum((df["Waktu Masuk (jam)"] - jam_masuk_resmi) * 60, 0).round(0)
df["Status Keterlambatan"] = df["Terlambat (menit)"].apply(lambda x: "Ya" if x > 0 else "Tidak")

df.to_excel("dataset_absensi_dengan_jam.xlsx", index=False)
print("✅ File berhasil disimpan sebagai 'dataset_absensi_dengan_jam.xlsx'")
