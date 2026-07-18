# =====================================================
#  weapon_shop/equip_item.py — คนรับผิดชอบ: ______________________
# =====================================================

# TODO: สร้างฟังก์ชัน equip_item(person, weapon)
#   - เช็คเงิน: เงินของ person ไม่พอราคา weapon -> ซื้อไม่ได้
#   - เช็คอาวุธ: person มีอาวุธอยู่แล้ว (equipment ไม่ใช่ "ไม่มี") -> ใส่เพิ่มไม่ได้
#   - ผ่านทั้งคู่ -> หักเงิน, เปลี่ยน equipment เป็นชื่ออาวุธ, บวก bonus เข้า power
#   - return {"status": True/False, "message": ข้อความบอกผล}


# ทดสอบ: python -m weapon_shop.equip_item
def equip_item(person, weapon):
    if person["money"] < weapon["price"]:
        return {"status": False, "message": "ซื้อไม่ได้"}
    
    if person["equipment"] != "ไม่มี":
        return {"status":False, "message": "ใส่เพิ่มไม่ได้"}

    person["money"] = person["money"] - weapon["price"]
    person["equipment"]= weapon["name"]
    person["power"] = person["power"] + weapon["bonus"]
    # print(person["money"])
    # print(person["equipment"])
    # print(person["power"]
    return {"status": True, "message": "ซื้อสำเร็จ"}

if __name__ == "__main__":
    vito = {"name": "Vito", "money": 60000, "power": 5, "equipment": "ไม่มี"}
    gun = {"name": "ปืนพก 9mm", "price": 50000, "bonus": 5}
    print(equip_item(vito, gun))   # ต้องได้ status True
    print(vito)                    # เงินเหลือ 10000, power เป็น 10, equipment เป็นปืน
    print(equip_item(vito, gun))   # ครั้งที่สองต้องได้ status False (มีอาวุธแล้ว)