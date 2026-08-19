import random

def game():
    hp = int(input("당신의 HP는?\n➡️ "))

    for i in range(5):
        damage = random.randint(10, 50000)

        print(damage, "의 데미지를 받았다!")

        hp = hp - damage

        print("현재 hp : ", hp, "턴수 : ", i + 1)

        if hp <= 0:
            print("You die...")
            break

    if hp > 0:
        print("살아남으셨습니다 ㅊㅊ")


print("안녕하세요 이승훈입니다.")
print("게임시작하겠습니다.")

gs = int(input("시작하려면 1을 입력하시오.\n"))

if gs == 1:
    print("게임시작!")
    print("====================")
    game()

else:
    print("게임종료")
