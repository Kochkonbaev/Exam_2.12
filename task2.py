some_text = '''
Advertising companies say advertising is
 necessary and important. It informs 
 people about new products. Advertising 
 hoardings in the street make our 
 environment colorful. And adverts on TV 
 are often funny. Sometimes they are 
 mini-dramas and we wait for the next 
 program in the mini-drama. Advertising 
 can educate, too. Adverts tell us about 
 new, healthy products. And adverts in 
 magazines give us ideas for how to look 
 prettier, be fashionable and be 
 successful. Without advertising, life is 
 boring and colorless.

But some consumers argue that 
advertising is a bad thing. They say that 
advertising is bad for children. Adverts 
make children ‘pester’ their parents buy 
things for them. Advertisers know we 
love our children and want to give them 
everything. So they use children’s ‘pester 
power’ to sell their products. Finally, 
consumers say, if there is advertising 
there must be rules. Some adverts
 advertise unhealthy things like cigarettes 
 and make people waste their money.
'''

word_s = 0
word_t = 0
advert = []
# for i in str.lower(some_text):
# это если все буквы посчитать и большие, и маленькие

for i in some_text.lower():
    if i == 's':
        word_s += 1
    elif i == 't':
        word_t += 1
    else:
        continue
some_text = some_text.replace('advert', 'ADVERT')
print(some_text)

# for i in some_text:
#     advert.append(i)
#     if i == 'adverts':
#         advert.append(str.replace(i))


print(word_t)
print(word_s)
# print(advert)
# print(some_text)