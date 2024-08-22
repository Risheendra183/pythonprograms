import statistics
def me_med_mod(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
a,b,c=me_med_mod([7,7,9,5,4,7,8])
print(f"mean:{a}\nmedian is {b},mode is {c}")

def dayss(year,mon):
    days_list=[31,28,31,30,31,30,31,30,31,30]
    
