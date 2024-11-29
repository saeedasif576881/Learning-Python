t_bill = 124.54
tip = 12 
people = 5 

t_tip = t_bill * (tip/100);
t_bill +=t_tip
bill = t_bill/people

total =round(( (t_bill + t_tip)/people),2)
print(total)

print(t_bill + t_tip)
bill = round(bill,2)
print(bill) 