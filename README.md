# Pcvet พาน้องไปหาหมอ

![Last commit](https://img.shields.io/github/last-commit/phurinwithree/pcvet)
![Top language](https://img.shields.io/github/languages/top/phurinwithree/pcvet)
![License](https://img.shields.io/github/license/phurinwithree/pcvet)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Status](https://img.shields.io/badge/status-in%20development-orange)

มาสคอตใน terminal ที่ชีวิตผูกกับสุขภาพคอมจริง ดูหน้าตามันก็รู้ว่าเครื่องเป็นยังไง ไม่ต้องอ่านตัวเลขหรือ log

```
 /\_/\
(^   ^)   "วันนี้เป็นยังไงบ้าง"
>  ^  <

```

> **สถานะ:** กำลังเริ่มพัฒนา ยังไม่มีเวอร์ชันที่ติดตั้งใช้งานได้
# ลองรันดู
> [!WARNING]
> ตอนนี้ยังติดตั้งยากและใช้งานได้เฉพาะในโฟลเดอร์โปรเจคเท่านั้น
> ต้องใช้ Git, Python และคำสั่ง terminal เองหลายขั้นตอน
> เหมาะกับคนที่เขียนโค้ดเป็นหรือคุ้นเคยกับ terminal
> ตัวติดตั้งที่ง่ายกว่านี้ (`pipx`, `pip `, `.exe`) ยังอยู่ในแผนการพัฒนาในอนาคต

> [!WARNING]
> โปรดใช้คำสั่งอย่างระมัดระวัง

ต้องมี [python](https://www.python.org/downloads/) 3.10 ขึ้นไป และ [Git](https://git-scm.com/install/windows) เสียก่อน

```powershell
git clone https://github.com/phurinwithree/pcvet.git
cd pcvet
python -m venv .venv
.venv\Scripts\activate
pip install psutil
python pcvet.py
```
> [!NOTE]
> ถ้าตอนรัน `.venv\Scripts\activate` ขึ้นข้อความสีแดงว่า `running scripts is disabled on this system` ให้รันคำสั่งนี้ครั้งเดียว แล้วลอง `activate` ใหม่
>
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```
>
> คำสั่งนี้ปลดล็อกเฉพาะผู้ใช้ของคุณ ไม่กระทบทั้งเครื่อง

## ทำไมถึงทำ

เพราะผมเห็นว่า คอมพิวเตอร์ควรมีโปรแกรมที่ใช้งานได้ง่าย ถึงแม้ระบบจะรันอยู่บน Terminal ที่หลายคนอาจจะบอกว่ามันซับซ้อนแต่ผมเชื่อว่ามันไม่อยากเกินไป
โปรแกรมนี่จะช่วยบอกสถานะของเครื่องและแสดงมันผ่านหน้าตามาสคอตของเราที่ผู้ใช้สามารถปรับแต่งได้เองตามใจชอบในอนาคตอันใกล้เมื่อโปรเจคเสร็จ 

## แผนฟีเจอร์

- ระบบ skin: ใครก็สร้างมาสคอตเองได้ด้วยไฟล์เดียว
- มาสคอตเปลี่ยนหน้าตาตามอาการของเครื่อง (ดิสก์ใกล้เต็ม, CPU โหลดสูง, เปิดเครื่องค้างนาน)
- แปลข้อความจาก Windows Event Log เป็นภาษาคน
- คำสั่งขึ้นต้นด้วย `/` เช่น `/status`, `/log`, `/help`
- AI ช่วยตอบคำถามเรื่องเครื่อง (ไม่บังคับ ใช้ API key ของผู้ใช้เอง)

## ความเป็นส่วนตัว

- ทุกอย่างทำงานบนเครื่องของคุณ ไม่มี server ของโปรเจคนี้ และไม่มี analytics
- มีเพียงคำสั่ง `/ask` ที่ส่งคำถามและสรุปสถานะเครื่องไปยังผู้ให้บริการ AI ที่คุณเลือกเอง และจะแจ้งให้ทราบชัดเจนตอนตั้งค่า
- API key เก็บใน Windows Credential Manager ไม่เก็บเป็นข้อความธรรมดา และไม่ปรากฏใน log
- ฟีเจอร์หลักทั้งหมดใช้ได้โดยไม่ต้องมี AI

## ไลเซนส์

MIT