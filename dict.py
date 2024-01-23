# Khai báo và các phương thức xoay quanh dict

data = {
    "id": "001",
    "name": "abc",
    "phone":"0911572155"
}

# C:Create thêm 1 giá trị vào dict, 
# U:Update cập nhật
# Thêm cặp key value khi dict chưa có key value đó, cập nhật giá trị cho key khi dict đã có key rồi
data["desc"] = "information dict"
data["desc"]="0914740698"
print(data)
# R:Read đọc dữ liệu
for key in data:
    print("key", key)
    print("value", data[key])
# D:Delete xóa
del data['desc']
data.clear() # xóa các giá trị trong dict
del data #Xóa khỏi bộ nhớ máy tính
# print(data)

# Phương thức thường sử dụng với dict
# Phương thức Get: trả ra giá trị của key, nếu key không tồn tại thì trả ra mặc định
phone = {
    "id": "01",
    "name":"Iphone",
    "price":1000
}
print(phone.get("desc", "none value"))

# Phương thức .keys(): lấy ra tất cả các key dưới dạng list
print(phone.keys())

# Phương thức .values(): lấy tất cả values dưới dạng list
print(phone.values())

# Phương thức .items(): lấy ra từng dict con dưới dạng tuple
print(phone.items())

# dict nâng cao (trong các thuộc tính key value sẽ là các dict con hoặc list hoặc tuple set...)
shoes_item = {
    "id":"nike01",
    "name":"pegasus39",
    "sizes":[41,42,43],
    "quantity":{
        "41":5,
        "42":5,
        "43":5
    }
}

# Phương thức .copy(): shallow copy (sao chép nông)
shoes_clone = shoes_item.copy()
shoes_clone["name"] = "abc"
print(id(shoes_clone), shoes_clone)
print(id(shoes_item), shoes_item)

# Phương thức deepcopy(): copy hoàn toàn dict hoặc list

# list comprehension: tạo list mới từ list cũ
lst_number = [1,2,3,4,5]
new_lst_number = [num * 2 for num in lst_number]
print(new_lst_number)
new_lst_even_number = [ele for ele in lst_number if ele % 2 == 0]
print(new_lst_even_number)

# Tuple: là collection type chứa nhiều giá trị trên 1 biến tương tự list(có index) tuy nhiên tuple không thể thay đổi giá trị
screen = (1080, 720)
print(screen[0])
print(screen[1])
dict_bullect = {
    (0,0):'1',
    (0,10):'2'
}
print(dict_bullect)
print(dict_bullect[(0,0)])
# set: chứa các giá trị không trùng nhau
lst_number = [1,1,1,2,2,2,3,3,3]
set_number = list(set(lst_number))
print(set_number)
num = 1
string_number = str(num)

tuple_number = (1,2,3,4,5)
lst_res = tuple(list(tuple_number))
print(lst_res)
# ghi chú: có thể chuyển đổi qua lại giữa các collection type(trừ dict vì dict có key): bằng cách ép kiểu
# Ví dụ: list(tuple): ép kiểu từ tuple về list
#        tuple(list): ép từ list về tuple
#        set(list): ép từ list về set => loại bỏ được các phần tử trùng
#        tuple(set): ép từ set về tuple
#        set(tuple): ép từ tuple về set
# để chuyển từ các kiểu trên về dict có thể dùng compehension