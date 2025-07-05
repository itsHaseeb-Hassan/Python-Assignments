studentName = input("Enter student name: ")
rollNumber = input("Enter roll number: ")
studentClass= input("Enter student class: ")
monthlyFee = int(input("Enter monthly fee: "))
numberOfMonthsPaid = int(input("Enter number of months paid: "))

totalFee = monthlyFee * numberOfMonthsPaid

remainingBalance = monthlyFee * (12 - numberOfMonthsPaid)

print(f"----------    Fee Receipt    ----------")
print(f"Student Name:               {studentName}")
print(f"Roll Number:                {rollNumber}")
print(f"Class:                      {studentClass}")
print(f"Monthly Fee:                {monthlyFee}")
print(f"Months Paid:                {numberOfMonthsPaid}")
print(f"Total Paid:                 {totalFee}")
print(f"Remaining Balance:          {remainingBalance}")
print("--------------------------------------")


# Display voucher
print("\n" + "="*40)
print("         School System")
print("         Student Fee Voucher")
print("="*40)
print(f"Student Name     : {studentName}")
print(f"Roll Number      : {rollNumber}")
print(f"Class            : {studentClass}")
print("-"*40)
print(f"Monthly Fee      : Rs. {monthlyFee}")
print(f"Months Paid      : {numberOfMonthsPaid}")
print(f"Total Paid       : Rs. {totalFee}")
print(f"Remaining Balance: Rs. {remainingBalance}")
print("="*40)
print("        Thank you for your payment!")
print("="*40)



