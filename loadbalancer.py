import random

f = open('load.txt','r')
servers = []
lines = f.readlines()

for line in lines:
	if line[-1]=='\n':
		s = line[0:-1:1].split(',')
	else:
		s = line.split(',')
	s = map(int,s)
	servers.append(s)

print servers
weight = [s[-1] for s in servers]
total_weight = sum(weight)
print total_weight

cum_weight = weight[:]
print cum_weight

for i in range(1,len(cum_weight)):
	cum_weight[i] += cum_weight[i-1]

print cum_weight

rand = random.randint(0,total_weight-1)
print rand

i = 0
while i < len(cum_weight):
	if(rand<cum_weight[i]):
		break
	i += 1

print i+1