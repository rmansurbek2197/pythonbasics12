def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

def main():
    son = int(input("Faktorialini hisoblash uchun son kiriting: "))
    if son < 0:
        print("Faktorial faqat musbat sonlar uchun hisoblanadi")
    else:
        print(f"{son}ning faktoriali: {faktorial(son)}")

def takrorlash():
    javob = input("Dasturni takrorlashni istaysizmi? (ha/yo'q): ")
    if javob.lower() == "ha":
        main()
        takrorlash()
    elif javob.lower() == "yo'q":
        print("Dastur tugadi")
    else:
        print("Noto'g'ri javob. Iltimos, ha yoki yo'q deb javob bering.")
        takrorlash()

main()
takrorlash()