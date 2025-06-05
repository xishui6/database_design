from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(minutes=1)

def get_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='XZY123',
        db='demo',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route('/')
def index():
    if 'username' in session and 'role' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/enter')
def enter():
    if 'username' in session and 'role' in session:
        if session['role'] == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('user_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        db = get_db()
        table = 'admin' if role == 'admin' else 'users'
        with db.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table} WHERE username = %s", (username,))
            user = cursor.fetchone()
        db.close()

        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            session['role'] = role
            return render_template('login.html', login_success=True)
        else:
            return render_template('login.html', error="用户名或密码错误", selected_role=role)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        role = request.form.get('role')

        if password != confirm_password:
            return render_template('register.html', error="两次输入的密码不一致", username=username, selected_role=role)

        db = get_db()
        table = 'admin' if role == 'admin' else 'users'
        try:
            with db.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table} WHERE username = %s", (username,))
                existing_user = cursor.fetchone()
                if existing_user:
                    return render_template('register.html', error="用户名已存在", username=username, selected_role=role)
                hashed_password = generate_password_hash(password)
                cursor.execute(f"INSERT INTO {table} (username, password) VALUES (%s, %s)", (username, hashed_password))
                db.commit()
        finally:
            db.close()
        return render_template('register.html', register_success=True)
    return render_template('register.html')

# 管理员首页：设备查询
@app.route('/admin')
def admin_dashboard():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))
    search_type = request.args.get('search_type')
    search_model = request.args.get('search_model')
    add_msg = request.args.get('add_msg')
    db = get_db()
    with db.cursor() as cursor:
        sql = """
            SELECT device_id, device_type, device_model, device_price, stock_quantity
            FROM device
            WHERE 1=1
        """
        params = []
        if search_type:
            sql += " AND device_type LIKE %s"
            params.append('%' + search_type + '%')
        if search_model:
            sql += " AND device_model LIKE %s"
            params.append('%' + search_model + '%')
        sql += " ORDER BY device_id DESC"
        cursor.execute(sql, params)
        devices = cursor.fetchall()
    db.close()
    return render_template('admin.html', username=session['username'], devices=devices, add_msg=add_msg, stat_result=None)
# 添加设备及入库
@app.route('/add_device', methods=['POST'])
def add_device():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))
    device_type = request.form['device_type']
    device_model = request.form['device_model']
    device_price = request.form['device_price']
    stock_quantity = request.form['stock_quantity']
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute(
            "INSERT INTO device (device_type, device_model, device_price, stock_in_time, stock_quantity) VALUES (%s, %s, %s, NOW(), %s)",
            (device_type, device_model, device_price, stock_quantity)
        )
        db.commit()
    db.close()
    return redirect(url_for('admin_dashboard', add_msg='设备添加成功'))

# 删除设备
@app.route('/delete_device', methods=['POST'])
def delete_device():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))
    device_id = request.form.get('device_id')
    if not device_id:
        return redirect(url_for('admin_dashboard', add_msg='设备ID无效'))
    db = get_db()
    try:
        with db.cursor() as cursor:
            cursor.execute("DELETE FROM device_record WHERE device_id=%s", (device_id,))
            cursor.execute("DELETE FROM device WHERE device_id=%s", (device_id,))
            db.commit()
    finally:
        db.close()
    return redirect(url_for('admin_dashboard', add_msg='设备删除成功'))

# 统计借还数量
@app.route('/device_stat')
def device_stat():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    stat_result = []
    if start_time and end_time:
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute("""
                SELECT d.device_id, d.device_type, d.device_model,
                    SUM(CASE WHEN r.borrow_time BETWEEN %s AND %s THEN 1 ELSE 0 END) AS borrow_count,
                    SUM(CASE WHEN r.return_time BETWEEN %s AND %s THEN 1 ELSE 0 END) AS return_count
                FROM device d
                LEFT JOIN device_record r ON d.device_id = r.device_id
                GROUP BY d.device_id, d.device_type, d.device_model
            """, (start_time, end_time, start_time, end_time))
            stat_result = cursor.fetchall()
        db.close()
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("""
            SELECT d.device_id, d.device_type, d.device_model, d.device_price, d.stock_quantity,
                   r.borrow_time, r.return_time
            FROM device d
            LEFT JOIN device_record r ON d.device_id = r.device_id
            ORDER BY d.device_id DESC
        """)
        devices = cursor.fetchall()
    db.close()
    return render_template('admin.html', username=session['username'], devices=devices, stat_result=stat_result, add_msg=None)

# 用户首页：查询设备库存
@app.route('/user', methods=['GET'])
def user_dashboard():
    if 'username' not in session or session.get('role') != 'user':
        return redirect(url_for('login'))
    search_type = request.args.get('search_type')
    search_model = request.args.get('search_model')
    borrow_msg = request.args.get('borrow_msg')
    return_msg = request.args.get('return_msg')
    db = get_db()
    try:
        with db.cursor() as cursor:
            sql = "SELECT * FROM device WHERE 1=1"
            params = []
            if search_type:
                sql += " AND device_type LIKE %s"
                params.append('%' + search_type + '%')
            if search_model:
                sql += " AND device_model LIKE %s"
                params.append('%' + search_model + '%')
            cursor.execute(sql, params)
            devices = cursor.fetchall()
    finally:
        db.close()
    return render_template('user.html', username=session['username'], devices=devices, borrow_msg=borrow_msg, return_msg=return_msg)

# 用户借出设备（严格校验，限制单次最多5台）
@app.route('/borrow_device', methods=['POST'])
def borrow_device():
    if 'username' not in session or session.get('role') != 'user':
        return redirect(url_for('login'))
    try:
        device_id = int(request.form['device_id'])
        borrow_count = int(request.form.get('borrow_count', 1))
    except Exception:
        return redirect(url_for('user_dashboard', borrow_msg="参数错误"))
    if borrow_count < 1 or borrow_count > 5:
        return redirect(url_for('user_dashboard', borrow_msg="借出数量必须为1-5台"))
    db = get_db()
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT id FROM users WHERE username=%s", (session['username'],))
            user = cursor.fetchone()
            if not user:
                return redirect(url_for('user_dashboard', borrow_msg="用户不存在"))
            cursor.execute("SELECT stock_quantity FROM device WHERE device_id=%s", (device_id,))
            device = cursor.fetchone()
            if not device or device['stock_quantity'] < borrow_count:
                return redirect(url_for('user_dashboard', borrow_msg="库存不足或设备不存在"))
            for _ in range(borrow_count):
                cursor.execute("INSERT INTO device_record (device_id, user_id, borrow_time) VALUES (%s, %s, NOW())", (device_id, user['id']))
            db.commit()
    except Exception:
        return redirect(url_for('user_dashboard', borrow_msg="借出失败，请重试"))
    finally:
        db.close()
    return redirect(url_for('user_dashboard', borrow_msg=f"借出成功，共借出{borrow_count}台"))

# 用户归还设备（严格校验，只能归还自己借的设备）
@app.route('/return_device', methods=['POST'])
def return_device():
    if 'username' not in session or session.get('role') != 'user':
        return redirect(url_for('login'))
    try:
        device_id = int(request.form['device_id'])
        return_count = int(request.form.get('return_count', 1))
    except Exception:
        return redirect(url_for('user_dashboard', return_msg="参数错误"))
    if return_count < 1:
        return redirect(url_for('user_dashboard', return_msg="归还数量必须大于0"))
    db = get_db()
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT id FROM users WHERE username=%s", (session['username'],))
            user = cursor.fetchone()
            if not user:
                return redirect(url_for('user_dashboard', return_msg="用户不存在"))
            cursor.execute("""
                SELECT record_id FROM device_record
                WHERE device_id=%s AND user_id=%s AND return_time IS NULL
                ORDER BY borrow_time ASC
                LIMIT %s
            """, (device_id, user['id'], return_count))
            records = cursor.fetchall()
            if not records or len(records) < return_count:
                return redirect(url_for('user_dashboard', return_msg="归还数量超过可归还数量"))
            record_ids = [r['record_id'] for r in records]
            if record_ids:
                format_strings = ','.join(['%s'] * len(record_ids))
                sql = f"UPDATE device_record SET return_time=NOW() WHERE record_id IN ({format_strings})"
                cursor.execute(sql, record_ids)
                db.commit()
    except Exception:
        return redirect(url_for('user_dashboard', return_msg="归还失败，请重试"))
    finally:
        db.close()
    return redirect(url_for('user_dashboard', return_msg=f"归还成功，共归还{return_count}台"))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)