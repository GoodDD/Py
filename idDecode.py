from datetime import datetime, date


def decode(idcode):
    ik=str(idcode) 
    Names=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Dec"] 
    Day=ik[5:7] 
    Month=ik[3:5] 
    YearEnd=ik[1:3] 
    if ik[0]=="1" or ik[0]=="2": 
        Year=1800+int(YearEnd) 
    elif ik[0]=="3" or ik[0]=="4": 
        Year=1900+int(YearEnd) 
    else: 
        Year=2000+int(YearEnd)
    YearDays = 365 
    birthday = date(year = int(Year), month = int(Month), day = int(Day)) 
    age = int((date.today() - birthday).days / YearDays)
    print("Person with id: " +str(idcode)+ " Was born in:",int(Day),Names[int(Month)-1],Year, "Year", ",", "Age:", age, "years")




f = open("idList.txt", "r")
for line in f:
    decode(line)


