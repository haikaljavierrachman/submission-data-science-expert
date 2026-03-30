@echo off
echo Mengaktifkan Docker...
docker-compose -f docker-compose.yaml up -d

echo Menunggu database stabil...
timeout /t 5 /nobreak

if exist data_kategorik.csv (
    echo Mengimpor data...
    python insert_data.py
) else (
    echo File data_kategorik.csv tidak ditemukan.
)

echo Selesai! Buka http://localhost:3000
pause