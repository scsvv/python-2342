import openpyxl
from openpyxl.styles import PatternFill


if __name__ == "__main__":
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    headers = ['Name', 'Surname', 'Age', 'Status']
    sheet.append(headers)

    data = [
        ["Ann", "Doe", 12, False],
        ["Ann", "Doe", 12, True],
        ["Ann", "Doe", 12, True],
        ["Ann", "Doe", 12, False],
        ["Ann", "Doe", 12, False],
        ["Ann", "Doe", 12, False],
        ["Ann", "Doe", 12, True],
        ["Ann", "Doe", 12, True],
        ["Ann", "Doe", 12, True],
        ["Ann", "Doe", 12, True],
        ["Ann", "Doe", 12, False],
        ["Ann", "Doe", 12, True],
        ["Ann", "Doe", 12, True]
    ]

    for row in data:
        sheet.append(row)

    workbook.save('ex.xlsx')