# Pcvet พาน้องไปหาหมอ (TH)

![Last commit](https://img.shields.io/github/last-commit/phurinwithree/pcvet)
![Top language](https://img.shields.io/github/languages/top/phurinwithree/pcvet)
![License](https://img.shields.io/github/license/phurinwithree/pcvet)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Status](https://img.shields.io/badge/status-in%20development-orange)

มาสคอตใน terminal ที่ชีวิตผูกกับสุขภาพคอมจริง ดูหน้าตามันก็รู้ว่าเครื่องเป็นยังไง ไม่ต้องอ่านตัวเลขหรือ log

```
 /\_/\
(^ . ^)   "วันนี้เป็นยังไงบ้าง"
>  ^  <

```

> **สถานะ:** กำลังเริ่มพัฒนา ยังไม่มีเวอร์ชันที่ติดตั้งใช้งานได้
## ลองรันดู
> [!WARNING]
> ตอนนี้ยังติดตั้งยากและใช้งานได้เฉพาะในโฟลเดอร์โปรเจคเท่านั้น
> ต้องใช้ Git, Python และคำสั่ง terminal เองหลายขั้นตอน
> เหมาะกับคนที่เขียนโค้ดเป็นหรือคุ้นเคยกับ terminal
> ตัวติดตั้งที่ง่ายกว่านี้ (`pipx`, `pip`, `.exe`) ยังอยู่ในแผนการพัฒนาในอนาคต

> [!WARNING]
> โปรดใช้คำสั่งอย่างระมัดระวัง

ต้องมี [Python](https://www.python.org/downloads/) 3.10 ขึ้นไป และ [Git](https://git-scm.com/install/windows) เสียก่อน

```powershell
git clone https://github.com/phurinwithree/pcvet.git
```
```powershell
cd pcvet
```
```powershell
python -m venv .venv
```
```powershell
.venv\Scripts\activate
```
```powershell
pip install psutil
```
```powershell
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


# Pcvet: Take Your Little Buddy to the Vet (EN)

A terminal mascot whose life is tied to the real health of your PC. Just look at its face to know how your machine is doing, no need to read numbers or logs.

```
 /\_/\
(^ . ^)   "How are you today?"
>  ^  <

```

> **Status:** Early development. There is no installable version yet.

## Try It Out

> [!WARNING]
> Right now it is hard to install and only works from inside the project folder.
> You need Git, Python, and several manual terminal steps.
> It is best suited for people who can code or are comfortable with a terminal.
> Easier installers (`pipx`, `pip`, `.exe`) are planned for future development.

> [!WARNING]
> Please run commands carefully.

You need [Python](https://www.python.org/downloads/) 3.10 or newer and [Git](https://git-scm.com/install/windows) first.

```powershell
git clone https://github.com/phurinwithree/pcvet.git
```
```powershell
cd pcvet
```
```powershell
python -m venv .venv
```
```powershell
.venv\Scripts\activate
```
```powershell
pip install psutil
```
```powershell
python pcvet.py
```

> [!NOTE]
> If running `.venv\Scripts\activate` shows a red error saying `running scripts is disabled on this system`, run the command below once, then try `activate` again.
>
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```
>
> This only unlocks scripts for your user account and does not affect the whole machine.

## Why I'm Building This

I believe computers should have programs that are easy to use. Many people think the terminal is complicated, but I believe it is not as hard as it seems.

This program tells you the state of your machine through a mascot's face. In the near future, once the project is finished, users will be able to customize the mascot however they like.

## Planned Features

- Skin system: anyone can create their own mascot with a single file
- The mascot changes its look based on the machine's condition (disk nearly full, high CPU load, machine left on for a long time)
- Translate Windows Event Log messages into plain language
- Commands that start with `/`, such as `/status`, `/log`, and `/help`
- AI help for questions about your machine (optional, uses your own API key)

## Privacy

- Everything runs on your machine. There is no server for this project and no analytics.
- Only the `/ask` command sends your question and a summary of your machine's status to the AI provider you choose yourself. This will be clearly shown during setup.
- API keys are stored in Windows Credential Manager, never as plain text, and never appear in logs.
- All core features work without any AI.

## License

MIT