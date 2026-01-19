def calculate_hvac(T_in, n_people):
    try:
        T_in = float(T_in)
        n_people = int(n_people)
        n_people >= 0
    except:
        return "Lỗi dữ liệu đầu vào!"
    
    if T_in < 20:
        if n_people < 15:
            return "AC OFF"
        elif n_people < 35:
            return "AC MEDIUM"
        return "AC HIGH"
    
    elif T_in <30:
        if n_people < 10:
            return "AC OFF"
        return "AC MEDIUM"
    
    else:
        if n_people < 5:
            return "AC OFF"
        elif n_people < 15:
            return "AC MEDIUM"
        return "AC HIGH"
    
count_off = 0
count_medium = 0
count_high = 0

end = 5
start = 1
print("Chương trình kiểm tra trạng thái điều hòa dựa trên nhiệt độ và số người trong phòng.")
while start <= end:
    print(f"---------Lần kiểm tra thứ {start}:---------")
    T_in = input("Nhập nhiệt độ trong phòng (°C): ")
    n_people = input("Nhập số người trong phòng: ")
    status = calculate_hvac(T_in, n_people)
    match status:
        case "AC OFF":
            count_off += 1
        case "AC MEDIUM":
            count_medium += 1
        case "AC HIGH":
            count_high += 1
    print(f"Trạng thái điều hòa: {status}\n")
    start += 1

print("===============================================")
print("Tổng kết trạng thái điều hòa sau 5 lần kiểm tra:")
print(f"AC OFF: {count_off} lần")
print(f"AC MEDIUM: {count_medium} lần")
print(f"AC HIGH: {count_high} lần")
