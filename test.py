mylist = ['apple', 'banana', 'cherry']
x = len(mylist)
print(x)

z = "CODELEARN"
print(z.lower())


v = "codelearn"
print(v.upper())

b = "2020"
print(b.isnumeric())
#hàm isnumeric kiểm tra xem một xâu có chứa toàn các ký tự số hay không :))
b = 'c2020'
print(b.isnumeric())

#hàm split, hàm này dùng để cắt một chuỗi ra thành list các chuỗi khác dựa trên chuỗi đầu vào
b = "Welcome to Summers rift"
print(b.split(" "))

b = "A1B1C1D1E1"
print(b.split("1"))
'''output: ['Welcome', 'to', 'Summers', 'rift']
['A', 'B', 'C', 'D', 'E', '']'''

#hàm join, hàm này dùng để nối một tập hợp thành một chuỗi
lst = ["welcome", "to", "the", "Summer's Rift"]
print(" " .join(lst))

lst = ['a', 'b', 'c', 'd']
print("_" .join(lst))
'''output: welcome to the Summer's Rift
a_b_c_d '''

#Hàm split() và hàm join() kết hợp để loại bỏ khoảng trắng thừa trong chuỗi
message = "welcome     to  codelearn.io!    "
print(" ".join(message.split()) )
#output: welcome to codelearn.io!

#hàm replace, hàm này dùng để thay thế các chuỗi con tìm thấy chuỗi mới
name = "cod3l3arn"
print(name.replace("3", "e"))
#output: codelearn

s = "Python String"
print(s[0])
#in ra phần tử đầu tiên trong chuỗi
print(s[-1])
#in ra phần tử cuối cùng trong chuỗi
print(s[-2])
#in ra phần tử đứng trước phần tử cuối cùng trong chuỗi
'''output:
p
g
n'''

#cắt chuỗi trong Python(Slice a string in Python)
#để lấy ra một dãy các ký tự liên tiếp trong chuỗi, bạn có thể sử dụng phương pháp slicing
s = 'Python String'
print(s[0:2]) #sẽ lấy từ 0 và 1 ký tự đầu
print(s[3:5]) # sẽ lấy từ 3 đến 4 ký tự đầu
print(s[7:]) # sẽ tính từ 7 còn lại lấy hết
print(s[:6])
print(s[7:-4])
print(s[-2:])
print(s[9:-1])
'''output:
Py
ho
String
Python
St
'''

x = "Python"
print(x[1])
#Slice - Trả về kí tự trong chuỗi

print(x[1:3]) # bắt đầu từ 1 đến 2
#Range slice-Trả về dãy kí tự trong chuỗi


print(x[2:5])# bắt đầu từ 2 đến 4

print("u" in x) #kiểm tra xem chuỗi có nằm trong chuỗi khác không


x = 12.345678
print("The value of x is %5.5f" %x)

x = 'code'
y = 'learn'
print(x + y) #cộng hai chuỗi với nhau

s1 = "Welcome"
print(s1[2:]) #lcome

print(s1[-2:]) #me

print(s1[:2]) #We


s1 = "sun"
s2 = "moon"
s1 = input()
s2 = input()
tmp = s1[:2] + s2[2:]
s1 = s2[:2] + s1[2:]
s2 = tmp
print(s1 + " " + s2)
