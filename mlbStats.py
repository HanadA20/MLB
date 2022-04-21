atBats = "455,597,548,565,582,433,260,545,608,633,606,520,364,197,166,300,491,428,528,490,387,98".split(',')
atBats = list(map(int,atBats))#convert list of strings to list of ints

hits = "120,179,179,174,180,140,67,165,185,180,173,141,104,52,41,76,148,108,146,122,83,18".split(',')
hits = list(map(int,hits))

doubles = "23,28,42,39,38,24,7,26,34,33,26,22,20,8,12,18,30,19,24,30,19,2".split(',')
doubles = list(map(int,doubles))

totalBases = "191,287,289,302,359,292,125,342,33,387,349,289,194,84,94,154,283,208,262,208,159,20".split(',')
totalBases = list(map(int,totalBases))

rbi = "61,80,100,103,109,90,42,140,147,146,134,118,65,23,26,60,92,72,93,71,57,7".split(',')
rbi = list(map(int,rbi))

mvpVotes = "19,9,17,5,2,4,1,4,10,24".split(',')
mvpVotes = list(map(int,mvpVotes))

#1 Getting Batting Average (hits/atBats)

total = 0

for i in range(0,len(atBats)):
    total += (hits[i]/atBats[i])

battingAvg = total / len(atBats)

print(format(battingAvg,".3f"))


#2 Slugging = totalBases/atBats

total = 0

for i in range(0,len(atBats)):
    total += (totalBases[i]/atBats[i])

slugging = total / len(atBats)

print(format(slugging,".3f"))



#3 List Top 3 RBI Seasons

rbi.sort()
print(f'Top 3 are {rbi[-1]}, {rbi[-2]}, {rbi[-3]}')




#4 What was the percentage of his career, did Ken hit at least 25 doubles in a season?

times = 0

for nums in doubles:
    if(nums >=25):
        times+=1

print(format(times/ len(doubles)* 100, '.2f' ) + "% of doubles in Ken's career are at least 25")


#5 During his 22-year career, Ken was in the MVP voting 10 times. Out of those times, how many did he place in the top 5?

times = 0
for place in mvpVotes:
    if place <= 5:
        times +=1


print(times)


