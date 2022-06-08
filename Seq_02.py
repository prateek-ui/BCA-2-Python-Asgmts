# Write a program to calculate simple interest on the basis of the principal amount, rate of interest, duration in years
p,r,t=int(input('Enter principal: ')),int(input('Enter roi: ')),int(input('Enter tenure: '))
print((p*r*t)//100)