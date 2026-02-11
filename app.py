import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Mezon Miniature", page_icon="👗")

# استایل دهی ساده
st.markdown("<h1 style='text-align: center; color: #d4af37;'>اتاق پرو مجازی مزون مینیاتور</h1>", unsafe_allow_html=True)

if "GOOGLE_API_KEY" not in st.secrets:
    st.error("لطفاً کلید API را در تنظیمات وارد کنید.")
else:
    # تنظیم کلید
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

    try:
        # استفاده از مدل بدون پیشوند v1beta
        # این کار باعث می‌شود کتابخانه خودش بهترین نسخه در دسترس را انتخاب کند
        model = genai.GenerativeModel('gemini-1.5-flash')

        u_file = st.file_uploader("عکس مشتری", type=['jpg', 'png', 'jpeg'])
        d_file = st.file_uploader("عکس لباس مزون", type=['jpg', 'png', 'jpeg'])

        if st.button("✨ اجرای پرو مجازی"):
            if u_file and d_file:
                with st.spinner("در حال تحلیل استایل..."):
                    img1 = Image.open(u_file)
                    img2 = Image.open(d_file)
                    
                    # ارسال عکس‌ها به هوش مصنوعی
                    response = model.generate_content([
                        "شما مشاور حرفه‌ای مزون مینیاتور هستید. با دقت به این دو تصویر نگاه کنید. تصویر اول مشتری و تصویر دوم لباس عروس است. تحلیل کنید که این لباس چطور بر تن این شخص می‌نشیند و توصیفی هنرمندانه و فارسی ارائه دهید.",
                        img1, 
                        img2
                    ])
                    
                    st.success("نتیجه پرو هوشمند مینیاتور:")
                    st.write(response.text)
            else:
                st.warning("لطفاً هر دو عکس را آپلود کنید.")

    except Exception as e:
        # اگر باز هم ارور داد، لیست مدل‌های در دسترس را چاپ می‌کنیم تا متوجه مشکل شویم
        st.error(f"خطا در مدل: {e}")
        if "404" in str(e):
            st.info("در حال تلاش برای یافتن مدل‌های جایگزین...")
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            st.write("مدل‌های در دسترس اکانت شما:", available_models)
