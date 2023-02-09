def isnumeric(s):
    s=s.strip()
    try:
        s=float(s)
        return True
    except:
        return False
n=input('enter the valid number')
print(isnumeric(n))
