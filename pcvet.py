import psutil #เรียกใช้ ไลเบอรี่ psutil
import time #เรียกใช้ ไลเบอรี่ time
import os #เรียกใช้ ไลเบอรี่ os

def decide_mood(cpu, disk, uptime_hours): #สร้างฟังชั่นชื่อ decid_mood รับค่า พารามิเตอร์ของ cpu disk
    if cpu >= 80: #ถ้า cpu ใช้งานมากว่าหรือเท่ากับ 80% ให้เหงื่อออกแทน sweaty
        return "sweaty"
    elif disk >= 90: #ถ้า disk ไดรฟ์ C ใช้งานมากกว่าหรือเท่ากับ 90% ให้แสดง fat
        return "fat"
    elif uptime_hours >= 6: #ถ้าเปิดเครื่องมานานกว่าหรือเท่ากับ 6 ชั่วโมง ให้แสดง tired
        return "tired"
    else: #ถ้าไม่เข้าเงื่อนไขทั้งสอง ก็ให้เป็นปกติ แทน normal
        return "normal"

CATS = { #สร้าง dict เพื่อจัดเก็บรูปภาพของน้องแมว
    "normal": r"""
        /\_/\
       (^ . ^)
       >  ^  <
          n 
    """,
    "sweaty": r"""
       ~/\_/\~
       (> . <)
       >  ~  <
          h 
    """,
    "fat": r"""
        //\_/\\
        ( -.- )
       ((  0  ))
           f
     """,
    "tired": r"""
        /\_/\   z
       ( -.- )z
       >  z  <
          t 

    """,
}

def draw_cat(mood): #กำหนดฟังชั่น เรียกใช้ mood ตามชื่อใน dict 
    return CATS[mood] #แล้วคืนค่านั้นไปที่ mood 

try:
    while True: #สร้าง loop ที่เช็คเงื่อนไขว่าเป็นจริงไหม และทำซ้ำทุกรอบเมื่อเงื่อนไขเป็นจริง
        cpu = psutil.cpu_percent(interval=1) #กำหนดตัวแปร cpu เพื่อรับค่าการใช้งาน ณ เวลา 1 วินาที
        disk = psutil.disk_usage("C:\\").percent #กำหนดตัวแปร disk เพื่อรับค่าการใช้งาน disk ทั้งหมดของ ไดรฟ์ C: และใช้ \\ เพราะต้องการให้ python ใช้เครื่องหมาย \
        uptime_hours = (time.time() - psutil.boot_time()) / 3600 #สร้างตัวแปร uptime_hours เก็บ เวลาปัจจุบันหน่วยวินาที มาลบกับ เวลาที่เครื่องบูตหน่วยวินาที หารด้วย 3600 เพราะ 1 ชั่วโมง 3600 วินาที
        mood = decide_mood(cpu, disk, uptime_hours) #กำหนดตัวแปร mood เพื่อเรียกใช้ฟังชั่น decide_mood 

        os.system("cls") #สั่งให้เคลียร์ clear เอง

        # _U ย่อมาจาก USE
        print(f"Cpu_U: {cpu:.2f} %") #ใช้ f หน้าเครื่องหมายคำพูดแสดงค่า Cpu_U เป็นทศนิยมผ่าน :.2f หมายถึงเอาแค่ 2 หลักและตามด้วย % ธรรมดา
        print(f"Disk_U: {disk:.2f} %") #ใช้ f หน้าเครื่องหมายคำพูดแสดงค่า Disk_U เป็นทศนิยมผ่าน :.2f หมายถึงเอาแค่ 2 หลักและตามด้วย % ธรรมดา
        print("Mood:", mood) #แสดงผลหน้าตาตามฟังชั่น
        print(f"Uptime:{uptime_hours:.2f} hours") #แสดงค่าการทำงานของ เครื่องนับตั้งแต่เครื่องเปิดใช้งานหน่วยเป็น ชั่วโมง
        print(draw_cat(mood)) #แสดงผลตัวการ์ตูนของเรา

        time.sleep(3) #สั่งให้โปรแกรมรอ 3 วินาทีในแต่ละรอบ
except KeyboardInterrupt: #ถ้าผู้ใช้เกิด ทำเหตุการณ์ที่ขึ้น KeyboardInterrupt เช่น Ctrl + C จะให้แสดงข้อความ ถ้าไม่ก็เข้า ลูปปกติ
    print("See you again ^.^")