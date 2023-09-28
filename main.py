class M:
    nullish = 0
    jan = 31
    fev = 28
    fevBi = 29
    mar = 31
    april = 30
    may = 31
    june = 30
    july = 31
    aug = 31
    sept = 30
    octo = 31
    nov = 30
    dec = 31

    months = [nullish, jan, fev, mar, april, may, june, july, aug, sept, octo, nov, dec]
    monthsBi = [nullish, jan, fevBi, mar, april, may, june, july, aug, sept, octo, nov, dec]

    def _sum(arr):
        sum = 0
        for i in arr:
            sum = sum + i
        return(sum)


day = int(input('type day here: '))
month = int(input('type month here: '))
isBisext = int(input('Confirm: This is a bisext year? Confirm with 1 | Deny with 0: '))


if day <= 31 and month <= 12:
    if isBisext == 1:
        monthArr = M.monthsBi[0:month+1]
        monthSum = M._sum(monthArr)
        totalDays = monthSum + day
        print(totalDays)
    elif isBisext == 0:
        monthArr = (M.months[0:month+1])
        print(monthArr)
        monthSum = M._sum(monthArr)
        print(monthSum)
        print(day)
        totalDays = monthSum + day
        print('is the', totalDays,'º day of the year')
    
        
        
        

