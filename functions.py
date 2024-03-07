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