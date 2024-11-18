import random
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from app import db, app

class Personal(db.Model):
    cccd_id = Column(String(12), primary_key=True, unique=True)
    name = Column(String(50), nullable=False)
    date = Column(String(255), nullable=True)
    sex = Column(String(255), default=0)
    hometown = Column(String(100), nullable=True)
    address = Column(String(100), nullable=True)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        data = [
            {
                "ho_ten": "Nguyễn Văn A",
                "ngay_sinh": "01/01/2000",
                "gioi_tinh": "Nam",
                "que_quan": "Hà Nội",
                "so_cccd": "001234567890",
                "dia_chi": "123 Đường ABC, Quận XYZ, Thành phố EFG"
            },
            {
                "ho_ten": "Lê Thị B",
                "ngay_sinh": "02/02/2001",
                "gioi_tinh": "Nữ",
                "que_quan": "Hồ Chí Minh",
                "so_cccd": "045204003256",
                "dia_chi": "456 Đường DEF, Quận UVW, Thành phố GHI"
            },
            {
                "ho_ten": "Trần Văn C",
                "ngay_sinh": "03/03/2002",
                "gioi_tinh": "Nam",
                "que_quan": "Đà Nẵng",
                "so_cccd": "012345678901",
                "dia_chi": "789 Đường JKL, Quận MNO, Thành phố PQR"
            },
            {
                "ho_ten": "Phạm Thị D",
                "ngay_sinh": "04/04/2003",
                "gioi_tinh": "Nữ",
                "que_quan": "Hải Phòng",
                "so_cccd": "023456789012",
                "dia_chi": "1011 Đường STU, Quận VWX, Thành phố YZA"
            },
            {
                "ho_ten": "Hoàng Văn E",
                "ngay_sinh": "05/05/1999",
                "gioi_tinh": "Nam",
                "que_quan": "Cần Thơ",
                "so_cccd": "034567890123",
                "dia_chi": "1213 Đường BCD, Quận XYZ, Thành phố EFG"
            },
            {
                "ho_ten": "Vũ Thị F",
                "ngay_sinh": "06/06/1998",
                "gioi_tinh": "Nữ",
                "que_quan": "Huế",
                "so_cccd": "045678901234",
                "dia_chi": "1415 Đường CDE, Quận UVW, Thành phố GHI"
            },
            {
                "ho_ten": "Đặng Văn G",
                "ngay_sinh": "07/07/1997",
                "gioi_tinh": "Nam",
                "que_quan": "Nha Trang",
                "so_cccd": "056789012345",
                "dia_chi": "1617 Đường DEF, Quận MNO, Thành phố PQR"
            },
            {
                "ho_ten": "Bùi Thị H",
                "ngay_sinh": "08/08/1996",
                "gioi_tinh": "Nữ",
                "que_quan": "Vũng Tàu",
                "so_cccd": "067890123456",
                "dia_chi": "1819 Đường FGH, Quận VWX, Thành phố YZA"
            },
            {
                "ho_ten": "Lý Văn I",
                "ngay_sinh": "09/09/1995",
                "gioi_tinh": "Nam",
                "que_quan": "Đà Lạt",
                "so_cccd": "078901234567",
                "dia_chi": "2021 Đường GHI, Quận XYZ, Thành phố EFG"
            },
            {
                "ho_ten": "Trương Thị K",
                "ngay_sinh": "10/10/1994",
                "gioi_tinh": "Nữ",
                "que_quan": "Hạ Long",
                "so_cccd": "089012345678",
                "dia_chi": "2223 Đường HIJ, Quận UVW, Thành phố GHI"
            },
            {
                "ho_ten": "Lê Hồng Đức",
                "ngay_sinh": "20/12/2004",
                "gioi_tinh": "Nam",
                "que_quan": "Quảng Trị",
                "so_cccd": "045204003235",
                "dia_chi": "943 Lê Văn Lương, Xã Phước Kiển, Huyện Nhà Bè, Thành Phố Hồ Chí Minh "
            }
        ]
        for p in data:
            person = Personal(
                           cccd_id=p['so_cccd'] , name=p['ho_ten'],
                           date=p['ngay_sinh'],
                           sex=p['gioi_tinh'], hometown=p['que_quan'],
                           address=p['dia_chi'])
            db.session.add(person)

        db.session.commit()
