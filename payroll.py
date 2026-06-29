# a bored turtle often leaves the shell 
import time 

pay_rate = 30.00 #sarting pay rate 
employee = input("enter the employee name:   ")
start_time = time.time()
input("enter to clock out:  ") 
end_time = time.time()
hours_worked = (end_time - start_time) / 3600 #converts seconds into hours 
print(f'{employee} worked for {hours_worked:.2f} hours and earned ${hours_worked * pay_rate:.1f}')

#write to file 
with open("payroll.txt", "w",)as f:
    f.write(f'YOU RECIEVED A DIRECT DEPOSIT OF\n{hours_worked * pay_rate:.1f}$')
