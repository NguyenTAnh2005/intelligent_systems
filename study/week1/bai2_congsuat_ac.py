air_condition_power = 30
def calculate_final_power(T_in, T_out, n_people, base_power):
    try:
        T_in = float(T_in)
        T_out = float(T_out)
        n_people = int(n_people)
        base_power = float(base_power) 
        T_in <= T_out
        n_people >= 0
    except:
        return "Lỗi dữ liệu đầu vào!"
    
    if T_in > 28:
        base_power += 10
    if T_out > 36:
        base_power += 20
    if n_people > 30:
        base_power += 15


    if base_power > 100:
        base_power = 100
    
    return base_power

print("Chương trình tính công suất aie con đi sần nồ  dựa theo các thông số đầu vào.")

T_in = input("Nhập nhiệt độ trong phòng (°C): ")
T_out = input("Nhập nhiệt độ ngoài trời (°C): ")
n_people = input("Nhập số người trong phòng: ")

final_power = calculate_final_power(T_in, T_out, n_people, air_condition_power)
print(f"Công suất điều hòa cần thiết là: {final_power}%")
    