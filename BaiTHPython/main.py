class Bai1:
    def InHinhChuNhat(self, n):
        i =0
        print("Hinh chu nhat While")
        while i < n:
            print("o" * n)
            i = i + 1

        print("Hinh chu nhat For")
        for i in range (0,n):
            print("p" * n)
            i = i + 1
    def InHinhTamGiacVuong(self, n):
        print("Hinh tam giac vuong")
        for i in range (1,n+1):
            print("z" * i)
            i = i + 1

        print("Hinh tam giac vuong nguoc")
        for i in range (1,n+1):
            print(" " * (n-i) + "e" * i)
            i = i + 1
    def InHinhTamGiacDeu(self, n):
        print("Hinh tam giac deu")
        for i in range (1,n+1):
            nSpace = n-i
            if nSpace%2 == 0:
                print(round(nSpace/2) *  " " + "t" * i )

class Bai2:
    def TimMinMax(self):
        n = int(input("Nhap so luong phan tu: "))
        if n <= 0:
            exit()
        a = []
        for i in range(0,n):
            a.append(int(input("a [%d] " % (i+1) ) ) )
        print(a)
        h = max(a)
        w = min(a)
        if h < 0:
            print("So duong lon nhat la: *")
        else:
            print("So duong lon nhat la: ",h)
            if w > 0:
                print("So am nho nhat la: *")
            else:
                print("So am nho nhat la: ", w)

class Bai3:
    def Dictionnary(self):
        dic = {
            'Tester' : 'Kiem thu vien',
            'Developer' : 'Lap trinh vien'
        }
        print(dic)
        dic.update({'QA' : 'Kiem soat chat luong SP'})
        print(dic)
        print("So luong phan tu %d " %len(dic))
        flag = 'false'
        key = "Tester"
        for k in dic.keys():
            if k == key:
                flag = 'true'
                break
        if flag == 'false':
            print("Khong tim thay")
        else:
            print("Tim thay")
            del dic[k]
        print(dic)

class Bai4:
    listEmployees = [{
            "Ma NV" : 1,
            "Ten NV" : "Nguyễn Văn A",
        }, {
            "Ma NV" : 2,
            "Ten NV" : "Lê Văn B",
        }, {
            "Ma NV" : 3,
            "Ten NV" : "Hồ Hữu C",
        }]
    n = len(listEmployees)
    def GetAllEmployees(self):
        for i in range(0,self.n):
            print("Ma NV: " + format(self.listEmployees[i]["Ma NV"]))
            print("Ten NV: " + self.listEmployees[i]["Ten NV"])
    def FindEmployees(self, name):
        for i in range(0,self.n):
            if self.listEmployees[i]["Ten NV"].find(name) != -1:
                print("Ma NV: " + format(self.listEmployees[i]["Ma NV"]))
                print("Ten NV: " + self.listEmployees[i]["Ten NV"])
    def FindEmployees2(self, name):
        for i in range(0,self.n):
            if format(self.listEmployees[i]["Ma NV"]).find(name) != -1:
                print("Ma NV: " + format(self.listEmployees[i]["Ma NV"]))
                print("Ten NV: " + self.listEmployees[i]["Ten NV"])


    def AddEmployees(self):
        id = int(input("Nhap Ma NV: "))
        for i in range(0,self.n):
            if self.listEmployees[i]["Ma NV"] == id:
                print("Ma NV da ton tai")
                return -1
        name = input("Nhap Ten NV: ")
        newEmployees = {"Ma NV" : id, "Ten NV" : name}
        self.listEmployees.append(newEmployees)
        self.n = len(self.listEmployees)
        print("Danh sach NV sau khi them la: ")
        self.GetAllEmployees()
    def DeleteEmployees(self):
        id2 = int(input("Nhap MaNV xoa: "))
        for i in range(0,self.n):
            if self.listEmployees[i]["Ma NV"] == id2:
                del self.listEmployees[i]
                self.n = len(self.listEmployees)
                print("Danh sach NV sau khi xoa: ")
                self.GetAllEmployees()
                return
        print("Khong tim thay")
    def DeleteEmployees2(self):
        id = input("Nhap Ten NV: " )
        for i in range(0,self.n):
            if self.listEmployees[i]["Ten NV"].find(id) != -1:
                del self.listEmployees[i]
                self.n = len(self.listEmployees)
                print("Danh sach sau khi xoa: ")
                self.GetAllEmployees()
                return
            else:
                 print("Khong tim thay NV")
# n = int (input("Nhap N: "))
# b1 = Bai1()
# b1.InHinhChuNhat(n)
# b1.InHinhTamGiacVuong(n)
# b1.InHinhTamGiacDeu(n)

# b2 = Bai2()
# b2.TimMinMax()

# b3 = Bai3()
# b3.Dictionnary()

b4 = Bai4()
# b4.GetAllEmployees()
# b4.FindEmployees("Nguyễn Văn A")
# b4.FindEmployees2("2")
b4.AddEmployees()
b4.DeleteEmployees()
# b4.DeleteEmployees2()


