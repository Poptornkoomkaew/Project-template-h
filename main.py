# =====================================================
#  main.py — ศูนย์กลางของระบบ (งานของหัวหน้ากลุ่ม!)
#
#  เมนู 1-6 หัวหน้าเขียนเอง โดยเรียกใช้ฟังก์ชันที่เพื่อนเขียน
#  pattern เดียวกันทุกเมนู:  รับ input -> เรียกฟังก์ชัน -> print ผลลัพธ์
#
#  สำคัญ: ไฟล์นี้จะรันได้ก็ต่อเมื่อทุกไฟล์ประกาศฟังก์ชันแล้ว
#  -> งานแรกของทุกคน: สร้างโครงฟังก์ชันตัวเอง (def ... + pass) แล้ว push ทันที
# =====================================================
from data import weapons_catalog
from personnel.add_member import add_member
from personnel.show_members import show_members
from personnel.search_member import search_member
from personnel.remove_member import remove_member
from weapon_shop.show_catalog import show_catalog
from weapon_shop.equip_item import equip_item
from missions.send_mission import send_mission

def main():
    while True:
        print("\n=== MAFIA MANAGEMENT SYSTEM ===")
        print("1. รับลูกน้องใหม่")
        print("2. ดูรายชื่อแก๊ง")
        print("3. ค้นหาประวัติ")
        print("4. สั่งเก็บลูกน้อง")
        print("5. คลังอาวุธ")
        print("6. ส่งไปทำภารกิจ")
        print("7. ออกจากระบบ")

        choice = input("เลือกคำสั่ง (1-7): ")

        # ---------- เมนู 1 ----------
        if choice == '1':
            print("\n--- เพิ่มลูกน้องใหม่ ---")
            name = input("ใส่ชื่อ :")
            age = int(input("ใส่อายุ :"))
            power = int(input("ใส่พลัง :"))
            money = float(input("ใส่เงิน :"))
            new = add_member(name,age,power,money)
            print(f"เพิ่ม {name} ในตำแหน่ง {new["role"]}")

        # ---------- เมนู 2 ----------
        elif choice == '2':
            print("\n--- รายชื่อลูกน้องทั้งหมด ---")
            show_members()

        # ---------- เมนู 3 ----------
        elif choice == '3':
            print("\n--- ค้นหาประวัติ ---")
            target_name = input("ใส่ชื่อ :")
            target = search_member(target_name)
            print(target)
            if target == None:
                print("ไม่พบชื่อในระบบ")
            else :
                print("เจอข้อมูล")

        # ---------- เมนู 4 ----------
        elif choice == '4':
            print("\n--- สั่งเก็บลูกน้อง ---")
            target_name = input("ใส่ชื่อ :")
            target = remove_member(target_name)
            if target == True :
                print("สั่งเก็บเรียบร้อย ")
            else : 
                print("ไม่พบชื่อในระบบ")
            
        # ---------- เมนู 5 ----------
        elif choice == '5':
            print("\n=== คลังอาวุธ ===")
            show_catalog()
            weapon = input("รับรหัสอาวุธ :")
            person = input("ใส่ชื่อคนที่มอบหมาย :")
            full_person = search_member(person)
            equip_item(full_person,weapons_catalog[weapon])

        # ---------- เมนู 6 (OPTIONAL) ----------
        elif choice == '6':
            print("\n--- ส่งไปทำภารกิจ ---")
            person = input("ใส่ชื่อ:")
            mission = search_member(person)
            go_out = send_mission(mission)
            if go_out["status"] == True :
                print(f"เงินรางวัล : {go_out["reward"]} \n ยอดเงินปัจจุบัน {mission["money"]} ")
            else : 
                remove_member(mission["name"])
                print("ตายแล้ว ล้มเหลว")


        elif choice == '7':
            print("ปิดระบบ...")
            break

        else:
            print("คำสั่งไม่ถูกต้อง")

if __name__ == "__main__":
    main()
