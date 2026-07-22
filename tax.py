net_income = int(input("กรอกเงินได้สุทธิ : "))
remain_net = net_income
tax = []


#ขั้นที่ 1
if  net_income >= 150000: 
    remain_net = net_income - 150000
    tax.append(0)
else:
    tax.append(0)


#ขั้นที่ 2
if net_income >= 300000: 
    remain_net = remain_net - 150000
    tax.append(150000 * (5/100))
else:
    tax.append(remain_net * (5/100))
    remain_net -= remain_net
    

#ขั้นที่ 3   
if  net_income >= 500000: 
    remain_net = remain_net - 200000
    tax.append(200000 * (10/100))
else:
    tax.append(remain_net * (10/100))
    remain_net -= remain_net

     
#ขั้นที่ 4
if  net_income >= 750000: 
    remain_net = remain_net - 250000
    tax.append(250000 * (15/100))
else:
    tax.append(remain_net * (15/100))
    remain_net -= remain_net


#ขั้นที่ 5
if  net_income >= 1000000: 
    remain_net = remain_net - 250000
    tax.append(250000 * (20/100))
else:
    tax.append(remain_net * (20/100))
    remain_net -= remain_net


#ขั้นที่ 6
if  net_income >= 2000000: 
    remain_net = remain_net - 1000000
    tax.append(1000000 * (25/100))
else:
    tax.append(remain_net * (25/100))
    remain_net -= remain_net


#ขั้นที่ 7
if  net_income >= 5000000: 
    remain_net = remain_net - 3000000
    tax.append(3000000 * (30/100))
else:
    tax.append(remain_net * (30/100))
    remain_net -= remain_net


#ขั้นที่ 8
if net_income > 5000000: 
   tax.append(remain_net * (35/100))
else:
    tax.append(0)
    

print(remain_net)
for i in range(len(tax)):
    print(i,tax[i])