import psutil #เรียกใช้ ไลเบอรี่ psutil
import time #เรียกใช้ ไลเบอรี่ time
import os #เรียกใช้ ไลเบอรี่ os
import json #เรียกใช้ ไลเบอรี่ json
import logging #เรียกใช้ ไลเบอรี่ logging
from logging.handlers import RotatingFileHandler

REQUIRED_MOODS = {"normal", "sweaty", "fat", "tired", "hungry"} # สร้าง set มาจัดเก็บชื่อของ อารมณ์ที่ต้องมี
LOG_FILD = "pcvet.log" #สร้างไฟล์คงที่เพื่อให้เวลาเรียกใช้ pcvet.log จะได้แก้ทีเดียว
LOG_DEFAULT_LINES = 10 #เพดานจำนวน log ที่ผู้ใช้ทำคำสั่งแบบไม่ระบุจำนวนบรรทัด 10 บรรทัด
LOG_MAX_LINES = 200 #เพดานจำนวน log สูงสุดเมื่อผู้ใช้ระบบจำนวนบรรทัดห้ามเกินนี้ 200 บรรทัด

handler = RotatingFileHandler( #สร้าง handler ไฟล์ pcvet เก็บค่า log และหมุนไฟล์ให้เองเรื่อยๆ
    LOG_FILD,
    maxBytes=500_000, #ไฟล์ละสูงสุด 500KB 
    backupCount=3, #สร้างสูงสุด 3 ไฟล์
    encoding="utf-8", #รูปแบบ UTF-8
)
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s")) #ตั้ง format ว่าจะเก็บหน้าตาแบบไหนในที่นี้คือ เวลา เลเวล และ ข้อความ

logger = logging.getLogger("pcvet")
logger.setLevel(logging.INFO) #จดตั้งแต่ INFO ขึ้นไป
logger.addHandler(handler) #รวมกัน logger เป็นคนจดเหตุการณ์ส่วน handler ก็เขียนไฟล์ให้

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

def load_skin(path): #สร้างฟังชั่น load_skin รับพารามิเตอร์ path
    try:
        with open(path, encoding="utf-8") as f: #เปิดไฟล์สกินของเรา และให้อ่านด้วย UTF-8 กัน windows เอ๋อ และตั้งชื่อไฟล์ให้เป็น f
            return json.load(f)
    except FileNotFoundError: #ถ้าหาไฟล์สกินไม่เจอก็ให้แสดงข้อความต่อไปนี้และย้อยกลับ None
        logger.error("Can't found the skin file: %s", path) #ให้ logger เป็นคนเอาค่าไปแทนที่เอง
        print(f"Can't found the skin file: {path}")
        return None
    except json.JSONDecodeError as e: #ถ้ารูปแบบไฟล์ json ผิด ให้เป็น e และแสดงข้อความต่อไปนี้ พร้อมข้อความบอกรายละเอียดและย้อนกลับ None
        logger.error("Can't found the skin file: %s", path, e) #ให้ logger เป็นคนเอาค่าไปแทนที่เอง
        print(f"Skin file is formatted incorrectly: {path}")
        print(f"Details: {e}")
        return None

def check_skin(skin):
    missing = REQUIRED_MOODS - set(skin["faces"].keys()) #เช็คด้วยการ แปลงสกินให้เป็นเซตและ เอามาลบกันด้วยเซตที่มีอยู่ถ้าเหลือแสดงว่า อารมณ์ไม่ครบ
    if missing: #ถ้าเซตที่ลบแล้วกลายเป็นเซตว่างให้แสดงข้อความ
        print(f"Skin this missing mood: {', '.join(sorted(missing))}") #เรียงตามตัวอักษรให้อ่านง่ายและคั่นด้วย ","
        return False
    return True
    #return True False บอกว่าสกินผ่านหรือไม่

skin = load_skin("skins/cat.json") #สร้างตัวแปร skin มาเพื่อเรียกใช้ฟังชั่นโหลดสกินพร้อมบอก path ที่อยู่
if skin is None or not check_skin(skin): #ถ้า skin เป็น None โปรแกรมจบถ้าไม่เป็นก็วิ่งไปเช็คสกินต่อ
    raise SystemExit(1)

def draw_cat(mood): 
    return "\n".join(skin["faces"][mood]) #หยิบไฟล์สองชั้น คือ หน้าตา และชื่ออารมณ์ และเอาทุกบรรทัดมาต่อกันใหม่ ขึ้นบรรทัดด้วย /n 


logger.info("Program starts running.") #ถ้าผู้ใช้เริ่มโปรแกรมให้จดลง log
last_mood = None #สร้างตัวแปรมาเพื่อ เก็บค่าของ mood ล่าสุดที่แสดง

try:
    while True: #สร้าง loop ที่เช็คเงื่อนไขว่าเป็นจริงไหม และทำซ้ำทุกรอบเมื่อเงื่อนไขเป็นจริง
        cpu = psutil.cpu_percent(interval=1) #กำหนดตัวแปร cpu เพื่อรับค่าการใช้งาน ณ เวลา 1 วินาที
        disk = psutil.disk_usage("C:\\").percent #กำหนดตัวแปร disk เพื่อรับค่าการใช้งาน disk ทั้งหมดของ ไดรฟ์ C: และใช้ \\ เพราะต้องการให้ python ใช้เครื่องหมาย \
        uptime_hours = (time.time() - psutil.boot_time()) / 3600 #สร้างตัวแปร uptime_hours เก็บ เวลาปัจจุบันหน่วยวินาที มาลบกับ เวลาที่เครื่องบูตหน่วยวินาที หารด้วย 3600 เพราะ 1 ชั่วโมง 3600 วินาที
        ram = psutil.virtual_memory().percent
        mood = decide_mood(cpu, disk, uptime_hours, ram) #กำหนดตัวแปร mood เพื่อเรียกใช้ฟังชั่น decide_mood 
        if mood != last_mood: #สร้าง เงื่อนไขว่า ถ้าอารมณ์ที่แสดงตอนนี้ ไม่ได้เท่ากับอารมณ์ที่เก็บไว้ใน last_mood ให้ log เก็บค่า และ ให้ last_mood = mood ปัจจุบัน
            logger.info("Mood swings: %s -> %s (cpu=%.1f disk=%.1f ram=%.1f)", last_mood, mood, cpu , disk, ram )
            last_mood = mood

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
    logger.info("User stops the program.") #ถ้าผู้ใช้หยุดโปรแกรม ให้จดลง log 
    print("See you again ^.^")