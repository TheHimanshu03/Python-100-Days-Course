str = "My name is {} and I am from {}"
country = "India"
name = "Himanshu Aggarwal"

print(str.format(name, country))



str2 = "My name is {1} and I am from {0}"
counntry = "India"
naame = "Himanshu Aggarwal"

print(str2.format(counntry, naame)) 

#----using F Strint---

name1 = "Himanshu"
country1 = "India"
language = "python"
print(f"My name is {name1} and I am from {country1} and I am learning the {language} language")


price = 61000.9876
print(f"the price of BitCoin is : {price: .2f}$")  #.2f is calculate the value upto 2 decimal places only


print(f"{2*30}")
print(type(f"{2*30}"))