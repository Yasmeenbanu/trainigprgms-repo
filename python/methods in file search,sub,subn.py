#search method
import re
str="rohan is rama is klma id tryijktrhjmn "
pattern="ram*"
res=re.search(pattern,str)
print(res)

#match method
import re
str="rohan is rama is klma id tryijktrhjmn "
pattern="ram*"
res=re.match(pattern,str)
print(res)

#findall
import re
str="rohan is rama is klma id tryijktrhjmn "
pattern="ram*"
res=re.findall(pattern,str)
print(res)
for data in res:
    print(data)
#sub
import re
str="rama89sita99ravana100"
pattern="[0-9]+"
replace="@"
res=re.sub(pattern,replace,str)
print(res)
#subn
import re
str="rama89sita99ravana100"
pattern="[0-9]+"
replace="@"
res=re.subn(pattern,replace,str)
print(res)

