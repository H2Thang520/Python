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

# n = int (input("Nhap N: "))
# b1 = Bai1()
# b1.InHinhChuNhat(n)
# b1.InHinhTamGiacVuong(n)
# b1.InHinhTamGiacDeu(n)

# b2 = Bai2()
# b2.TimMinMax()

b3 = Bai3()
b3.Dictionnary()