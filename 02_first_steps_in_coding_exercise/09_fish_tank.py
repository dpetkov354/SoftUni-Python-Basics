# 9 Fish Tank
length = float(input())
width = float(input())
height = float(input())
percent = float(input())
volume_cm_cubed = float(length * width * height)
volume_liters = float(volume_cm_cubed / int(1000))
used_space = float(percent / int(100))
required_liters = float(volume_liters * float(int(1)-used_space))
print(f'{required_liters} liters of water are needed to fill up the fish tank')