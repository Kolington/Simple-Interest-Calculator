print("Do You Want to Invest Calculate your Profit with This Calculator")
principal = input('Input the Principal: ')
rate = input('Input the Rate: ')
time = input('Input the Time: ')
simple_interest = int(principal) * float(rate) * int(time) / 100
print(simple_interest)