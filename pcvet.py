import psutil #เรียกใช้ ไลเบอรี่ psutil

def decide_mood(cpu, disk): #สร้างฟังชั่นชื่อ decid_mood รับค่า พารามิเตอร์ของ cpu disk
    if cpu >= 80: #ถ้า cpu ใช้งานมากว่าหรือเท่ากับ 80% ให้เหงื่อออกแทน sweaty
        return "sweaty"
    elif disk >= 90: #ถ้า disk ไดรฟ์ C ใช้งานมากกว่าหรือเท่ากับ 90% ให้แสดง fat
        return "fat"
    else: #ถ้าไม่เข้าเงื่อนไขทั้งสอง ก็ให้เป็นปกติ แทน normal
        return "normal"

CATS = { #สร้าง dict เพื่อจัดเก็บรูปภาพของน้องแมว
    "normal": r"""
        /\_/\
       (^   ^)
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
}

def draw_cat(mood): #กำหนดฟังชั่น เรียกใช้ mood ตามชื่อใน dict 
    return CATS[mood] #แล้วคืนค่านั้นไปที่ mood 


cpu = psutil.cpu_percent(interval=1) #กำหนดตัวแปร cpu เพื่อรับค่าการใช้งาน ณ เวลา 1 วินาที
disk = psutil.disk_usage("C:\\").percent #กำหนดตัวแปร disk เพื่อรับค่าการใช้งาน disk ทั้งหมดของ ไดรฟ์ C: และใช้ \\ เพราะต้องการให้ python ใช้เครื่องหมาย \
mood = decide_mood(cpu, disk) #กำหนดตัวแปร mood เพื่อเรียกใช้ฟังชั่น decide_mood 

# _U ย่อมาจาก USE
print("Cpu_U:", cpu , "%") #แสดงผลค่า ตัวแปร cpu ต่อท้ายด้วยเครื่องหมาย % 
print("Disk_U:", disk, "%") #แสดงผลค่า ตัวแปร disk แต่เอาแค่เปอเซ็นเท่านั้นต่อท้ายด้วยเครื่องหมาย %
print("Mood:", mood) #แสดงผลตามฟังชั่น
print(draw_cat(mood)) #แสดงผลตัวการ์ตูนของเรา