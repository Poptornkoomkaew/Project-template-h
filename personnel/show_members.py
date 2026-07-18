l# =====================================================
#  personnel/show_members.py — คนรับผิดชอบ: ______________________
# =====================================================
from data import family_members

# TODO: สร้างฟังก์ชัน show_members()
#   - print ข้อมูลลูกน้องทุกคนใน family_members บรรทัดละคน (ชื่อ, ตำแหน่ง, ความโหด, อาวุธ)
def show_members():
    for i in family_members:
        print(f"Name: {i["name"].upper()} | age:  {i["age"]} |role: {i["role"]} | Money: {i["money"]} | equipment: {i["equipment"]}")



# ทดสอบ: python -m personnel.show_members
if __name__ == "__main__":
    show_members()   # ต้องเห็น Tony กับ Luigi คนละบรรทัด
