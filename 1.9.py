time=int(input('enterb time'))
entry=list(map(int(input('enter list of entries').split())))
exi=list(map(int(input('enter list of exits').split())))
if(time,entry,exi <0):
    print('please enter a positive value')

present=0
total_guests=0
for i in range(time):
    Present+=entry[i]-exit[i]
    if Total_guests<present:
        Total_guests=present
print(Total_guests,end=' ')
