# =====================================================
#  personnel/search_member.py — คนรับผิดชอบ: Mj
# =====================================================
from data import family_members

# TODO: สร้างฟังก์ชัน search_member(target_name)
#   - หาคนใน family_members ที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก)
#   - เจอ -> return dict ของคนนั้น | ไม่เจอ -> return None
def search_member(target_name) :
    for person in family_members :
        if target_name.lower() == person["name"].lower() :
            return person["name"]
        else :
            return None
            


# ทดสอบ: python -m personnel.search_member
if __name__ == "__main__":
    print(search_member("tony"))        # ต้องได้ dict ของ Tony (พิมพ์เล็กก็ต้องเจอ)
    print(search_member("ไม่มีคนนี้"))    # ต้องได้ None
