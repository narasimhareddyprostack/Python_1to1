#create 
price=399
rating=4.5
product_Name="GAP"
is_discount=True 
c=10+20j

colors=['Red','Blue','Black']
pids=(101,102,103,104)
coupon_ids={333,444,333,444}  #duplicates are not allowed
product_details={
    'pid':101,
    'pname':"Mens Check Shirt"
}

b=bytes([0,10,20,255])
ba=bytearray([0,10,20,30,255])
fz=frozenset({10,10,10})
seq=range(100)
n=None 

#read type
print(type(price))
print(type(rating))
print(type(product_Name))
print(type(is_discount))
print(type(c))
print(type(colors))
print(type(pids))
print(type(coupon_ids))
print(type(product_details))
print(type(b))
print(type(ba))
print(type(fz))
print(type(seq))
print(type(n))