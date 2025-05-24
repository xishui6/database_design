'''
登录界面
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* ...你的样式不变... */
    </style>
</head>
<body>
<div class="overlay"></div>
<div class="container d-flex align-items-center justify-content-center">
    <div class="login-container">
        <h2 class="text-center mb-4">登录</h2>
        {% if error %}
        <div class="alert alert-danger text-center">{{ error }}</div>
        {% endif %}
        <form method="post">
            <div class="mb-3">
                <label for="username" class="form-label">用户名</label>
                <input type="text" class="form-control" name="username" placeholder="请输入用户名" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">密码</label>
                <input type="password" class="form-control" name="password" placeholder="请输入密码" required>
            </div>
            <div class="mb-3">
                <label class="form-label">身份</label>
                <select class="form-select" name="role" required>
                    <option value="user" {% if selected_role == 'user' %}selected{% endif %}>普通用户</option>
                    <option value="admin" {% if selected_role == 'admin' %}selected{% endif %}>管理员</option>
                </select>
            </div>
            <div class="d-grid">
                <button type="submit" class="btn btn-primary btn-lg">登录</button>
            </div>
        </form>
        <div class="text-center mt-3">
            <p class="text-white">还没有账号？<a href="{{ url_for('register') }}" class="text-white text-decoration-underline">注册</a></p>
        </div>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''
'''
注册界面
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>注册</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* ...你的样式不变... */
    </style>
</head>
<body>
<div class="overlay"></div>
<div class="container d-flex align-items-center justify-content-center">
    <div class="register-container">
        <h2 class="text-center mb-4">注册</h2>
        {% if error %}
        <div class="alert alert-danger text-center">{{ error }}</div>
        {% endif %}
        <form method="post">
            <div class="mb-3">
                <label for="username" class="form-label">用户名</label>
                <input type="text" class="form-control" name="username" placeholder="请输入用户名" required value="{{ username|default('') }}">
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">密码</label>
                <input type="password" class="form-control" name="password" placeholder="请输入密码" required>
            </div>
            <div class="mb-3">
                <label for="confirm_password" class="form-label">确认密码</label>
                <input type="password" class="form-control" name="confirm_password" placeholder="请再次输入密码" required>
            </div>
            <div class="mb-3">
                <label class="form-label">身份</label>
                <select class="form-select" name="role" required>
                    <option value="user" {% if selected_role == 'user' %}selected{% endif %}>普通用户</option>
                    <option value="admin" {% if selected_role == 'admin' %}selected{% endif %}>管理员</option>
                </select>
            </div>
            <div class="d-grid">
                <button type="submit" class="btn btn-success btn-lg">注册</button>
            </div>
        </form>
        <div class="text-center mt-3">
            <p class="text-white">已有账号？<a href="{{ url_for('login') }}" class="text-white text-decoration-underline">去登录</a></p>
        </div>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''
'''
admin界面
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>管理员首页</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>欢迎管理员：{{ username }}</h1>
        <a href="{{ url_for('logout') }}" class="btn btn-danger mt-3">退出登录</a>
    </div>
</body>
</html>
'''
'''
user界面
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>用户首页</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>欢迎用户：{{ username }}</h1>
        <a href="{{ url_for('logout') }}" class="btn btn-danger mt-3">退出登录</a>
    </div>
</body>
</html>
'''
'''
index界面
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>设备管理系统</title>

    <!-- 引入 Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- 自定义样式：设置背景图 -->
    <style>
        body {
            margin: 0;
            padding: 0;
            background-image: url("{{ url_for('static', filename='images/background.png') }}");
            background-size: cover; /* 背景图覆盖整个页面 */
            background-repeat: no-repeat; /* 不重复 */
            background-position: center; /* 居中显示 */
            background-attachment: fixed; /* 背景固定，滚动页面时背景不动 */
            color: white; /* 设置文字颜色，确保文字可见 */
        }

        .content {
            background-color: rgba(0, 0, 0, 0.5); /* 半透明背景，增强文字对比度 */
            padding: 2rem;
            border-radius: 10px;
        }
    </style>
</head>
<body>

    <!-- 页面内容 -->
    <div class="container d-flex align-items-center justify-content-center flex-column min-vh-100">
        <div class="content text-center">
            <h1 class="display-4 text-white">你好，欢迎使用设备管理系统</h1>
            <p class="lead text-white">本系统用于管理实验室设备信息</p>
            <a href="/devices" class="btn btn-primary btn-lg mt-3">进入系统</a>
        </div>
    </div>

    <!-- 引入 Bootstrap 5 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <a href="/logout" class="btn btn-danger">退出登录</a>
</body>
</html>
'''
'''
主界面
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
            if role == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
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
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/admin')
def admin_dashboard():
    if 'username' in session and session.get('role') == 'admin':
        return render_template('admin.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/user')
def user_dashboard():
    if 'username' in session and session.get('role') == 'user':
        return render_template('user.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
'''
'''
主界面
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
            # 登录成功，渲染带 success 标志的 login.html
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
        # 注册成功，渲染带 success 标志的 register.html
        return render_template('register.html', register_success=True)
    return render_template('register.html')

@app.route('/admin')
def admin_dashboard():
    if 'username' in session and session.get('role') == 'admin':
        return render_template('admin.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/user')
def user_dashboard():
    if 'username' in session and session.get('role') == 'user':
        return render_template('user.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
'''
'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>管理员首页</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            margin: 0;
            min-height: 100vh;
            background: url('/static/images/admin-bg.jpg') no-repeat center center fixed;
            background-size: cover;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .overlay {
            background-color: rgba(255, 255, 255, 0.92);
            border-radius: 15px;
            box-shadow: 0 0 25px rgba(0,0,0,0.1);
            padding: 2rem;
            margin-top: 2rem;
        }
        
        .welcome-card {
            background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }
        
        .form-control:focus {
            box-shadow: 0 0 0 0.2rem rgba(79, 70, 229, 0.25);
            border-color: #4f46e5;
        }
        
        .btn-custom {
            border-radius: 8px;
            padding: 0.4rem 1.2rem;
            transition: all 0.3s ease;
        }
        
        .btn-custom:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .table th {
            background-color: #4f46e5;
            color: white;
            border-color: #e5e7eb;
        }
        
        .alert-info {
            background-color: #dbeafe;
            color: #1e40af;
            border: none;
            border-left: 4px solid #3b82f6;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-10 col-lg-8 overlay">
            <!-- Welcome Card -->
            <div class="welcome-card text-center mb-4 p-4">
                <h1 class="display-6 mb-3">欢迎管理员：{{ username }}</h1>
                <a href="{{ url_for('logout') }}" class="btn btn-light btn-custom">退出登录</a>
            </div>

            <!-- 1. 添加设备及入库 -->
            <div class="mb-5">
                <h3 class="text-center mb-4 text-primary">添加设备</h3>
                <form method="post" action="{{ url_for('add_device') }}" class="mb-4">
                    <div class="row g-3">
                        <div class="col-md-3">
                            <input type="text" name="device_type" class="form-control" placeholder="设备类型" required>
                        </div>
                        <div class="col-md-3">
                            <input type="number" step="0.01" name="device_price" class="form-control" placeholder="设备价格" required>
                        </div>
                        <div class="col-md-3">
                            <input type="number" name="stock_quantity" class="form-control" placeholder="入库数量" required>
                        </div>
                        <div class="col-md-3 d-grid">
                            <button type="submit" class="btn btn-success btn-custom">添加</button>
                        </div>
                    </div>
                </form>
                {% if add_msg %}
                    <div class="alert alert-info">{{ add_msg }}</div>
                {% endif %}
            </div>

            <!-- 2. 查询设备 -->
            <div class="mb-5">
                <h3 class="text-center mb-4 text-primary">设备查询</h3>
                <form method="get" action="{{ url_for('admin_dashboard') }}" class="mb-4">
                    <div class="row g-3 justify-content-center">
                        <div class="col-md-5">
                            <input type="text" name="search_type" class="form-control" placeholder="输入设备类型进行查询">
                        </div>
                        <div class="col-md-2 d-grid">
                            <button type="submit" class="btn btn-primary btn-custom">查询</button>
                        </div>
                    </div>
                </form>
                
                <div class="table-responsive">
                    <table class="table table-bordered table-hover align-middle">
                        <thead>
                            <tr>
                                <th>设备ID</th>
                                <th>类型</th>
                                <th>价格</th>
                                <th>库存现货</th>
                                <th>借出时间</th>
                                <th>归还时间</th>
                            </tr>
                        </thead>
                        <tbody>
                        {% for d in devices %}
                            <tr>
                                <td>{{ d.device_id }}</td>
                                <td>{{ d.device_type }}</td>
                                <td>{{ d.device_price }}</td>
                                <td>{{ d.stock_quantity }}</td>
                                <td>{{ d.borrow_time or '-' }}</td>
                                <td>{{ d.return_time or '-' }}</td>
                            </tr>
                        {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- 3. 统计借还数量 -->
            <div>
                <h3 class="text-center mb-4 text-primary">借还统计</h3>
                <form method="get" action="{{ url_for('device_stat') }}" class="mb-4">
                    <div class="row g-3 justify-content-center">
                        <div class="col-md-4">
                            <input type="datetime-local" name="start_time" class="form-control" required>
                        </div>
                        <div class="col-md-4">
                            <input type="datetime-local" name="end_time" class="form-control" required>
                        </div>
                        <div class="col-md-2 d-grid">
                            <button type="submit" class="btn btn-warning btn-custom">统计</button>
                        </div>
                    </div>
                </form>
                
                {% if stat_result %}
                <div class="table-responsive">
                    <table class="table table-bordered align-middle">
                        <thead>
                            <tr>
                                <th>设备ID</th>
                                <th>类型</th>
                                <th>借出次数</th>
                                <th>归还次数</th>
                            </tr>
                        </thead>
                        <tbody>
                        {% for s in stat_result %}
                            <tr>
                                <td>{{ s.device_id }}</td>
                                <td>{{ s.device_type }}</td>
                                <td>{{ s.borrow_count }}</td>
                                <td>{{ s.return_count }}</td>
                            </tr>
                        {% endfor %}
                        </tbody>
                    </table>
                </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>
</body>
</html>
'''

'''
admin界面
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>管理员首页</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h1>欢迎管理员：{{ username }}</h1>
    <a href="{{ url_for('logout') }}" class="btn btn-danger mt-3 mb-4">退出登录</a>

    <!-- 1. 添加设备及入库 -->
    <h3>添加设备</h3>
    <form method="post" action="{{ url_for('add_device') }}" class="mb-4">
        <div class="row g-2">
            <div class="col"><input type="text" name="device_type" class="form-control" placeholder="设备类型" required></div>
            <div class="col"><input type="number" step="0.01" name="device_price" class="form-control" placeholder="设备价格" required></div>
            <div class="col"><input type="number" name="stock_quantity" class="form-control" placeholder="入库数量" required></div>
            <div class="col"><button type="submit" class="btn btn-success">添加</button></div>
        </div>
    </form>
    {% if add_msg %}
        <div class="alert alert-info">{{ add_msg }}</div>
    {% endif %}

    <!-- 2. 查询设备 -->
    <h3>设备查询</h3>
    <form method="get" action="{{ url_for('admin_dashboard') }}" class="mb-3">
        <div class="row g-2">
            <div class="col"><input type="text" name="search_type" class="form-control" placeholder="设备类型"></div>
            <div class="col"><button type="submit" class="btn btn-primary">查询</button></div>
        </div>
    </form>
    <table class="table table-bordered table-hover">
        <thead>
            <tr>
                <th>设备ID</th>
                <th>类型</th>
                <th>价格</th>
                <th>库存现货</th>
                <th>借出时间</th>
                <th>归还时间</th>
            </tr>
        </thead>
        <tbody>
        {% for d in devices %}
            <tr>
                <td>{{ d.device_id }}</td>
                <td>{{ d.device_type }}</td>
                <td>{{ d.device_price }}</td>
                <td>{{ d.stock_quantity }}</td>
                <td>{{ d.borrow_time or '-' }}</td>
                <td>{{ d.return_time or '-' }}</td>
            </tr>
        {% endfor %}
        </tbody>
    </table>

    <!-- 3. 统计借还数量 -->
    <h3>借还统计</h3>
    <form method="get" action="{{ url_for('device_stat') }}" class="mb-3">
        <div class="row g-2">
            <div class="col"><input type="datetime-local" name="start_time" class="form-control" required></div>
            <div class="col"><input type="datetime-local" name="end_time" class="form-control" required></div>
            <div class="col"><button type="submit" class="btn btn-warning">统计</button></div>
        </div>
    </form>
    {% if stat_result %}
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>设备ID</th>
                <th>类型</th>
                <th>借出次数</th>
                <th>归还次数</th>
            </tr>
        </thead>
        <tbody>
        {% for s in stat_result %}
            <tr>
                <td>{{ s.device_id }}</td>
                <td>{{ s.device_type }}</td>
                <td>{{ s.borrow_count }}</td>
                <td>{{ s.return_count }}</td>
            </tr>
        {% endfor %}
        </tbody>
    </table>
    {% endif %}
</div>
</body>
</html>
'''

'''
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
    add_msg = request.args.get('add_msg')
    db = get_db()
    with db.cursor() as cursor:
        if search_type:
            cursor.execute("""
                SELECT d.device_id, d.device_type, d.device_price, d.stock_quantity,
                       r.borrow_time, r.return_time
                FROM device d
                LEFT JOIN device_record r ON d.device_id = r.device_id
                WHERE d.device_type LIKE %s
                ORDER BY d.device_id DESC
            """, ('%' + search_type + '%',))
        else:
            cursor.execute("""
                SELECT d.device_id, d.device_type, d.device_price, d.stock_quantity,
                       r.borrow_time, r.return_time
                FROM device d
                LEFT JOIN device_record r ON d.device_id = r.device_id
                ORDER BY d.device_id DESC
            """)
        devices = cursor.fetchall()
    db.close()
    return render_template('admin.html', username=session['username'], devices=devices, add_msg=add_msg, stat_result=None)

# 添加设备及入库
@app.route('/add_device', methods=['POST'])
def add_device():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))
    device_type = request.form['device_type']
    device_price = request.form['device_price']
    stock_quantity = request.form['stock_quantity']
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute(
            "INSERT INTO device (device_type, device_price, stock_in_time, stock_quantity) VALUES (%s, %s, NOW(), %s)",
            (device_type, device_price, stock_quantity)
        )
        db.commit()
    db.close()
    return redirect(url_for('admin_dashboard', add_msg='设备添加成功'))

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
                SELECT d.device_id, d.device_type,
                    SUM(CASE WHEN r.borrow_time BETWEEN %s AND %s THEN 1 ELSE 0 END) AS borrow_count,
                    SUM(CASE WHEN r.return_time BETWEEN %s AND %s THEN 1 ELSE 0 END) AS return_count
                FROM device d
                LEFT JOIN device_record r ON d.device_id = r.device_id
                GROUP BY d.device_id, d.device_type
            """, (start_time, end_time, start_time, end_time))
            stat_result = cursor.fetchall()
        db.close()
    # 设备列表也要查出来
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute("""
            SELECT d.device_id, d.device_type, d.device_price, d.stock_quantity,
                   r.borrow_time, r.return_time
            FROM device d
            LEFT JOIN device_record r ON d.device_id = r.device_id
            ORDER BY d.device_id DESC
        """)
        devices = cursor.fetchall()
    db.close()
    return render_template('admin.html', username=session['username'], devices=devices, stat_result=stat_result, add_msg=None)

@app.route('/user')
def user_dashboard():
    if 'username' in session and session.get('role') == 'user':
        return render_template('user.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
'''

'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            background-image: url("{{ url_for('static', filename='images/login_background.png') }}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
            color: white;
            font-family: "Microsoft YaHei", sans-serif;
        }
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.1);
            z-index: -1;
        }
        .login-container {
            max-width: 400px;
            margin-top: 150px;
            padding: 2rem;
            border-radius: 15px;
            background-color: rgba(255, 255, 255, 0.05);
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
        }
        .login-container h2 { color: #fff; }
        .login-container .form-control,
        .login-container .form-select {
            background-color: rgba(255, 255, 255, 0.1);
            color: #fff;
            border: none;
        }
        .login-container .form-control::placeholder { color: #ddd; }
        .login-container .btn { background-color: #007bff; border: none; }
        .login-container .btn:hover { background-color: #0056b3; }
        .login-container .text-white a { text-decoration: underline; }
        /* 动画样式 */
        .success-animation {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #28a745;
            font-size: 2rem;
            margin-top: 40px;
        }
        .checkmark {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            display: block;
            stroke-width: 4;
            stroke: #28a745;
            stroke-miterlimit: 10;
            box-shadow: 0 0 20px #28a74544;
            margin: 0 auto 20px auto;
            background: #fff;
        }
        .checkmark__circle {
            stroke-dasharray: 166;
            stroke-dashoffset: 166;
            animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
        }
        .checkmark__check {
            stroke-dasharray: 48;
            stroke-dashoffset: 48;
            animation: stroke 0.4s 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
        }
        @keyframes stroke {
            100% { stroke-dashoffset: 0; }
        }
    </style>
</head>
<body>
<div class="overlay"></div>
<div class="container d-flex align-items-center justify-content-center">
    <div class="login-container">
        {% if login_success %}
            <div class="success-animation">
                <svg class="checkmark" viewBox="0 0 52 52">
                    <circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none"/>
                    <path class="checkmark__check" fill="none" d="M14 27l7 7 16-16"/>
                </svg>
                <div>登录成功！正在进入系统...</div>
            </div>
            <script>
                setTimeout(function() {
                    window.location.href = "{{ url_for('index') }}";
                }, 2000);
            </script>
        {% else %}
            <h2 class="text-center mb-4">登录</h2>
            {% if error %}
            <div class="alert alert-danger text-center">{{ error }}</div>
            {% endif %}
            <form method="post">
                <div class="mb-3">
                    <label for="username" class="form-label">用户名</label>
                    <input type="text" class="form-control" name="username" placeholder="请输入用户名" required>
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">密码</label>
                    <input type="password" class="form-control" name="password" placeholder="请输入密码" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">身份</label>
                    <select class="form-select" name="role" required>
                        <option value="user" {% if selected_role == 'user' %}selected{% endif %}>普通用户</option>
                        <option value="admin" {% if selected_role == 'admin' %}selected{% endif %}>管理员</option>
                    </select>
                </div>
                <div class="d-grid">
                    <button type="submit" class="btn btn-primary btn-lg">登录</button>
                </div>
            </form>
            <div class="text-center mt-3">
                <p class="text-white">还没有账号？<a href="{{ url_for('register') }}" class="text-white">注册</a></p>
            </div>
        {% endif %}
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''