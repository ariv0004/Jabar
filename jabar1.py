inListX =[15,12,8,8,7,7,7,6,5,3]
inListY = [10,25,17,11,13,17,20,13,9,15]

meanX = (sum(inListX)/len(inListX))
meanY = (sum(inListY)/len(inListY))

sumXsquare, sumYsquare, sumXY = 0.0, 0.0, 0.0

for x,y in zip(inListX, inListY):
    sumXsquare += (x - meanX)**2
    sumYsquare += (y - meanY)**2
    sumXY += (x - meanX) * (y - meanY)

r = sumXY / ((sumXsquare**(.5)) * (sumYsquare**(.5)))
print("%.3f" % round(r,3))
