#어떤 수 n이 입력되면 n의 각 자릿수의 합이 한 자리가 될때까지 계산하여 출력하시오.

#예) 1234567

#1234567 → 1+2+3+4+5+6+7 = 28 → 2 + 8 = 10 → 1 + 0 = 1


def SumofDigits(num):
    result = 0
    x = 0
    if len(str(num)) > 1:
        for i in str(num):
            x += int(i)
        SumofDigits(x)
    else:
        print(num)

inputx = input()

SumofDigits(inputx)
