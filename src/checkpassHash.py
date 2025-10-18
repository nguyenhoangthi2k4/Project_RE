# tạo file exe nhập mật khẩu với hash
from hashlib import sha256

def hash_password(password):
    """Trả về hash SHA-256 của mật khẩu."""
    return sha256(password.encode()).hexdigest()

def check_password(password, hashed_password):
    """Kiểm tra mật khẩu đã cho với hash đã lưu."""
    return hash_password(password) == hashed_password

if __name__ == "__main__":
    stored_hashed_password = "0c5bbf26aec5bf446593a85747bc9262f3dde7425d21ca0a23b452476b18990f" #sinhvienIT
    user_input = input("Nhập mật khẩu: ")
    
    if check_password(user_input, stored_hashed_password):
        print("Mật khẩu đúng!")
    else:
        print("Mật khẩu sai!")
    pause = input("Nhấn Enter để thoát...")
