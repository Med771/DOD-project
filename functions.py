from openpyxl import load_workbook

def check_regist(id_number: str) -> bool:
    with open("Id_numbers.txt", "r") as file:
        arr = tuple(map(lambda x: x.strip(), file.readlines()))

    return id_number not in arr

def append_id_number(id_number: int) -> None:
    with open("Id_numbers.txt", "a") as file:
        file.write(f"{id_number}\n")

def append_full_info_in_xlsx(info_user: list[str]) -> None:
    fn = "Data.xlsx"
    wb = load_workbook(fn)
    ws = wb["Data"]

    ws.append(info_user)
    wb.save(fn)
    wb.close()

def check_name(query: str) -> bool:
    try:
        name, surname = query.split()

        if name.isalpha() and surname.isalpha():
            return True

        return False
    except:
        return False

def check_num_phone(query: str) -> bool:
    try:
        query = query.strip(",./ +")
        if query.isdigit() or query[1:].isdigit():
            if len(query) == 11 and (query[0] == "8" or query[0] == "7"):
                return True

        return False
    except:
        return False

def check_school(query: str) -> bool:
    try:
        school, number = query.split()

        if school.capitalize() in ["Лицей", "Школа", "Гимназия"] and int(number.strip("№ ,.")):
            return True
    except:
        return False

def check_class(query: str) -> bool:
    try:
        if 0 < int(query) < 12:
            return True
        else:
            return False
    except:
        return False
