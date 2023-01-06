import time 

while True:
        sec= 0 # секунди
        min = 0 # хвилини
        hour = 0 # години 
        
        time_user = int(input("Введіть кількість секунд: "))
        comment = str(input("Введіть назву: "))
        for q in range(time_user):
            time.sleep(1)
            sec += 1
        print ( sec, "Секунд пройшло:" )
        if(sec % 60) == 0:
            min += 1
        print ( min, "Хвилин пройшло:")
        if(min % 3600) == 0:
            hour +=1
        print ( hour, "Годин пройшло:")

print("Час вийшов!")