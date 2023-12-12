print("========================")
print("= 구구단 출력 프로그램 =")
print("========================")

while True:
    dan = int(input("몇 단을 출력할까요? "))
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan*i}")
    answer = input("계속하려면 y를 입력하시고 멈추려면 n 입력하세요. ")
    if answer.lower() == 'n':
        break
