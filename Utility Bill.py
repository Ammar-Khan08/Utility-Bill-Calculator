#Name: Ammar Khan

print("Welcome to the Global Energy bill calculator!")

#Collecting inputs from the user.
AccountNumber = int(input("Enter your account number: "))
Month = int(input("Enter the month number (e.g., for January, enter 1): "))
ElectricityPlan = input("Enter your electricity plan (EFIR or EFLR): ") 
ElectricityAmount = float(input(f"Enter the amount of electricity you used in month {Month} (in kWh): "))
GasPlan = input("Enter your gas plan (GFIR or GFLR): ")
GasAmount = float(input(f"Enter the amount of gas you used in month {Month} (in GJ): "))
Province = input("Enter the abbreviation for your province of residence (two letters): ")

FixedMonthlyFee = 120.62
FixedMonthlyGasFee = 1.32

#Province Tax
if Province == "AB" or "BC" or "MB" or "NT" or "NU" or "QC" or "Sk" or "YT" :
    TaxRate = 5/100
elif Province == "ON" :
    TaxRate = 13/100
elif Province == "NB" or "NL" or "NS" or "PE" :
    TaxRate = 15/100

#Calculate Electricity Bill  
if ElectricityPlan == "EFIR" :
    if ElectricityAmount <= 1000:
        ElectricityBill = (ElectricityAmount * 8.36 )* 0.01
    elif ElectricityAmount > 1000:
        ElectricityBill = (((ElectricityAmount - 1000) * 9.41 ) + (1000*8.36)) * 0.01  
elif ElectricityPlan == "EFLR" :
        ElectricityBill = (ElectricityAmount * 9.11) * 0.01


#Calculate Gas Bill
if GasPlan == "GFIR" :
    if GasAmount <= 950 :
        GasBill = (GasAmount * 4.56 )* 0.01 
    elif GasAmount > 950 :
        GasBill = ((((GasAmount - 950) * 5.89) + (950*4.56)) * 0.01) 
elif GasPlan == "GFLR" :
    GasBill = (GasAmount * 3.93 )* 0.01 

# Calculate the provincial tax according to the Province of the Customer
TotalTax = ((ElectricityBill + GasBill) + FixedMonthlyFee + FixedMonthlyGasFee) * TaxRate

# Calculate the Total Bill Due for the month including all fees + tax
TotalBill = round(((ElectricityBill + GasBill) + FixedMonthlyFee + FixedMonthlyGasFee) + TotalTax, 2)

# Prints the Total Bill Due for the month
print(f"Thank you! Your total amount due now is: ${TotalBill}")
    


