import random
import streamlit as st

st.title("🟨 🟩 ⬛ Fruits Wordle")
st.write("ลองทายคำศัพท์หมวดผลไม้ภาษาอังกฤษที่มี 5 ตัวอักษรให้ถูกภายใน 6 ครั้ง")
st.write("💡 *พิมพ์คำศัพท์แล้วกด Enter บนคีย์บอร์ดได้เลย*")

# 1. กำหนดค่าเริ่มต้นใน session_state
if "คลังคำ" not in st.session_state:
    st.session_state.คลังคำ = [
        "apple",
        "mango",
        "lemon",
        "grape",
        "melon",
        "peach",
        "berry",
        "raisin",
        "guava",
        "prune",
    ]
    st.session_state.คำปริศนา = random.choice(st.session_state.คลังคำ)
    st.session_state.ประวัติการทาย = []
    st.session_state.เกมจบแล้ว = False


def เริ่มเกมใหม่():
    st.session_state.คำปริศนา = random.choice(st.session_state.คลังคำ)
    st.session_state.ประวัติการทาย = []
    st.session_state.เกมจบแล้ว = False


# 2. ฟังก์ชันตรวจสอบคำทาย (จะทำงานทันทีเมื่อผู้เล่นกด Enter)
def ตรวจสอบคำทาย():
    # ดึงคำที่พิมพ์มาจากตัวแปรชั่วคราวใน session_state
    key_ปัจจุบัน = f"input_round_{len(st.session_state.ประวัติการทาย)}"
    เดาคำ = st.session_state.get(key_ปัจจุบัน, "").lower().strip()

    if not เดาคำ:
        return

    if len(เดาคำ) != 5:
        st.warning("❌ กรุณาพิมพ์คำศัพท์ให้ครบ 5 ตัวอักษร")
        return

    คำปริศนา = st.session_state.คำปริศนา
    ผลลัพธ์คำใบ้ = ["⬛"] * 5
    คำปริศนา_คัดลอก = list(คำปริศนา)

    # รอบที่ 1: ตรวจสอบตัวอักษรที่ถูกทั้งตัวและตำแหน่ง (🟩)
    for i in range(5):
        if เดาคำ[i] == คำปริศนา[i]:
            ผลลัพธ์คำใบ้[i] = "🟩"
            คำปริศนา_คัดลอก[i] = None

    # รอบที่ 2: ตรวจสอบตัวอักษรที่ถูกแต่ผิดตำแหน่ง (🟨)
    for i in range(5):
        if ผลลัพธ์คำใบ้[i] != "🟩":
            if เดาคำ[i] in คำปริศนา_คัดลอก:
                ผลลัพธ์คำใบ้[i] = "🟨"
                คำปริศนา_คัดลอก[คำปริศนา_คัดลอก.index(เดาคำ[i])] = None

    สตริงคำใบ้ = "".join(ผลลัพธ์คำใบ้)
    st.session_state.ประวัติการทาย.append((เดาคำ, สตริงคำใบ้))


# 3. แสดงประวัติการทายทั้งหมดด้านบน
for รอบ, (เดา, คำใบ้) in enumerate(st.session_state.ประวัติการทาย, 1):
    st.write(f"**รอบที่ {รอบ}:** `{เดา.upper()}`  👉  {คำใบ้}")

โอกาสทั้งหมด = 6
รอบปัจจุบัน = len(st.session_state.ประวัติการทาย)

# ตรวจสอบสถานะเกม ชนะ/แพ้
if รอบปัจจุบัน > 0:
    เดาคำล่าสุด, คำใบ้ล่าสุด = st.session_state.ประวัติการทาย[-1]
    if เดาคำล่าสุด == st.session_state.คำปริศนา:
        st.session_state.เกมจบแล้ว = True
        st.success(
            f"🎉 ยินดีด้วย! คุณทายถูกแล้ว คำนั้นคือ: {st.session_state.คำปริศนา.upper()} 🟩🟩🟩🟩🟩"
        )
    elif รอบปัจจุบัน >= โอกาสทั้งหมด:
        st.session_state.เกมจบแล้ว = True
        st.error(
            f"😢 หมดโอกาสทายแล้ว! คำศัพท์ที่ถูกต้องคือ: {st.session_state.คำปริศนา.upper()}"
        )

# 4. แสดงช่องรับข้อมูล (ถ้าเกมยังไม่จบ)
if not st.session_state.เกมจบแล้ว and รอบปัจจุบัน < โอกาสทั้งหมด:
    # ผูกฟังก์ชัน ตรวจสอบคำทาย ไว้กับ on_change
    st.text_input(
        f"พิมพ์คำศัพท์ 5 ตัวอักษร (เหลือโอกาส {โอกาสทั้งหมด - รอบปัจจุบัน} ครั้ง):",
        max_chars=5,
        key=f"input_round_{รอบปัจจุบัน}",
        on_change=ตรวจสอบคำทาย,
    )

# 5. ปุ่มเริ่มเกมใหม่
if st.session_state.เกมจบแล้ว:
    st.button("🔄 เล่นใหม่อีกครั้ง", on_click=เริ่มเกมใหม่)
