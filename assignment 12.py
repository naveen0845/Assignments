#sum of the dict

dict={"a":10,"b":20,"c":30}
print(dict)
add=sum(dict.values())
print("sum of the values",add)



#accessing elements

dict={"ten":10,
           "fifty":50,
           "twenty":20}
print(dict["ten"])
print(dict["fifty"])



#concate dict

first_dict={"a":10,"b":20,"c":30}
second_dict={"d":40,"e":50}
print(first_dict)
print(second_dict)
first_dict.update(second_dict)
print(first_dict)



#add keys/values in dict

dict={"a":1,"b":2,"c":3}
dict["d"]=4
dict["e"]=5
print(dict)




#length of dict

dict={"one":1,"two":2,"three":3}
print(len(dict))



#to remove items from dict

dict={"a":5,"b":55,"c":555}
dict.pop("b")
print(dict)