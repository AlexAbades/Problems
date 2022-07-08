# First algorithm to get used to code judge 
# The three siblings Anna, Laura, and Oscar, just got their Christmas presents. Anna gets jealous if both Laura and Oscar has more 
# presents than her. Laura gets jealous if Anna has more presents than her, and Oscar gets jealous if Anna or Laura (or both) has more
# presents than him

an, la, os = list(map(int, input().split()))
jealous = []

if la > an and os > an:
    jealous.append('Anna')
if an > la:
    jealous.append('Laura')
if an > os or la > os:
    jealous.append('Oscar')
if not jealous:
    jealous.append(None)

for i in jealous:
    print(i)


#%% 
# Solution 2
A, L, O = map(int, input().split())
found = False

if A < L and A < O:
	print("Anna")
	found = True
if L < A:
	print("Laura")
	found = True

if O < A or O < L:
	print("Oscar")
	found = True

if not found:
	print("NONE")