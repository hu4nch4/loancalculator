import math
import argparse

# Aici e partea in care le scrii
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"],
                    help="Incorrect parameters")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

# Aici e un kkt ca sa mearga sa le dai assign la o variabila
args = parser.parse_args()

# Aici de dai assign la cate o variabila
type = args.type

payment = args.payment
if payment is not None:
    payment = float(payment)

interest = args.interest
if interest is not None:
    interest = (float(args.interest)) / (12 * 100)

periods = args.periods
if periods is not None:
    periods = int(periods)

principal = args.principal
if principal is not None:
    principal = float(principal)

#PRINTURI AICI
#print("Aici e payment "+str(payment))
#print("Aici e interest rate "+str(interest))
#print("Aici sunt lunile "+str(periods))
#print("Aici e loanprincipal "+str(principal))
#("")
# Aici verifici cacaturile alea de la inceput ( 3 )

num_params = sum(arg is not None for arg in vars(args).values())
if num_params < 4:
    print("Incorrect parameters")
    exit()

if type is None:
    print('Incorrect parameters')

else:
    if (type == "diff" and payment is not None) or (type == "diff" and interest is None):
        print("Incorrect parameters")
        exit()
    elif (payment is not None and payment < 0) or (periods is not None and periods < 0) or (
            interest is not None and interest < 0) or (principal is not None and principal < 0):
        print("Incorrect parameters")
        exit()

#Un array cu numarul lunii
periods_array = []
while (periods is not None) and (periods > 0):
    periods_array.append(periods)
    periods -= 1
periods_array.reverse()
periods = len(periods_array)
#PRINT AICI
#print(periods_array)
#print("")

#1, 2
gaoz = 0
if type == "diff":
    if payment is None:
        for x in periods_array:
            lego1 = principal / periods
            lego2 = (principal * (x - 1)) / periods
            final = lego1 + interest * (principal - lego2)
            final = math.ceil(final)
            gaoz = gaoz + final
            final = str(final)
            payment = str(x)
            print("Month "+ payment +": payment is "+final)
        finalal = str(int(gaoz - principal))
        print("Overpayment = "+finalal)


elif type == "annuity":
    if principal is None:
        # print(periods)
        # print(interest)
        j1 = 1 + interest
        j2 = math.pow(j1, periods)
        j3 = interest * j2
        j4 = j2 - 1
        j5 = j3 / j4
        principal = math.floor(payment / j5)
        a1 = 1 + interest
        a2 = math.pow(a1, periods)
        a3 = interest * a2
        a4 = math.pow(a1, periods) - 1
        a5 = interest * a2
        a6 = math.ceil(principal * a5 / a4)
        overpayment = int(a6 * periods - principal)
        print("Your loan principal: " + str(principal)+"!")
        print("Overpayment = "+str(overpayment))
    elif payment is None:
        annuity_payment = principal * (interest * (1 + interest) ** periods) / (
                    (1 + interest) ** periods - 1)

        annuity_payment = math.ceil(annuity_payment)
        print("Your annuity payment =", annuity_payment)
        overpayment = (periods * annuity_payment) - principal
        print("Overpayment = "+str(round(overpayment)))
    elif periods == 0:
        periods = None
        x = payment / (payment - interest * principal)
        n = round(math.log(x, 1 + interest))
        periods = n
        #print(periods)
        #print("ajutor")
        years = round(periods / 12)
        print("It will take", years, "years to repay this loan!")
        print("Overpayment = "+str(round((periods * payment) - principal)))

