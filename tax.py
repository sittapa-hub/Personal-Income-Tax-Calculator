net_income = int(input("กรอกเงินได้สุทธิ : "))

if  net_income >= 0 and net_income <= 150000: #ขั้นที่ 1
    remain_net = net_income - 150000

if net_income >= 150001 and net_income <= 300000: #ขั้นที่ 2
    remain_net = remain_net - 150000

if  net_income >= 300001 and net_income <= 500000: #ขั้นที่ 3
    remain_net = remain_net - 200000

if  net_income >= 500001 and net_income <= 750000: #ขั้นที่ 4
    remain_net = remain_net - 250000

if  net_income >= 750001 and net_income <= 1000000: #ขั้นที่ 5
    remain_net = remain_net - 250000

if  net_income >= 100001 and net_income <= 2000000: #ขั้นที่ 6
    remain_net = remain_net - 1000000

if net_income >=
