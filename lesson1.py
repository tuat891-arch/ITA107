def add (a, b, c):
    s1 = a+b  #  Nhận thấy dòng 2 đang thực hiện 2 phép tính
    # Nhưng không phụ thuộc đến kích thước dữ liệu đầu vào 
    s2 = s1+c
    return s2
# T(n) = 5 => O(1) 
# - Thời gian thực hiện không phụ thuộc vào kích thước dữ liệu đầu vào
# O(n)
def sum (n):
    s = 0 #1
    for i in range(1, n+1): # n
        s += i # 2
    return s # 1
# T(n) = 1 + n*2 + 1 = 2n + 2 => O(n)
# O(n^2))
def sum2 (n):
    s = 0 #1
    for i in range(1, n+1): # n
        for j in range(1, n+1): # n
            s += i*j # 3
    return s # 1
# T(n) = 1 + n*(n*3) + 1 = 3n^2 + 2 => O(n^2)
# O(log n)
def sum3 (n):
    count = 0
    while n > 0: 
        n = n // 2
        count += 1
    return count
# T(n) = log n + 1 => O(log n)
# Lưu ý:
# O(1): rất nhanh
# O(n): duyệt phần tử 
# O(n^2): rất dễ gây châm chương trình phải đặc biệt chú ý
# O(log n): Thuật toán cực tốt
#  Dùng code hôm trước đã có hãy tính toán độ phức tạp
