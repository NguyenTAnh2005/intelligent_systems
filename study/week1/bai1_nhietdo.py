def checking_var(tempture):
    # Phan vung gia tri
    if tempture < 22:
        return "Lạnh"
    elif tempture < 27:
        return "Vừa"
    else:
        return "Nóng"
    
n = input("Nhập vào đây nhiệt độ trong phòng: ")
try:
    print(checking_var(float(n)))
except:
    print("Lỗi dữ liệu đầu vào!")


    