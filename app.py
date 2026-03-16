# -*- coding: utf-8 -*-
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="AI Havalimanı Karar Destek", layout="wide")

st.title("🛫 Havalimanı Pazarlama Karar Destek Sistemi")
st.markdown("### Multimodal (Metin + Görsel) Analiz Dashboard")

# Yan Panel: Analiz Ayarları
st.sidebar.header("🔍 Analiz Parametreleri")
location_type = st.sidebar.selectbox(
    "Havalimanı Bölgesi Seçin:",
    ["Lounge / Bekleme Alanı", "Check-in / Kontuvar", "Yeme-İçme Alanı", "Güvenlik Geçişi"]
)

# Kriterlere göre simüle edilmiş nesne tespiti
vision_mock = {
    "Lounge / Bekleme Alanı": ["Koltuk Doluluğu: %85", "Atık/Kirlilik: Saptandı", "Aydınlatma: Yeterli"],
    "Check-in / Kontuvar": ["Kuyruk Uzunluğu: >10m", "Personel Sayısı: 2", "Bekleme Süresi: Yüksek"],
    "Yeme-İçme Alanı": ["Masa Temizliği: Düşük", "Gıda Çeşitliliği: Orta", "Yoğunluk: Orta"],
    "Güvenlik Geçişi": ["Arama Noktası: 3 Açık", "Akış Hızı: Yavaş", "Gerginlik Skoru: Orta"]
}

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Veri Giriş Katmanı")
    uploaded_file = st.file_uploader("Yelp Fotoğrafı Yükle", type=["jpg", "png", "jpeg"])
    user_review = st.text_area("Müşteri Yorumu (İngilizce):", height=150, 
                               placeholder="Örn: The food was great but the lounge was incredibly crowded and dirty.")

with col2:
    st.subheader("📊 Yapay Zeka Analiz Merkezi")
    
    if uploaded_file is not None and user_review != "":
        st.image(uploaded_file, caption=f"Kaynak: Yelp | Bölge: {location_type}", use_container_width=True)
        
        # 1. Görüntü İşleme Katmanı (Simülasyon)
        st.write("---")
        st.markdown("**👁️ Görüntüden Tespit Edilen Fiziksel Kriterler:**")
        detected_items = vision_mock[location_type]
        cols = st.columns(len(detected_items))
        for i, item in enumerate(detected_items):
            cols[i].info(item)
            
        # 2. Metin Analiz Katmanı
        analysis = TextBlob(user_review)
        score = analysis.sentiment.polarity
        
        st.write("---")
        st.markdown("**📝 Metinsel Duygu ve Pazarlama Analizi:**")
        
        if score > 0.1:
            st.success(f"Pozitif Deneyim Skoru: {score:.2f}")
            st.markdown("**Stratejik Tavsiye:** Deneyim kalitesini korumak için personel ödüllendirilmeli.")
        elif score < -0.1:
            st.error(f"Negatif Deneyim Skoru: {score:.2f}")
            st.markdown("**Stratejik Tavsiye:** ACİL MÜDAHALE! Fiziksel koşullar operasyonel verimliliği düşürüyor.")
        else:
            st.warning(f"Nötr Deneyim Skoru: {score:.2f}")
            
        # 3. MCDM Girdisi
        st.write("---")
        st.caption(f"ℹ️ Bu multimodal analiz sonucu, MCDM modelindeki '{location_type}' ağırlığını güncellenmiştir.")
    else:
        st.info("Analiz başlatmak için lütfen sol taraftan fotoğraf yükleyin ve metin girin.")