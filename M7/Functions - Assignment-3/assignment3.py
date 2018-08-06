"""# Functions - Assignment-3 - Using Bisection Search to Make the Program Faster

# You'll notice that in Problem 2, your monthly payment had to be a multiple
 of $10. Why did we make it that way? You can try running
# your code locally so that the payment can be any dollar and cent 
amount (in other words, the monthly payment is a multiple of $0.01).
# Does your code still work? It should, but you may notice that your 
code runs more slowly, especially in cases with very large balances
# and interest rates. (Note: when your code is running on our servers,
 there are limits on the amount of computing time each submission
# is allowed, so your observations from running this experiment on the
 grading system might be limited to an error message complaining
# about too much time taken.)

# Well then, how can we calculate a more accurate fixed monthly payment 
than we did in Problem 2 without running into the problem of slow
# code?
# We can make this program run faster using a technique introduced in
 lecture - bisection search!

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# To recap the problem: we are searching for the smallest monthly payment 
such that we can pay off the entire balance within a year. What
# is a reasonable lower bound for this payment value? $0 is the obvious anwer,
 but you can do better than that. If there was no interest,
# the debt can be paid off by monthly payments of one-twelfth of the
 original balance, so we must pay at least this much every month.
# One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly,
 we paid off the entire balance at the end of the year. What we
# ultimately pay must be greater than what we would've paid in monthly
installments, because the interest was compounded on the balance
# we didn't pay off each month. So a good upper bound for the monthly
 payment would be one-twelfth of the balance, after having its
# interest compounded monthly for an entire year.

# In short:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Write a program that uses these bounds and bisection search (for
more info check out the Wikipedia page on bisection search) to find
# the smallest monthly payment to the cent (no more multiples of $10)
such that we can pay off the debt within a year. Try it out with
# large inputs, and notice how fast it is (try the same large inputs
in your solution to Problem 2 to compare!). Produce the same return
# value as you did in Assignment 2."""



def paying_debt_offinayear(balance, annualInterestRate):
    min_month_payment = 0
    monthly_unpaid_balance = 0
    monthly_interest_rate =  annualInterestRate / 12.0
    low_bal = balance / 12.0
    high_bal = (balance * (1 + monthly_interest_rate) ** 12 ) / 12.0
    min_month_payment = (low_bal + high_bal) / 2.0
    while (True):
        rem_balance = balance
        for i in range(0,12):
            monthly_unpaid_balance = rem_balance - min_month_payment
            rem_balance =  monthly_unpaid_balance + (
                monthly_interest_rate * monthly_unpaid_balance)
        if(rem_balance <= 0 and rem_balance >= -0.01):
            break
        else:
            if(rem_balance > 0):
                low_bal = min_month_payment
            else:
                high_bal = min_month_payment
        min_month_payment = (low_bal + high_bal) / 2.0
    return round(min_month_payment, 2) 
def main():
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " +str(paying_debt_offinayear(data[0], data[1])))
    
if __name__== "__main__":
    main()
