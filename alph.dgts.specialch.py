def alphadigitspecialsymbol(ss):
    if ss >= 'a'and ss<= 'z':
         return "\nIt is an alphabet"
    if ss >= 'A' and ss <= 'Z': 
         return "\nIt is an a\tlphabet"

    if ss>='0' or ss==('inf'):
     return "\n digit "
    else:
     return "\n some special symbol"     

print(alphadigitspecialsymbol(''))
