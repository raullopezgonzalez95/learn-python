num = 1234567890

def invertir(num):
    resp = ""
    i = len(str(num)) - 1

    while i >= 0:
        resp += str(num)[i]
        i -= 1
    
    return resp

invertir(num)
