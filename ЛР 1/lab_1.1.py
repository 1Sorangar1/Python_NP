numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

None_number = 4

average = (sum(numbers[:slide])+sum(numbers[(slide+1):]))/(len(numbers))
numbers[slide] = average
print("Измененный список:", numbers)
