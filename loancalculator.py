import math
print('Enter the loan principal:')
lprincipal = int(input())
print('What do you want to calculate?')
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
wanttocalculate = input()
if wanttocalculate == "m":
    print('Enter the monthly payment:')
    monthlypayment = int(input())
    rezultat = math.ceil(lprincipal / monthlypayment)
    if rezultat != 1:
            print('It will take',rezultat,'months to repay the loan')
    elif rezultat == 1:
            print('It will take',rezultat,'month to repay the loan')
elif wanttocalculate == "p":
    print('Enter the number of months:')
    nrofmonths = int(input())
    rezultat2 = lprincipal / nrofmonths
    verificare = round(rezultat2)
    primele = math.ceil(rezultat2)
    verificare2 = int(lprincipal / primele)
    ultima = lprincipal - (primele * verificare2)
    if verificare - rezultat2 == 0:
        print('Your monthly payment =',verificare)
    elif verificare - rezultat2 != 0:
        string_in_string = "and the last payment = {}.".format(ultima)
        print('Your monthly payment =', primele, string_in_string)