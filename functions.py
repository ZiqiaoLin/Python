items = ["Mic","Phone",323.12,3123.123,"Justin","Bag","Cliff Bars",134]

str_items=[]
num_items=[]

for i in items:
	if isinstance(i,float) or isinstance(i,int):
		num_items.append(i)
	elif isinstance(i,str):
		str_items.append(i)
	else:
		pass

print(str_items)
print(num_items)


def parse_lists(some_list):
    str_list_items = []
    num_list_items = []

    for i in some_list:
        if isinstance(i,int) or isinstance(i,float):
            num_list_items.append(i)
        elif isinstance(i,str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items

print(parse_lists(items))

item2 = ["Mic",'Jason',['apple',1234,'Banada']]
print(parse_lists(item2))


sum = [123,323,423]
def my_sum(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i,int) or isinstance(i,float):
            total += i
        else:
            pass
    return total

print("-------------------------")
print( my_sum(items))
print("-------------------------")

def my_average(my_num_list):
    total = 0
    average = 0
    length = 0
    for i in my_num_list:
        if isinstance(i,int) or isinstance(i,float):
            total += i
            length += 1
            print(length)
            print(total)
    average = total/length
    return average

print(my_average(items))
print("-------------------------")