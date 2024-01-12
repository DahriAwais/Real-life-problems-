trans = input("enter your transportation vehicle , bus , train , car or more ;; ").lower()
des = input("enter your destination Hyderabad , hala , nawabshah ;; ").lower()
status = input("enter your traveling status luxary  or not luxary:: ").lower()

price = 0
def transportation():
    global trans
    global price
    if trans == "bus":
        price = 700
    elif trans == "train":
        price = 2000
    elif trans == "car":
        price = 5000
    else:
        price = 6000
    return price

    
price1 = 0
distance = ()
def destination():
    global des 
    global price1
    global distance 
    if des == "Hyderabad":
        price1 = 200
        distance = "80kms"
    elif des == "hala":
        price1 = 400
        distance = "100kms"
    elif des == "nawabshah":
        distance = "50"
        price1 = 100
    return price1,distance

price3 = 0
def trans_status():
    global status 
    global price3
    if status == "not luxary":
        price3 = price + price1 + 500
    elif status == "luxary":
        price3 = price + price1 + 1000
    else:
        price3 = price + price1 + 100

transportation()
destination()
trans_status()

print(f"your travel vehicle price is {price}")
print(f"your destination distance is {distance}")
print(f"your destination fee is {price1}")
print(f"your travelling status is {status}")
print(f"your total price is {price3}")