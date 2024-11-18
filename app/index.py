from flask import render_template
from app import app
from app.models import Personal

@app.route('/user_info/<cccd_id>')
def user_info(cccd_id):
    nguoi_dung = Personal.query.filter_by(cccd_id=cccd_id).first()
    if nguoi_dung:
        return render_template('index.html', nguoi_dung=nguoi_dung)
    else:
        return "Không tìm thấy người dùng có số CCCD: " + cccd_id