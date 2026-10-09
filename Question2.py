"""
Question 2: Online Mobile Store 
An online store maintains a list of mobile prices. Write a function 
to display all mobiles costing more than ₹20,000, calculate the 
total inventory value, and find the most expensive mobile price. 

"""

mobile_price=[5000,23000,23500,19000,21000,15000]
def cost20k(mobile_price):
    expansive_mobile=max(mobile_price)
    total_inventry_value=sum(mobile_price)
    mobile20k=[i for i in mobile_price if i>20000]
    
    return{
        "expensive mobile":expansive_mobile,
        "total inventory value":total_inventry_value,
        "mobiles cost>20k":mobile20k
    }

result=cost20k(mobile_price)
print(result)