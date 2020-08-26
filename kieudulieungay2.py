#Chuỗi trong Python

#thay đổi hoặc xóa chuỗi
#các chuỗi trong Python không thể thay đổi - chúng là cố định giống như tuple,xóa toàn bộ chuỗi bằng del:
#bạn không thể xóa hoặc loại bỏ ký tự ra khỏi chuỗi

#Nối chuỗi
#nối bằng dấu (+) hoặc dấu (*)
x = 3 * "un" + 'in'
print(x)
#output: unununin

#Hai hoặc nhiều ký tự dạng chuỗi(tức là nằm trong dấu nháy) cạnh nhau được nối tự động
z = "py" "thon"
b = 'py' 'thon'
print(z)
print(b)
#output: python

#tính năng trên chỉ làm việc với dạng chuỗi, không áp dụng với biến hay biểu thức
'''prefix = 'py'
x = prefix 'thon'
print(x)
#output: SyntaxError: invalid syntax'''

#sử dụng dấu cộng để ghép nối các biến với nhau, hoặc biến với chuỗi
prefix = 'py'
z = prefix + 'thon'
print(z)
#output: python


#lặp và kiểm tra phần tử trong chuỗi
cout = 0
x = 'quantrimang.com'
for letter in x:
    if letter == 'i':
        cout += 1
print("có", cout, "phần tử i ở đây")
#output: có 1 phần tử i ở đây

#hai hàm len() và hàm enumerate()(liệt kê) thường dùng nhất khi làm việc với string trong Python
#hàm len(), sẽ trả về độ dài của chuỗi
s = 'qqqqqqqqqqqqeeeeeeeeeeeeeeeeerrrrrrrrvvv'
print(len(s))
#output: 40

#hàm enumerate() trả về đối tượng liệt kê, chứa cặp giá trị và index của phần tử trong string

qtm_str = 'Python'

r = list(enumerate(qtm_str)) #kết hợp với hàm list() để liệt kê toàn bộ các cặp chứa giá trị
print(r)


#hàm format() để định dạng chuỗi
#phương phát format() rất linh hoạt và đầy sức mạnh khi dùng để định dạng chuỗi
#định dạng chuỗi chứa dấu {} làm trình giữ chỗ hoặc trường thay thế để nhận giá trị thay thế

thu_tumac_dinh = '{} và {} và {}'.format('quản', 'trị', 'mạng')
print(thu_tumac_dinh)



#phương thức thường được sử dụng trong string
#có lower(), upper(), joih(), split(), find(), replace(), vvv

x = "QUANTRIMANG.COM".lower()
print(x)

y = "quantrimang.com".upper()
print(y)

z = 'quan tri man cham com'.split()
print(z)

c = ['quan', 'tri', 'mang']
print(' '.join(c))

c = 'quantrimang'
print(','.join(c)) #output: q,u,a,n,t,r,i,m,a,n,g

c = 'quan tri mang chấm com'.find('co')
print(c) #phương thức find() giúp tìm ra thứ tự trong chuỗi

c = ['quan', 'tri', 'mang'.find('ng')]
print(c) #


#truy cập vào phần tử của list
#index chỉ mục của list:
#sử dụng toán tử index[] để truy cập vào một phần tử của list. Index bắt đầu từ 0,
#Index phải là một số nguyên, không thể sử dụng float, hay kiểu dữ liệu khác, sẽ tạo ra lỗi TypeError

squares = [1, 4, 9, 16, 25]
print(squares)
list1 = [] #list rỗng
list2 = [1, 2, 3] #list số nguyên
list3 = [1, 'hello', 3.4] #list với kiểu dữ liệu hỗn hợp

#có thể tạo các list lồng nhau
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0]) #output:  ['a', 'b', 'c']
print(x[0][1]) #ouput: b

list4 = ['mouse', [8, 4 , 3], ['a']]
print(list(enumerate(list4)))



ln_list = ['hello', [1,2,4,6]]
print(list(enumerate(ln_list)))


#Thay đổi hoặc thêm phần tử vào list

#Hỗ trợ việc nối các hoạt động như nối list:
x = squares + [36, 49, 64, 81, 100]
print(x)
print(squares) #squares ở trên

#không giống như chuỗi, bị cố định, còn list là kiểu dữ liệu có thể thay đổi

number = [1, 3, 4, 5, 5]
number[0] = 6
#print(number) #output: [6, 3, 4, 5, 5]


#bạn có thêm mục mới vào cuối list bằng cách sử dụng phương thức append():
number.append(9)
print(number) #không gán đc x = number.append()
#ouput: [6, 3, 4, 5, 5, 9]

#việc gán cho lát cũng có thể thực hiện và thậm chỉ có thể thay đổi cả kích thước của list hay xóa nó hoàn toàn
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

#xóa list bằng cách gán tất cả phần tử bằng rỗng
letters[:] = []
print(letters) #output: [], rỗng phần tử
#hàm len() cũng có thể áp dụng được với list
print(len(letters)) #output: 0, vì vừa xóa phần tử trong list

#xóa hoặc bỏ từng phần tử trong list
my_list = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']

del my_list[2]
print(my_list) #output: ['q', 'u', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', '.', 'c', 'o', 'm']

del my_list[1:7]
print(my_list) # Output: ['q', 'a', 'n', 'g', '.', 'c', 'o', 'm']


#bạn có thể sử dụng remove() loại bỏ những phần tử đã cho hoặc pop() để loại bỏ phần tử tại một index nhất định .pop()
#.pop() loại bỏ phần tử trả về và phần tử cuối cùng nếu không chỉ định index
#Điều này giúp triển khai list dưới dạng stack (ngăn xếp) (cấu trúc dữ liệu first in last out - vào đầu tiên, ra cuối cùng).
#phương thức clear() cũng được dùng để làm rỗng một list (xóa tất cả các phần tử trong list)
my_list = ['q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', '.', 'c', 'o', 'm']
my_list.remove('.')

# Output: ['q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', 'c', 'o', 'm']
print(my_list)

# Output: n
print(my_list.pop(3))

# Output: ['q', 'u', 'a', 't', 'r', 'i', 'm', 'a', 'n', 'g', 'c', 'o', 'm']
print(my_list)

# Output: m
print(my_list.pop())

# Output: ['q', 'u', 'a', 't', 'r', 'i', 'm', 'a', 'n', 'g', 'c', 'o']
print(my_list)

my_list.clear()

# Output: [] (list rỗng)
print(my_list)

my_list = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
my_list[11:15]=[]
print(my_list) #output ['q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g']

#TỔNG HỢP LẠI

'''Phương thức list trong Python
Những phương thức có sẵn cho list trong Python gồm:

append(): Thêm phần tử vào cuối list.
extend(): Thêm tất cả phần tử của list hiện tại vào list khác.
insert(): Chèn một phần tử vào index cho trước.
remove(): Xóa phần tử khỏi list.
pop(): Xóa phần tử khỏi list và trả về phần tử tại index đã cho.
clear(): Xóa tất cả phần tử của list.
index(): Trả về index của phần tử phù hợp đầu tiên.
count(): Trả về số lượng phần tử đã đếm được trong list như một đối số.
sort(): Sắp xếp các phần tử trong list theo thứ tự tăng dần.
reverse(): Đảo ngược thứ tự các phần tử trong list.
copy(): Trả về bản sao của list.'''

#TÓM TẮT TỪ index() trở đi
QTM = [9, 8, 7, 6, 8, 5, 8]

# Output: 2
print(QTM.index(7))

# Output: 3
print(QTM.count(8))

QTM.sort()

# Output: [5, 6, 7, 8, 8, 8, 9]
print(QTM)

QTM.reverse()

# Output: [9, 8, 8, 8, 7, 6, 5]
print(QTM)

#ví dụ khác dành chỗ kiểu chữ

QTM = ['q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', '.', 'c', 'o', 'm']

# Output: 3
print(QTM.index('n'))

# Output: 2
print(QTM.count('a'))

QTM.sort()

# Output: ['.', 'a', 'a', 'c', 'g', 'i', 'm', 'm', 'n', 'n', 'o', 'q', 'r', 't', 'u']
print(QTM)

QTM.reverse()

# Output: ['u', 't', 'r', 'q', 'o', 'n', 'n', 'm', 'm', 'i', 'g', 'c', 'a', 'a', '.']
print(QTM)

#List comprehension: Cách tạo list mới ngắn gọn
#list comprehension là một biểu thức đi kèm vòng lặp for được đặt trong dấu ngoặc vuông []

number = [3 ** x for x in range(9)]
print(number) #output [1, 3, 9, 27, 81, 243, 729, 2187, 6561]
#tương đương với

number = []
for x in range(9):
    number.append(3**x)
print(number) #output: [1, 3, 9, 27, 81, 243, 729, 2187, 6561]

#Ngoài kết hợp với vòng lặp for thì có thể kết hợp được với if
number = [3 ** x for x in range(9) if x > 4]
print(number) #output [243, 729, 2187, 6561]

number = [3 ** x for x in range(9) if x % 2 == 1]
print(number) #output [3, 27, 243, 2187]

#noi_list
noi_list = [x + y for x in ['ngôn ngữ ', 'lập trình'] for y in ['python', 'c++']]
print(noi_list)

#tương tự
list = []
for x in ['ngôn ngữ ', 'lập trình']:
    for y in ['python', 'c++']:
        list.append(x+y)
print(list)
#output: ['ngôn ngữ python', 'ngôn ngữ c++', 'lập trìnhpython', 'lập trìnhc++']



#Kiểm Tra Phần Tử Có Trong List Hay Không
#Sử dụng keyword in để kiểm tra xem một phần tử đã có trong list hay chưa.
#Nếu phần tử đã tồn tại, kết quả trả về là True, và ngược lại sẽ trả về False.
QTM = ['q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', '.', 'c', 'o', 'm']

# Output: True
print('q' in QTM)

# Output: True
print('.' in QTM)

# Output: False
print('z' in QTM)

#output: False
print('h' in QTM)

#Vòng lặp for trong list
for ngon_ngu in ['Python', 'Java', 'C']:
    print("Tôi thích lập trình", ngon_ngu)
'''output:Tôi thích lập trình Python
Tôi thích lập trình Java
Tôi thích lập trình C
'''


#Các hàm Pythin tích hợp sẵn như all(), any(), enumerate(), len(), min(), max(), list(), sorted()
#sử dụng trong list để thực hiện nhiệm vụ khác nhau
'''
all(): Trả về giá trị True nếu tất cả các phần tử của list đều là true hoặc list rỗng.
any(): Trả về True khi bất kỳ phần tử nào trong list là true. Nếu list rỗng hàm trả về giá trị False.
enumerate(): Trả về đối tượng enumerate, chứa index và giá trị của tất cả các phần tử của list dưới dạng tuple.
len(): Trả về độ dài (số lượng phần tử) của list.
list(): Chuyển đổi một đối tượng có thể lặp (tuple, string, set, dictionary) thành list.
max(): Trả về phần tử lớn nhất trong list.
min(): Trả về phần tử nhỏ nhất trong list.
sorted(): Trả về list mới đã được sắp xếp.
sum(): Trả về tổng của tất cả các phần tử trong list.'''

QTM = [9, 8, 7, 6, 8, 5, 8]
print(sum(QTM))

print(max(QTM))

print(sorted(QTM))











#Tuple trong Python
#Tuple là một chuỗi các phần tử có thứ tự giống như list,
#Sự khác biệt giữa list và tuple là chúng ta không thể thay đổi các phần tử trong tuple khi đã gán, nhưng trong list thì các phần tử có thể thay đổi.
#Tuple thường được sử dụng cho các dữ liệu không cho phép sửa đổi và nhanh hơn list vì nó không thể thay đổi tự động


#Tuple được tạo bằng cách đặt tất cả các phần tử của nó trong dấu ngoặc đơn (), phân tách bằng dấu phẩy. Bạn có thể bỏ dấu ngoặc đơn nếu muốn,
# nhưng nên thêm nó vào cho code rõ ràng hơn.

#Tuple không bị giới hạn số lượng phần tử và có thể có nhiều kiểu dữ liệu khác nhau như số nguyên, số thập phân, list, string,...
my_tuple = ()
print(my_tuple)

#tuple số nguyên
my_tuple = (2, 4, 16, 2)
print(my_tuple)

#tuple lồng nhau
my_tuple = ('QTM', ['yyy', 2, 3], (2, 4, 5))
print(my_tuple)

my_tuple = 10, 'Hello World', 3.5, [2, 3, "hello world"]

#output: (10, 'Hello World', 3.5, [2, 3, 4])

a, b, c, d = my_tuple
print(a)
print(b)
print(c)
print(d)
'''output: 10
Hello World
3.5
[2, 3, 'hello world']
'''

#Tạo tuple chỉ có một phần tử hơi phức tạp chút,
#nếu bạn tạo theo cách thông thường là cho phần tử đó vào trong cặp dấu () là chưa đủ, cần phải thêm dấu phẩy để chỉ ra rằng, đây là tuple.
my_tuple = ("Quan tri mang") #output: <class 'str'>
print(type(my_tuple))

my_tuple = ("Quan tri mang",) #output: <class 'tuple'>
print(type(my_tuple))

my_tuple = "Quan tri mang", #output: (thêm dấu phẩy vào sau để nhận ra là kiểu <tupple>)
print(type(my_tuple))


#Truy cập vào các phần tử của tuple

# tuple lồng nhau
n_tuple = ("Quantrimang.com", [2, 6, 8], (1, 2, 3))

# index lồng nhau
# Output: 'r'
print(n_tuple[0][5])

# index lồng nhau
# Output: 8
print(n_tuple[1][2])

#Index âm: Python cho phép lập chỉ mục âm cho các đối tượng dạng chuỗi. Index -1 tham chiếu đến phần tử cuối cùng, -2 là thứ 2 tính từ cuối tính lên.

#Cắt lát: Có thể truy cập đến một loạt phần tử trong tuple bằng cách sử dụng toán tử cắt lát : (dấu 2 chấm).



#Thay đổi một tuple
#Không giống như list, tuple không thể thay đổi.
# Điều này có nghĩa là các phần tử của một tuple không thể thay đổi một khi đã được gán. Nhưng, nếu bản thân phần tử đó là một kiểu dữ liệu có thể thay đổi (như list chẳng hạn) thì các phần tử lồng nhau có thể được thay đổi.
# Chúng ta cũng có thể gán giá trị khác cho tuple (gọi là gán lại - reassignment).

my_tuple = (1 , 3 , 4 ,[7, 9])
my_tuple[3][0] = 10
print(my_tuple)
print(type(my_tuple))
# Nhưng phần tử có index 3 trong tuple là list
# list có thể thay đổi, nên phần tử đó có thể thay đổi
my_tuple[3][1] = 10
print(my_tuple)

my_tuple = (1 , 3 , 4 , 5)
print(type(my_tuple))
print(my_tuple)

# Nếu cần thay đổi tuple hãy gán lại giá trị cho nó

my_tuple = (1, 3, 4, 4)
print(type(my_tuple))
print(my_tuple)

#Bạn có thể dùng toán tử + để nối 2 tuple, toán tử * để lặp lại tuple theo số lần đã cho. Cả + và * đều cho kết quả là một tuple mới.

print((2, 4 , 8 , [3, 'em yêu anh']) + ("anh cũng yêu em", 3, 9))

# Lặp lại tuple
# Output: ('Quantrimang.com', 'Quantrimang.com', 'Quantrimang.com')
print(("Quantrimang.com",) * 3)


#Xóa tuple
#Các phần tử trong tuple không thể thay đổi nên chúng ta cũng không thể xóa, loại bỏ phần tử khỏi tuple.
#Nhưng việc xóa hoàn toàn một tuple có thể thực hiện được với từ khóa del như dưới đây:

QTM = ['q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', '.', 'c', 'o',
       'm']  # Không thể xóa phần tử của tuple # Nếu bạn bỏ dấu # ở dòng 8, # sẽ tạo ra lỗi: # TypeError: 'tuple' object doesn't support item deletion

# del QTM[3]

# Có thể xóa toàn bộ tuple
# Kết quả chạy code sẽ hiện ra lỗi:
# NameError: name 'my_tuple' is not defined
del QTM


#Phương thức và hàm dùng với tuple trong Python

#count(x): Đếm số phần tử x trong tuple.
#index(x): Trả về giá trị index của phần tử x đầu tiên mà nó gặp trong tuple.

QTM = ['q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', '.', 'c', 'o', 'm']

# Count
# Output: 1
print(QTM.count('t'))

# Index
# Output: 5
print(QTM.index('r'))


'''Các hàm dùng trong tuple khá giống với list, gồm có:

all(): Trả về giá trị True nếu tất cả các phần tử của tuple là true hoặc tuple rỗng.
any(): Trả về True nếu bất kỳ phần tử nào của tuple là true, nếu tuple rỗng trả về False.
enumerated(): Trả về đối tượng enumerate (liệt kê), chứa cặp index và giá trị của tất cả phần tử của tuple.
len(): Trả về độ dài (số phần tử) của tuple.
max(): Trả về phần tử lớn nhất của tuple.
min(): Trả về phần tử nhỏ nhất của tuple.
sorted(): Lấy phần tử trong tuple và trả về list mới được sắp xếp (tuple không sắp xếp được).
sum(): Trả về tổng tất cả các phần tử trong tuple.
tuple(): Chuyển đổi những đối tượng có thể lặp (list, string, set, dictionary) thành tuple.
'''

#Kiểm tra phần tử trong tuple

QTM = ['q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g', '.', 'c', 'o', 'm']

# Kiểm tra phần tử
# Output: True
print('a' in QTM)

# Output: False
print('b' in QTM)

# Not in operation
# Output: False
print('g' not in QTM)

#Output: False
NVT = [2, 3 , 4 , 7 ,5]
print(10 in NVT)

#Lặp qua các phần tử của tuple trong Python
#Sử dụng vòng lặp for để lặp qua các phần tử trong tuple.

for ngon_ngu in NVT:
    print("tôi yêu số", ngon_ngu)
"""tôi yêu số 2
tôi yêu số 3
tôi yêu số 4
tôi yêu số 7
tôi yêu số 5"""
for ngon_ngu in ('Python','C++','Web'):
    print("Tôi thích lập trình",ngon_ngu)
'''Tôi thích lập trình Python
 Tôi thích lập trình C++
 Tôi thích lập trình Web'''

#Set trong Python

#Set trong Python là tập hợp các phần tử duy nhất, không có thứ tự.
# Các phần tử trong set phân cách nhau bằng dấu phẩy và nằm trong dấu ngoặc nhọn {}.
# Nhớ kỹ rằng các phần tử trong set không có thứ tự. @@@@@
# Nhưng các phần tử trong set có thể thay đổi, có thể thêm hoặc xóa phần tử của set.
# Set có thể được sử dụng để thực hiện các phép toán như tập hợp, giao,...


a = {3, 4, 5 ,2, 3 }
print('a =', a) #set sẽ tránh được các ký tự lặp nhau và sắp xếp chúng theo thứ tự

a = {'m', 'n', 'a', 'c', 'b'}
print('a =', a)

#Tạo set rỗng có chút khó khăn. Cặp dấu {} sẽ tạo một dictionary trong Python. Để tạo set không có phần tử nào, ta sử dụng hàm set() mà không có đối số nào.

# initialize a with {}
qtm = {}
# Kiểm tra kiểu dữ liệu của qtm
# Output: <class 'dict'>
print(type(qtm))


#Làm sao để thay đổi set trong Python

#Để thêm một phần tử vào set, bạn sử dụng add() và để thêm nhiều phần tử dùng update().
# Update() có thể nhận tuple, list, strring và set làm đối số.
# Trong mọi trường hợp, Set có giá trị duy nhất, các bản sao sẽ tự động bị loại bỏ.


my_set = { 2, 3, 4}
print(my_set)

#thêm phần tử
my_set.add(5)
print(my_set)

#thêm nhiều phần tử vào set
my_set.update([1, 2, 3])
print(my_set)
#output: {1, 2, 3, 4, 5}

#thêm list và set
my_set.update([9,10], {1,23,99})
print(my_set)
#output: {1, 2, 3, 4, 5, 99, 9, 10, 23}

#Xóa phần tử khỏi set
#Bạn dùng discard() và remove() để xóa phần tử cụ thể khỏi set.
#Khi phần tử cần xóa không tồn tại trong set thì discard() không làm gì cả, còn remove() sẽ báo lỗi.

my_set.discard(3)
print(my_set) #output: {1, 2, 4, 5, 99, 9, 10, 23}
#chỉ lấy chính xác 1 dối số, không thể xóa hơn 1 đối số
print(my_set)
my_set.remove(4)
print(my_set) #output: {1, 2, 5, 99, 9, 10, 23}

# Khởi tạo my_set
 # Output: set of unique elements
my_set = set("Quantrimang.com")
print(my_set)
#output random :{'.', 'm', 'c', 'i', 'r', 'a', 'g', 'o', 'Q', 't', 'u', 'n'}

print(my_set.pop())
#xóa phần tử bằng pop()
#xóa phần tử một cách ngẫu nhiên

#clear my_set
#Output: set()
my_set.clear()
print(my_set)


#Các toán tử set trong Python
#Set thường được sử dụng để chứa các toán tử tập hợp như hợp, giao, hiệu, bù.
# Có cả phương thức và toán tử để thực hiện những phép toán tập hợp này.

