#ฟังก์ชันคำนวณภาษี
def calculate_tax(net_income):
    tax = []
    remain_net = net_income
    total_tax  = 0

    #ขั้นที่ 1
    if  net_income >= 150000: 
        remain_net = net_income - 150000
        tax.append(0)
    else:
        tax.append(0)
        remain_net -= remain_net

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

    #รวมภาษี
    for money in tax:
        total_tax += money

    #รายได้หลังหักภาษี
    after_tax_income = net_income - total_tax

    #คำนวณอัตราภาษีที่แท้จริง
    if net_income == 0:
        effective_tax_rate = 0
    else:
        effective_tax_rate = (total_tax / net_income) * 100

    return  tax, total_tax, after_tax_income, effective_tax_rate


#ฟังก์ชันแสดงรายลละเอียดภาษี
def show_tax_detail(tax, total_tax, after_tax_income, effective_tax_rate):
    print("=" * 55)
    print(f"{'รายละเอียดภาษี':^55}")
    print("=" * 55)


    #ขั้นที่ 1
    if  net_income > 150000:
        print(f"{'0 - 150,000':<30}:  {format(tax[0],',.0f')} บาท")
    else:
        print(f"0 - {format(net_income,','):<20}:  {format(tax[0],',.0f')} บาท")


    #ขั้นที่ 2
    if tax[1] != 0:
        if net_income > 300000:
            print(f"{'150,001 - 300,000':<30}:  {format(tax[1],',.0f')} บาท")
        else:
            print(f"150,001 - {format(net_income,','):<20}:  {format(tax[1],',.0f')} บาท")
    

    #ขั้นที่ 3
    if tax[2] != 0:
        if net_income > 500000:
            print(f"{'300,001 - 500,000':<30}:  {format(tax[2],',.0f')} บาท")
        else:
            print(f"300,001 - {format(net_income,','):<20}:  {format(tax[2],',.0f')} บาท")
    

    #ขั้นที่ 4
    if tax[3] != 0:
        if net_income > 750000:
            print(f"{'500,001 - 750,000':<30}:  {format(tax[3],',.0f')} บาท")
        else:
            print(f"500,001 - {format(net_income,','):<20}:  {format(tax[3],',.0f')} บาท")


    #ขั้นที่ 5
    if tax[4] != 0:
        if net_income > 1000000:
            print(f"{'750,001 - 1,000,000':<30}:  {format(tax[4],',.0f')} บาท")
        else:
            print(f"750,001 - {format(net_income,','):<20}:  {format(tax[4],',.0f')} บาท")

    

    #ขั้นที่ 6
    if tax[5] != 0:
        if net_income > 2000000:
            print(f"{'1,000,001 - 2,000,000':<30}:  {format(tax[5],',.0f')} บาท")
        else:
            print(f"1,000,001 - {format(net_income,','):<20}:  {format(tax[5],',.0f')} บาท")
    

    #ขั้นที่ 7
    if tax[6] != 0:
        if net_income > 5000000:
            print(f"{'2,000,001 - 5,000,000':<30}:  {format(tax[6],',.0f')} บาท")
        else:
            print(f"2,000,001 - {format(net_income,','):<20}:  {format(tax[6],',.0f')} บาท")


    #ขั้นที่ 8    
    if tax[7] != 0:
        print(f"{'มากกว่า 5,000,000':<31}:  {format(tax[7],',.0f'):} บาท")

    #แสดง ภาษีรวม,รายได้หลังหักภาษี และ Effective Tax Rate
    print("=" * 55)
    print(f"{'ภาษีรวม':<31}:  {format(total_tax,',.0f')} บาท")
    print(f"{'รายได้หลังหักภาษี':<34}:  {format(after_tax_income,',.0f')} บาท")
    print(f"{'Effective Tax Rate':<30}:  {format(effective_tax_rate,',.2f')} %")
    print("=" * 55)

#รับค่าเงินได้สุทธิจากผู้ใช้
net_income = int(input("กรอกเงินได้สุทธิ : "))

tax, total_tax, after_tax_income, effective_tax_rate = calculate_tax(net_income)

show_tax_detail(tax,total_tax,after_tax_income,effective_tax_rate)