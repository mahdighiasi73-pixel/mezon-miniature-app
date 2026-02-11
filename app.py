import streamlit as st
import google.generativeai as genai
from PIL import Image

# تنظیمات ظاهری برنامه
st.set_page_config(page_title="Mezon Miniature", page_icon="👗")
st.markdown("<h1 style='text-align: center; color: #d4af37;'>اتاق پرو مجازی مزون مینیاتور</h1>", unsafe_allow_html=True)

# تنظیمات اتصال به API
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("لطفاً API Key را در تنظیمات Streamlit وارد کنید.")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

    # --- تنظیمات اختصاصی شما از AI Studio ---
    generation_config = {
        "temperature": 1,  # این عدد را طبق AI Studio تغییر دهید
        "top_p": 0.95,
        "max_output_tokens": 8192,
    }

 model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",  # حتما کلمه models/ را قبل از نام مدل بگذارید
    generation_config=generation_config,
    system_instruction="شما دستیار مزون مینیاتور هستید و لباس عروس را روی تصویر مشتری پرو می‌کنید."
)
    # طراحی بخش آپلود
    col1, col2 = st.columns(2)
    with col1:
        user_img = st.file_uploader("عکس خودتان", type=['jpg', 'png'])
    with col2:
        dress_img = st.file_uploader("عکس لباس مزون", type=['jpg', 'png'])

    if st.button("✨ اجرای پرو مجازی"):
        if user_img and dress_img:
            with st.spinner("در حال جادو..."):
                img1 = Image.open(user_img)
                img2 = Image.open(dress_img)
                
                # ارسال به مدل
                response = model.generate_content([
                    "لباس تصویر دوم را روی شخص در تصویر اول قرار بده و خروجی را توصیف کن (یا تصویر بساز)", 
                    img1, 
                    img2
                ])
                st.write(response.text)
        else:
            st.warning("لطفاً هر دو عکس را آپلود کنید.")
