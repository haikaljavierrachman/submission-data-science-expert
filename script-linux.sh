#!/bin/bash

echo "Menjalankan Docker Compose..."
docker-compose -f docker-dompose.yaml up -d

echo "Menunggu PostgreSQL siap (5 detik)..."
sleep 5

# Menjalankan insert data (Pastikan file CSV Anda ada di folder ini)
if [ -f "employee_data.csv" ]; then
    echo "Mengimpor data ke database..."
    python3 insert_to_postgre.py
else
    echo "File employee_data.csv tidak ditemukan. Lewati tahap insert."
fi

echo "Selesai! Akses Metabase di http://localhost:3000"