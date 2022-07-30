def vowalorcons(ch):

    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'
    or ch=='A'or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
         return "vowal"

    if ch >= 'a'and ch <= 'z':
         return "\n consonant"
    if ch >= 'A' and ch <= 'Z': 
         return "\n consonant"

    else: 
         return "somthing else"

print(vowalorcons('P'))        