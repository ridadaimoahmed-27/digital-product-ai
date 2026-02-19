import streamlit as st
import requests

# --- الإعدادات (مفتاحك الذي أرسلته لي) ---
API_KEY = "Sk-proj-A_B_ZwmK1Eq--7VsOm5K7dH5pCw671eZK5V8Sp6VVDVSIv4AWDBxUHq8GoI1smw-NBwLpUcwcFT3BlbkFJHBsTtU7ndhw_qF2CwQwa2O0DH6jEv6nWoRcPw5_7nuWRmwrtRGp8XJ6ES6Nt_5r0tsqvxZ4NgA"
URL = "https://api.openai.com/v1/images/generations"

st.set_page_config(page_title="مصنع الصور الذكي", page_icon="🎨")

st.title("🎨 مولد الصور بالذكاء الاصطناعي")
st.write("اكتب فكرتك وسأحولها إلى صورة احترافية")

# إدخال الوصف
prompt = st.text_input("وصف الصورة (بالانجليزية أفضل لنتائج مبهرة):", placeholder="e.g. A futuristic car in Algerian Sahara, cinematic lighting")

if st.button("إبدأ التوليد ✨"):
    if prompt:
        with st.spinner("جاري الرسم... انتظر قليلاً"):
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }
            data = {
                "model": "dall-e-3",
                "prompt": prompt,
                "n": 1,
                "size": "1024x1024"
            }
            
            response = requests.post(URL, json=data, headers=headers)
            
            if response.status_code == 200:
                image_url = response.json()['data'][0]['url']
                st.image(image_url, caption="النتيجة النهائية")
                
                # زر التحميل
                st.markdown(f'[📥 اضغط هنا لتحميل الصورة]({image_url})')
                st.success("تم التوليد بنجاح!")
            else:
                st.error("خطأ: تأكد من شحن رصيد OpenAI أو صحة المفتاح.")
    else:
        st.warning("الرجاء إدخال وصف أولاً")

st.info("نصيحة: الصور التي تولدها يمكنك بيعها يدوياً على فيسبوك أو منصات التصميم.")

import streamlit as st
import requests
import os
from dotenv import load_dotenv

# تحميل البيانات من ملف .env
load_dotenv()

# سحب المفاتيح من الملف
API_KEY = os.getenv("DALL_E_API_KEY")
GUMROAD_KEY = os.getenv("GUMROAD_API_KEY")

# تكملة الكود...
