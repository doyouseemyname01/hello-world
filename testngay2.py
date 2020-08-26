#lặp chữ cái trong python
for chu in "quantrimang":
    print(chu)
#output: q u a n t r i m a n g

#lặp từ trong chuỗi
chuoi = ['bố', 'mẹ', 'em']
for chu in chuoi:
    print("anh yêu", chu)

'''output: anh yêu bố
anh yêu mẹ
anh yêu em  '''

#tính tổng tất cả số trong danh sách A (chuỗi)
A = [1, 3, 5, 6, 7, 6]
sum = 0
for a in A:
    sum += a
#ouput = 28
print("sum =", sum)

#Hàm range()
#sử dụng hàm range() để tạo ra một dãy số, ví dụ range(100) sẽ tạo ra một dãy từ 0 dến 99 (100 số)
#Hàm range(số bắt đầu,số kết thúc, khoảng cách giữa 2 số
#Để hàm range() xuất tất cả giá trị, bạn cần sử dụng hàm list()
print(list(range(1,9)))
print(list(range(0, 15, 5)))

#kết hợp hàm range() với hàm len() để lặp qua một dãy sử dụng index
chuoi = ['bố', 'mẹ', 'em']
for tu in range(len(chuoi)):
    print("anh yêu", chuoi[tu]) #giống mảng

#kết hợp For và else
B = [0, 3, 4, 6]
for b in B:
    print(b)
else:
    print("đã hết số")
"""output:
0
3
4
6
đã hết số
"""
#else sẽ chạy khi không có lệnh break nào được thực thi
for number in range(0, 10):
    for i in range(2,number):
        if number % i == 0:
            j = number % i
            print("%d bằng %d * %d" %(number, j, i))
            break
    else:
        print(number,"là số nguyên tố")

