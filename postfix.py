#!/usr/bin/env python3

def eval_expr(s,d={}):
    arg=s.split()
    zas=[]
    
    for item in arg:
        if item in ("+","-","*","/"):
            if item=="+":
                zas.append(zas.pop()+zas.pop())
            elif item=="-":
                zas.append(zas.pop(0)-zas.pop())
            elif item=="*":
                zas.append(zas.pop()*zas.pop())
            elif item=="/":
                zas.append(zas.pop(0)//zas.pop())
        elif item.isdigit():
            zas.append(int(item))
        else:
            zas.append(d[item])

    return zas[0]
