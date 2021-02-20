#import json as js

#    
#    print(products['quantity'])
##obj = json.loads(dater)
##print(obj)

import json as js
with open('mama_mboga_items.json','r') as (a):
    data = js.load(a)

for dub in data["products"]:
 print(dub['item'],dub['price'])
 print(dub['item'],dub['quantity'])
 print(dub['quantity'],dub['price'])