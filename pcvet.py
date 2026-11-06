import psutil #เรียกใช้ ไลเบอรี่ psutil
import time #เรียกใช้ ไลเบอรี่ time
import os #เรียกใช้ ไลเบอรี่ os
import json #เรียกใช้ ไลเบอรี่ json

def decide_mood(cpu, disk, uptime_hours, ram): #สร้างฟังชั่นชื่อ decid_mood รับค่า พารามิเตอร์ของ cpu disk uptime_hours ram
    if cpu >= 80: #ถ้า cpu ใช้งานมากว่าหรือเท่ากับ 80% ให้เหงื่อออกแทน sweaty
        return "sweaty"
    elif disk >= 90: #ถ้า disk ไดรฟ์ C ใช้งานมากกว่าหรือเท่ากับ 90% ให้แสดง fat
        return "fat"
    elif ram >= 85: #ถ้า ram ใช้งานเกินหรือมากกว่า 85% ให้แสดงสถานะ hungry
        return "hungry"
    elif uptime_hours >= 6: #ถ้าเปิดเครื่องมานานกว่าหรือเท่ากับ 6 ชั่วโมง ให้แสดง tired
        return "tired"
    else: #ถ้าไม่เข้าเงื่อนไขทั้งสี่ ก็ให้เป็นปกติ แทน normal
        return "normal"

with open("skins/cat.json", encoding="utf-8") as f: #เปิดไฟล์สกินของเรา และให้อ่านด้วย UTF-8 กัน windows เอ๋อ และตั้งชื่อไฟล์ให้เป็น f
    skin = json.load(f) #สร้างตัวแปร skin เพื่อให้อ่านไฟล์ json เก็บเป็น dict

def draw_cat(mood): 
    return "\n".join(skin["faces"][mood]) #หยิบไฟล์สองชั้น คือ หน้าตา และชื่ออารมณ์ และเอาทุกบรรทัดมาต่อกันใหม่ ขึ้นบรรทัดด้วย /n 

try:
    while True: #สร้าง loop ที่เช็คเงื่อนไขว่าเป็นจริงไหม และทำซ้ำทุกรอบเมื่อเงื่อนไขเป็นจริง
        cpu = psutil.cpu_percent(interval=1) #กำหนดตัวแปร cpu เพื่อรับค่าการใช้งาน ณ เวลา 1 วินาที
        disk = psutil.disk_usage("C:\\").percent #กำหนดตัวแปร disk เพื่อรับค่าการใช้งาน disk ทั้งหมดของ ไดรฟ์ C: และใช้ \\ เพราะต้องการให้ python ใช้เครื่องหมาย \
        uptime_hours = (time.time() - psutil.boot_time()) / 3600 #สร้างตัวแปร uptime_hours เก็บ เวลาปัจจุบันหน่วยวินาที มาลบกับ เวลาที่เครื่องบูตหน่วยวินาที หารด้วย 3600 เพราะ 1 ชั่วโมง 3600 วินาที
        ram = psutil.virtual_memory().percent
        mood = decide_mood(cpu, disk, uptime_hours, ram) #กำหนดตัวแปร mood เพื่อเรียกใช้ฟังชั่น decide_mood 

        os.system("cls") #สั่งให้เคลียร์ clear เอง

        # _U ย่อมาจาก USE
        print(f"Cpu_U: {cpu:.2f} %") #ใช้ f หน้าเครื่องหมายคำพูดแสดงค่า Cpu_U เป็นทศนิยมผ่าน :.2f หมายถึงเอาแค่ 2 ตำแหน่งและตามด้วย % ธรรมดา
        print(f"Disk_U: {disk:.2f} %") #ใช้ f หน้าเครื่องหมายคำพูดแสดงค่า Disk_U เป็นทศนิยมผ่าน :.2f หมายถึงเอาแค่ 2 ตำแหน่งและตามด้วย % ธรรมดา
        print(f"Ram_U: {ram:.2f} %")
        print(f"Uptime:{uptime_hours:.2f} hours") #แสดงค่าการทำงานของ เครื่องนับตั้งแต่เครื่องเปิดใช้งานหน่วยเป็น ชั่วโมง
        print("Mood:", mood) #แสดงผลหน้าตาตามฟังชั่น
        print(draw_cat(mood)) #แสดงผลตัวการ์ตูนของเรา

        time.sleep(3) #สั่งให้โปรแกรมรอ 3 วินาทีในแต่ละรอบ
except KeyboardInterrupt: #ถ้าผู้ใช้เกิด ทำเหตุการณ์ที่ขึ้น KeyboardInterrupt เช่น Ctrl + C จะให้แสดงข้อความ ถ้าไม่ก็เข้า ลูปปกติ
    print("See you again ^.^")