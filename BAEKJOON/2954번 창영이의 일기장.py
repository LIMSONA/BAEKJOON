# #실패------------------------------------------
# import re
# text=input()
# p=re.compile("(a|e|i|o|u)p(?=(a|e|i|o|u))")
# m=p.sub("",text)
# print(m)


#성공--------------------------------------------
import re
text=input()
m=re.sub('(a|e|i|o|u)p(a|e|i|o|u)','\\1',text)
print(m)