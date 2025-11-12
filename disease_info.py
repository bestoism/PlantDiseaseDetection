# File: disease_info.py

disease_details = {
    'Tomato___Bacterial_spot': {
        'nama': 'Bercak Bakteri pada Tomat',
        'deskripsi': 'Penyakit yang disebabkan oleh bakteri Xanthomonas, menyerang daun, batang, dan buah. Menyebar cepat dalam kondisi hangat dan basah.',
        'gejala': [
            'Bercak kecil, gelap, dan basah pada daun.',
            'Bercak seringkali memiliki lingkaran kuning di sekelilingnya.',
            'Pada buah, bercak sedikit timbul dan kasar seperti kudis.'
        ],
        'penanganan': [
            'Gunakan benih yang bebas penyakit.',
            'Pastikan sirkulasi udara yang baik, jangan tanam terlalu rapat.',
            'Hindari penyiraman dari atas daun, siram di bagian akar.',
            'Buang dan musnahkan tanaman yang terinfeksi parah.'
        ]
    },
    'Tomato___Late_blight': {
        'nama': 'Hawar Daun pada Tomat',
        'deskripsi': 'Disebabkan oleh jamur Phytophthora infestans. Ini adalah penyakit yang sangat merusak dan dapat menghancurkan seluruh tanaman dengan cepat.',
        'gejala': [
            'Bercak besar, berwarna hijau keabu-abuan pada daun, seringkali tampak basah.',
            'Ada jamur putih yang tumbuh di bagian bawah daun saat lembab.',
            'Bercak pada buah besar, berwarna coklat, dan keras.'
        ],
        'penanganan': [
            'Jaga agar daun tetap kering.',
            'Gunakan fungisida preventif, terutama saat cuaca lembab.',
            'Lakukan rotasi tanaman, jangan menanam tomat/kentang di tempat yang sama setiap tahun.'
        ]
    },
    'Pepper__bell___healthy': {
        'nama': 'Paprika Sehat',
        'deskripsi': 'Tanaman tidak menunjukkan tanda-tanda penyakit. Daun tampak hijau subur dan utuh.',
        'gejala': ['Tidak ada bercak, perubahan warna, atau kelainan bentuk pada daun.'],
        'penanganan': ['Lanjutkan praktik perawatan yang baik, seperti penyiraman teratur, pemupukan seimbang, dan pemantauan rutin.']
    },
    'Potato___healthy': {
        'nama': 'Kentang Sehat',
        'deskripsi': 'Tanaman kentang dalam kondisi optimal tanpa infeksi.',
        'gejala': ['Daun berwarna hijau merata, tidak ada lubang atau bercak abnormal.'],
        'penanganan': ['Jaga kebersihan area tanam dan lanjutkan pemantauan untuk deteksi dini hama atau penyakit.']
    },
    'Pepper__bell___Bacterial_spot': {
        'nama': 'Bercak Bakteri pada Paprika',
        'deskripsi': 'Penyakit umum yang disebabkan oleh bakteri Xanthomonas campestris, sering terjadi dalam kondisi cuaca yang hangat dan basah.',
        'gejala': [
            'Bercak kecil basah pada daun yang kemudian membesar dan menjadi gelap/kehitaman.',
            'Pusat bercak seringkali tampak kering dan retak.',
            'Bercak bisa juga muncul di batang dan buah.'
        ],
        'penanganan': [
            'Hindari menyiram daun, fokus pada akar.',
            'Beli benih dari sumber terpercaya yang bebas penyakit.',
            'Lakukan rotasi tanaman dan jangan menanam paprika di lokasi yang sama berturut-turut.'
        ]
    },
    # --- ANDA BISA MENAMBAHKAN 11 KELAS LAINNYA DI SINI DENGAN FORMAT YANG SAMA ---
    'default': {
        'nama': 'Informasi Tidak Ditemukan',
        'deskripsi': 'Informasi detail untuk penyakit ini belum ditambahkan ke dalam sistem.',
        'gejala': ['-'],
        'penanganan': ['-']
    }
}