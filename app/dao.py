from app import db  # Import the SQLAlchemy object

def lay_thong_tin_nguoi_dung(so_cccd):
    """
    Lấy thông tin người dùng từ database MySQL dựa trên số CCCD.
    """

    cursor = db.connection().cursor(dictionary=True)  # Use db.connection() to get the connection
    sql = "SELECT * FROM personal WHERE cccd_id = %s"
    val = (so_cccd,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    return result
