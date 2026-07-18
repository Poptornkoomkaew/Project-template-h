# =====================================================
#  personnel/add_member.py — คนรับผิดชอบ: ______________________
# =====================================================
from data import family_members

# TODO: สร้างฟังก์ชัน add_member(name, age, power, money)
#   - คำนวณ role: power >= 8 -> "Hitman" | money >= 1000000 -> "Sponsor" | นอกนั้น -> "Slave"
#   - สร้าง dict สมาชิกใหม่ (key: name, age, role, power, money, equipment เริ่มต้น "ไม่มี")
#   - เพิ่มเข้า family_members แล้ว return dict นั้น
def add_member(name, age, power, money):
    if power >= 8:
         role = "Hitman"
    elif money >= 1000000:
         role = "Sponsor"
    else:
         role = "Slave"

    member = {
     "name": name,
     "age": age,
     "role": role,
     "power": power,
     "money": money,
     "equipment": "ไม่มี"
    }
    family_members.append(member)

# ทดสอบ: python -m personnel.add_member
if __name__ == "__main__":
    add_member("Vito", 20, 9, 500)
    print(family_members)   # ต้องเห็น Vito ต่อท้าย และ role เป็น Hitman
