def find_common_participants(string1, string2, division=','):
    string1 = set(string1.split(division))
    string2 = set(string2.split(division))
    result = list(string1.intersection(string2))
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
