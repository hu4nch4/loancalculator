import math

print('What do you want to calculate?')
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
cevrea = input()
if cevrea == "n":
    print('Enter the loan principal:')
    lprincipal = float(input())
    print('Enter the monthly payment:')
    mpayment = float(input())
    print('Enter the loan interest:')
    linterest0 = float(input())
    linterest1 = linterest0 / (12 * 100)
    # print(linterest1)
    x = mpayment / (mpayment - linterest1 * lprincipal)
    n = math.ceil((math.log(x, 1 + linterest1)))
    # print(n)
    nomo = math.ceil(n % 12)
    noy = n / 12
    # print(nomo)
    noybun = math.floor(noy)
    print('It will take', noybun, 'years and', nomo, 'months to repay this loan!')
elif cevrea == "p":
    print('Enter the annuity payment:')
    peluna = float(input())
    print('Enter the number of periods:')
    cateluni = float(input())
    print('Enter the loan interest:')
    linterest0 = float(input())
    interest1 = linterest0 / (12 * 100)
    op1 = interest1 * math.pow((1 + interest1), cateluni)
    op2 = math.pow((1 + interest1), cateluni) - 1
    paranteza1 = op1 / op2
    final = peluna / paranteza1
    final2 = round(final)
    print('Your loan principal = {}!'.format(final2))
elif cevrea == "a":
    print('Enter the loan principal:')
    P = float(input())
    print('Enter the number of periods:')
    n = float(input())
    print('Enter the loan interest:')
    linterest0 = float(input())
    interest1 = linterest0 / (12 * 100)
    x = interest1 * math.pow((1 + interest1), n)
    y = math.pow((1 + interest1), n) - 1
    gheboasa = P * (x / y)
    serparoasa = math.ceil(gheboasa)
    print('Your monthly payment = {}!'.format(serparoasa))
