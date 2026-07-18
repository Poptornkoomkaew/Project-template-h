# =====================================================
#  personnel/remove_member.py — คนรับผิดชอบ: ______________________
# =====================================================
from data import family_members

# TODO: สร้างฟังก์ชัน remove_member(target_name)
#   - หาคนที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก) แล้วลบออกจาก family_members
#   - ลบสำเร็จ -> return True | ไม่เจอ -> return False
def remove_member (target_name):
    x = target_name.lower()
    for i in family_members : 
        m = i["name"].lower()
        if x == m:
            family_members.remove(i)
            return True
    return False

# ทดสอบ: python -m personnel.remove_member
if __name__ == "__main__":
    print(remove_member("Luigi"))   # ครั้งแรกต้องได้ True
    print(remove_member("Luigi"))   # ครั้งที่สองต้องได้ False (ลบไปแล้ว)
    print(family_members)           # ต้องเหลือแค่ Tony
