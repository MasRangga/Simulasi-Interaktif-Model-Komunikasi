Simulasi Interaktif Model Komunikasi dalam Sistem Terdistribusi
Dalam proyek ini, kami mengimplementasikan dua model komunikasi utama dalam sistem terdistribusi, yaitu Model Message Passing dan Model Request-Response.

Model Message Passing
Model Message Passing memungkinkan entitas dalam sistem berinteraksi dengan mengirimkan dan menerima pesan. Dalam simulasi ini, kami menggunakan dua komponen utama: produsen dan konsumen. Produsen menghasilkan data dalam bentuk pesan dan menempatkannya dalam antrian. Sementara itu, konsumen mengambil pesan dari antrian tersebut untuk memproses atau menampilkan informasi yang diterima. Model ini sangat efektif untuk komunikasi antara proses atau thread yang berjalan secara paralel, memberikan fleksibilitas dalam pertukaran informasi antar komponen yang terpisah.

Model Request-Response
Model Request-Response adalah pendekatan komunikasi di mana satu entitas (klien) mengirimkan permintaan (request) kepada entitas lain (server) dan menunggu respon (response) sebelum melanjutkan proses. Dalam simulasi ini, kami menggunakan API Flask untuk mengelola interaksi antara klien dan server. Ketika klien mengirimkan permintaan untuk memulai proses, server memproses permintaan tersebut dan mengirimkan respons yang sesuai. Model ini sangat umum digunakan dalam aplikasi web dan layanan API, karena memberikan cara yang jelas dan terstruktur untuk pertukaran informasi.
