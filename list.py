# list is a mutable collection of items.
    # mutable
    # orderes 
    # indexed
    # anydata type 
    # mix of datatype
    # duplicat allowed


# `list= [10,20,800,40,50]

# # normal operation
#             print(list)  # print list with []
#             print(len(list)) #length of list
#             print(type(list))  # type of list
#             print(list[0])  #first element of list
#             print(list[-1])  # last element of list
#             print(list[:])   # slice of list  - all elemet 

# slic f list in details
        # print(list[0:4]) #print alll eleement in list
        # print(list[-1:])  # only print last element of list
        # print(list[0::2])
        # print(list[:])
        # print(list[::-1])
        # print(list[0:len(list)-1:2]) # print all the element of list except last one


# operation on list
#  1. add element to list(append , insert and extend/+ operator)

          
            # list.append(6) #add element in the end of the list
            # print(list)
            # list.insert(0,20) #add element at a particular index 
            # print(list)
            # list.extend([7,8,9]) # or new_list = [7,8,9]  -> list.extend(new_list)   #modify list by adding multiple element at the end of the list 7,8
            # list +=[7,8,9] # list  = list +[7,8,9]  both are work differently  list+= modify the list but list  = list+ [7,8,9] create a new list instead of ,odifying the existiong a list 
            # print(list)
  #note🚩:- append and insert ( but can add mutliple item ex - list.append([6,6]))add only one element at a time but extend and + operator  can add multiple item in a  list           



# 2.remove element from list (remove, pop,del and clear )
            # print(list)
            # list.remove(30)   # remove element by value but it will return none
            # print(list)
            # print(list.pop(0)) # remove element by index and it will return the removed element and if we don't pass any index it will remove the last element of the list
            # print(list)

            # del list[1] #del is  a instruction not a method remov eelement by index  ,,,, it eill remove 4 th element 
            # print(list)
            # del list # it will delte the entire list
            # print(list)  # give name erroe because list is delteed(but here its give type of lsit because we use name list so it take as a buit in name of list)
            # list.clear()

#3. checking the existance of a list element(index/ in operator)


        # print(list.index(20))    #it will return of the first occurence of element and is value not found it will  give  valure error
        # print(70 in list)       #it will retuen true if element is found otherwise false

#4.  count the number of occurenc in a lst(count)
            # list.extend([10,20,20,20])
            # # print(list)

            # print(list.count(20))    # it  will give the count of the element in the list iif not founf return 0

#5.sort the list(sort)  by default it will sort in ascending order
 # a. ASCENDING ORDER
        # list.sort()  #it will return  nonne but sorted list  it will modify th original list and return none
        # print(list)
 #B. DESCENDING ORDER
        # list.sort(reverse=True)
        # print(list)


#6. reverse theb lsit(reverse)
            # new_list = [10,30,20,50,40]
            # new_list.reverse()   #ir t will reverse the list and return none and it will not sort rthe list in descending order
            # print(new_list)
#7. copy the list(copy) 
            # new_list = list.copy() # it will create a new list with same element   if we modify new list it will not affect original list
            # list.append(80)
            # print(new_list)


# wapto renmove duplicates of a list
lst =[1,2,2,3,4,3,2,5]
print(list(set(lst)))