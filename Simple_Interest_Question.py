principal = 10000
rate = 0.06
term = 5
totalinterest = 0

for year in range(1, term+1):
    print(f"Year [year]: ${principal}")
    interest = principal + rate
    print(f"Interest Earned: ${interest}")
    principal = principal + interest
    totalinterest = totalinterest + interest

print(f"Total interest earned: ${totalinterest}");
print(f"Final Principal after {term} years: ${principal}");
