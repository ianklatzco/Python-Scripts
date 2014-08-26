#!/usr/bin/python

# A friend of mine had an assignment, a notebook, for a Creative Writing class. He likes numbers (he's a stats kinda guy) 
# so he decided to number the pages with three boxes: one counting up from 1-9, then 0 (not a computer guy, so he doesn't 
# count up from 0); one of pi sequentially, and one of e sequentially.

# I googled the numbers and made of the 1 thru 0 with some copypasting. Then ran em thru a for loop with a cpx (comparison of equality) (I like acronyms).


pi = "3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306"
e = "27182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"
onetonine = "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"

for x in range(1, 101):
	if pi[x] == e[x] and e[x] == onetonine[x]:
		print "On page "+str(x)+", the numbers will cross at "+pi[x]+e[x]+onetonine[x]+"."

# tidbits from when i was trying to figure it out
# evar = str(math.e)
# enopd = evar.replace(".", "")
# print evar
# print evar[5]
# print enopd