bonus = 1000


#core requirements
# with open("hr_system.txt") as hr_list:
#     for data_set in hr_list:
#         clean_line = data_set.strip()
#         parts = clean_line.split()
#         name = parts[0]
#         title = parts[2]
#         print(f"Name: {name}, Title: {title}")

#stretch chalange
with open("hr_system.txt") as hr_list:
    for data_set in hr_list:
        clean_line = data_set.strip()
        parts = clean_line.split()
        name = parts[0]
        id = int(parts[1])
        title = parts[2]
        salary = int(parts[3])
        bonus = 1000

        monthly_s = (salary / 12) / 2
        if title.lower() == "engineer":
            bonus_pay = monthly_s + bonus
            print(f"{name} (ID: {id}) {title} - monthly: ${bonus_pay:.2f}")
        else:
            print(f"{name} (ID: {id}) {title} - monthly: ${monthly_s:.2f}")

       