import xlrd
from .models import Computer, ComputerModel

# book = xlrd.open_workbook("book1.xlsx")
# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))
# sh = book.sheet_by_index(0)
# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# print("Cell D30 is {0}".format(sh.cell_value(rowx=11, colx=1)))
# for rx in range(sh.nrows):
#     print(sh.row(rx))


class ExcelParser:

    def parse(self, filename):
        wb = xlrd.open_workbook(filename)
        sh = wb.sheet_by_index(0)
        result = []
        for row in range(sh.nrows):
            # line = sh.cell_value(rowx=row, colx=1)
            # result[sh.cell_value(rowx=row, colx=0)] = line.replace(u'\xa0', ' ')
            temp_list = []
            for col in range(sh.ncols):
                item = sh.cell_value(rowx=row, colx=col)
                if isinstance(item, float):
                    item = int(item)
                if isinstance(item, str) and u'\xa0' in item:
                    item = item.replace(u'\xa0', ' ')
                temp_list.append(item)
            result.append(temp_list)
        return result


class SaveListToModel:

    def __init__(self, querylist):
        self.querylist = querylist
        self.save_in_model()

    def save_in_model(self):
        for row in self.querylist:
            obj, created = ComputerModel.objects.get_or_create(computermodelname=row[len(row)-1])
            get = Computer.objects.create(
                inventorynum=row[0],
                serialnum=row[1],
                name=row[2],
                netbiosname=row[3],
                ip=row[4],
                macaddress=row[5],
                computermodel_id=obj
            )
            get.save()


# for key, value in exceldata.items():
#     obj, created = WorkstationModel.objects.get_or_create(model=value)
#     if created:
#         get = Workstation.objects.create(title=key, model=obj)
#         get.save()
#     else:
#         comp = Workstation.objects.create(title=key, model=obj)
#         comp.save()