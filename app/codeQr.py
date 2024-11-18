import cv2
from pyzbar import pyzbar
from app.dao import lay_thong_tin_nguoi_dung
from app.models import Personal
import json
from app import app, db  # Import app và db
from flask import redirect, url_for
import webbrowser

def lay_tat_ca_nguoi_dung():
    with app.app_context():
        nguoi_dung = Personal.query.all()
    return nguoi_dung

# Khởi tạo camera
cap = cv2.VideoCapture(1)  # 1 là chỉ số camera iVCam
da_quet_duoc = False  # Biến kiểm tra xem đã quét được mã QR chưa

while True:
    # Đọc frame hình ảnh từ camera
    ret, frame = cap.read()

    # Quét mã QR trong frame
    ma_qr = pyzbar.decode(frame)
    for qr in ma_qr:
        try:
            # Lấy dữ liệu từ mã QR
            du_lieu_qr = qr.data.decode("utf-8")

            # Trích xuất số CCCD
            so_cccd = du_lieu_qr.split("|")[0]

            # Lấy tất cả người dùng từ model
            tat_ca_nguoi_dung = lay_tat_ca_nguoi_dung()

            # Tìm kiếm người dùng có số CCCD tương ứng
            nguoi_dung = next((item for item in tat_ca_nguoi_dung if item.cccd_id == so_cccd), None)

            if nguoi_dung:  # Sửa lỗi indentation
                print("Thông tin người dùng:")
                print(f"- Số CCCD: {nguoi_dung.cccd_id}")
                print(f"- Họ tên: {nguoi_dung.name}")
                print(f"- Ngày sinh: {nguoi_dung.date}")
                print(f"- Địa Chỉ: {nguoi_dung.address}")
                print(f"- Giới Tính: {nguoi_dung.sex}")
                print(f"- Quê Quán: {nguoi_dung.hometown}")
            else:
                print("Không tìm thấy người dùng có số CCCD:", so_cccd)

            da_quet_duoc = True  # Đánh dấu đã quét được mã QR
            break  # Thoát khỏi vòng lặp for

        except Exception as e:
            print("Lỗi:", e)

    # Hiển thị frame hình ảnh
    cv2.imshow("Quet ma QR", frame)

    # Thoát khỏi vòng lặp khi nhấn phím 'd' hoặc đã quét được mã QR
    if cv2.waitKey(1) & 0xFF == ord('d') or da_quet_duoc:
        break
# Giải phóng camera và đóng cửa sổ hiển thị
cap.release()
cv2.destroyAllWindows()