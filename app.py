import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image # Pillow library untuk memproses gambar
from disease_info import disease_details

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Deteksi Penyakit Tanaman",
    page_icon="🌿",
    layout="wide"
)

# --- Fungsi untuk Memuat Model (dengan Caching) ---
# Decorator @st.cache_resource memastikan model hanya dimuat sekali
@st.cache_resource
def load_model():
    model_path = 'models/plant_disease_model.h5'
    model = tf.keras.models.load_model(model_path)
    return model

# Panggil fungsi untuk memuat model
model = load_model()

# --- Definisikan Nama Kelas ---
# Penting: Urutan harus sama dengan urutan yang dipelajari oleh model.
# Biasanya, ini adalah urutan alfabet dari nama folder.
# Mari kita buat list ini berdasarkan output yang kita lihat sebelumnya.
class_names = [
    'Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites_Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# --- Fungsi Prediksi ---
def predict(image):
    """Fungsi untuk membuat prediksi pada gambar yang diunggah."""
    # Ukuran gambar yang diharapkan oleh model
    img_height = 224
    img_width = 224
    
    # Preprocessing gambar
    # 1. Ubah ukuran gambar
    image = image.resize((img_height, img_width))
    # 2. Konversi gambar ke numpy array
    img_array = np.array(image)
    # 3. Tambahkan dimensi batch
    img_array = np.expand_dims(img_array, axis=0)
    # 4. Normalisasi gambar
    img_array = img_array / 255.0

    # Lakukan prediksi
    predictions = model.predict(img_array)
    
    # Dapatkan kelas dengan probabilitas tertinggi
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_name = class_names[predicted_class_index]
    confidence = np.max(predictions[0])
    
    return predicted_class_name, confidence

# --- Antarmuka Aplikasi Web (UI) ---

st.title("🌿 Deteksi Penyakit Daun Tanaman")
st.write("Unggah gambar daun tanaman Anda dan biarkan AI kami menganalisisnya.")

# Komponen untuk mengunggah file
uploaded_file = st.file_uploader("Pilih gambar daun...", type=["jpg", "jpeg", "png"])

# Cek apakah pengguna sudah mengunggah file
if uploaded_file is not None:
    # Buka dan tampilkan gambar yang diunggah
    image = Image.open(uploaded_file)
    
    # Buat dua kolom: satu untuk gambar, satu untuk hasil
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption='Gambar yang diunggah.', use_column_width=True)
    
    # Saat tombol ditekan, jalankan prediksi
    if st.button("🔍 Analisis Gambar"):
        with st.spinner('Model sedang bekerja...'):
            # Panggil fungsi prediksi
            predicted_class, confidence = predict(image)

            # Tampilkan hasil di kolom kedua
            # Ganti blok 'with col2:' yang lama dengan yang ini
            
       # Ganti seluruh blok 'with col2:' yang lama dengan yang ini
        with col2:
            # --- Logika Ambang Batas Kepercayaan ---
            CONFIDENCE_THRESHOLD = 0.70  # 70%

            if confidence > CONFIDENCE_THRESHOLD:
                st.success("Analisis Selesai!")
                st.markdown(f"### **Prediksi:** `{predicted_class}`")
                st.markdown(f"### **Tingkat Kepercayaan:** `{confidence:.2%}`")
                st.write("---")

                # Ambil dan tampilkan informasi detail
                info = disease_details.get(predicted_class, disease_details['default'])
                
                st.markdown(f"#### Nama Penyakit: {info['nama']}")
                st.markdown("##### Deskripsi")
                st.write(info['deskripsi'])
                st.markdown("##### Gejala Umum")
                for gejala in info['gejala']:
                    st.markdown(f"- {gejala}")
                st.markdown("##### Saran Penanganan")
                for saran in info['penanganan']:
                    st.markdown(f"- {saran}")
            else:
                # Jika confidence di bawah ambang batas
                st.error("Model Tidak Cukup Yakin dengan Prediksi Ini.")
                st.markdown(f"**Tingkat Kepercayaan Terdeteksi:** `{confidence:.2%}` (di bawah `{CONFIDENCE_THRESHOLD:.0%}`)")
                st.write("---")
                st.info("Saran:", icon="💡")
                st.markdown("""
                - Coba ambil gambar dari sudut yang berbeda.
                - Pastikan pencahayaan cukup dan tidak ada bayangan yang menutupi daun.
                - Pastikan gambar fokus dan tidak buram.
                - Objek utama dalam gambar haruslah daun yang diduga sakit.
                """)

            st.warning("**Disclaimer:** Ini adalah hasil dari model AI dan mungkin tidak 100% akurat. Selalu konsultasikan dengan ahli agronomi untuk diagnosis definitif.", icon="⚠️")