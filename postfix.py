#!/usr/bin/env python3

def eval_expr(s,d={}):
    arg=s.split()
    zas=[]
    
    for item in arg:
        if item in ("+","-","*","/"):
            if item=="+":
                zas.append(zas.pop(-2)+zas.pop())
            elif item=="-":
                zas.append(zas.pop(-2)-zas.pop())
            elif item=="*":
                zas.append(zas.pop(-2)*zas.pop())
            elif item=="/":
                zas.append(zas.pop(-2)//zas.pop())
        elif item.isdigit():
            zas.append(int(item))
        else:
            zas.append(d[item])

    return zas[0]

def to_infix(s):
    arg=s.split()
    zas=[]

    for item in arg:
        if item=="+":
            zas.append( "( " + zas.pop(-2) + " + " + zas.pop() + " )" )
        elif item=="-":
            zas.append( "( " + zas.pop(-2) + " - " + zas.pop() + " )" )
        elif item=="*":
            zas.append( "( " + zas.pop(-2) + " * " + zas.pop() + " )" )
        elif item=="/":
            zas.append( "( " + zas.pop(-2) + " / " + zas.pop() + " )" )
        else:
            zas.append(item)
    return zas[0]
