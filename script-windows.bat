@echo off
echo Mengaktifkan Docker...
docker-compose -f docker-compose.yaml up -d

echo Menunggu database stabil...
timeout /t 5 /nobreak

if exist employee_data.csv (
    echo Mengimpor data...
    python insert_to_postgre.py
) else (
    echo File employee_data.csv tidak ditemukan.
)

echo Selesai! Buka http://localhost:3000
pause