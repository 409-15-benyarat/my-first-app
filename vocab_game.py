import time
import streamlit as st

st.title("⏱️ ทายศัพท์จับเวลา:โดราเอม่อน")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.ans6_val = ""  # เคลียร์ค่าช่องข้อ 6
    st.session_state.ans7_val = ""  # เคลียร์ค่าช่องข้อ 7
    st.session_state.ans8_val = ""  # เคลียร์ค่าช่องข้อ 8
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans1 = ans3.strip().lower()
    u_ans2 = ans4.strip().lower()
    u_ans1 = ans5.strip().lower()
    u_ans2 = ans6.strip().lower()
    u_ans1 = ans7.strip().lower()
    u_ans2 = ans8.strip().lower()
    
    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

     # ตรวจข้อ 3
    if u_ans3 == "fish":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

     # ตรวจข้อ 4
    if u_ans4 == "fish":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

     # ตรวจข้อ 5
    if u_ans5 == "fish":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

     # ตรวจข้อ 6
    if u_ans6 == "fish":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")

     # ตรวจข้อ 7
    if u_ans7 == "fish":
        st.success("✅ ข้อ 7: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")

     # ตรวจข้อ 8
    if u_ans8 == "fish":
        st.success("✅ ข้อ 8: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 8: ยังไม่ถูกต้อง (คุณตอบ '{u_ans8}')")
        

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 8:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: เป็นตัวละครลักษณะภายนอกเป็นตัวสีฟ้า มีความสามารถในการเสกของวิเศษออกมาได้",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: เป็นตัวละครลักษณะภายนอกเป็นผู้ชายใส่แว่น เสื้อสีเหลือง กางเกงสีฟ้า",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: เป็นตัวละครที่ลักษณะภายนอกเป็นคนรูปร่างใหญ่ ใส่เสื้อสีส้ม ชอบแกล้งโนบิตะ และ ร้องเพลงเพี้ยน",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: เป็นตัวละครหญิง มัดผมแกละสองข้าง ใส่เสื้อสีชมพูและกระโปรงสั้น ชอบเล่นไวโอลิน",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5: เป็นตัวละครชาย มีผมและปากแหลมๆ ตาตี่ รวย ชอบพูดจาโอ้อวดและเจ้าเล่ห์ ชอบแกล้งโนบิตะ",
    value=st.session_state.ans5_val,
)
ans6 = st.text_input(
    "ข้อ 6: เป็นตัวละครชาย ฉลาดและเรียนเก่ง หน้าตาดี บุคลิกดี ไม่พูดจาโอ้อวด",
    value=st.session_state.ans6_val,
)
ans7 = st.text_input(
    "ข้อ 7: ตัวละครสีฟ้า เสกของวิเศษได้",
    value=st.session_state.ans7_val,
)
ans8 = st.text_input(
    "ข้อ 8: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans8_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6
st.session_state.ans7_val = ans7
st.session_state.ans8_val = ans8


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8)

st.divider()
st.write("นางเบญญารัตน์ นาวิก เลขที่ 15 ม.4/9")



