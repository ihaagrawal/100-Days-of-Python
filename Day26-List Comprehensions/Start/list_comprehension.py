numbers=[1,2,3,4]
new_list=[n+1 for n in numbers]
print(new_list)

name = "Angela"
letter_list=[letter for letter in name]
print(letter_list)

range_number=[n*2 for n in range(1,5)]
print(range_number)

names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
short_list=[sn for sn in names if len(sn)<5]
print(short_list)


cap_list=[sn.upper() for sn in names if len(sn)>4]
print(cap_list)