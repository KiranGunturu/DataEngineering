#-----------
# tom_exp_list=[2100, 3400, 3500]
# joe_exp_list = [200, 500, 700]
#
#
# total=0
#
# for exp in tom_exp_list:
#     total=total+exp
# print("total tom exp is:", exp)
#
# for joeexp in joe_exp_list:
#     total=total+joeexp
#
# print("total joe exp is:", joeexp)

#--------------


def calculator(exp):
    total=0
    for item in exp:
        total=total+item
    return  total


tom_exp_list=[2100, 3400, 3500]
joe_exp_list = [200, 500, 700]


tom_total=calculator(tom_exp_list)
joe_total=calculator(joe_exp_list)


print("tom total is:",tom_total)
print("joe total is:",joe_total)