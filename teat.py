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

'''
APP

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
            # 先删除关联的借还记录
            cursor.execute("DELETE FROM device_record WHERE device_id=%s", (device_id,))
            # 再删除设备本身
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

# 用户首页：查询设备库存
@app.route('/user', methods=['GET'])
def user_dashboard():
    if 'username' not in session or session.get('role') != 'user':
        return redirect(url_for('login'))
    search_type = request.args.get('search_type')
    borrow_msg = request.args.get('borrow_msg')
    return_msg = request.args.get('return_msg')
    db = get_db()
    try:
        with db.cursor() as cursor:
            if search_type:
                cursor.execute("SELECT * FROM device WHERE device_type LIKE %s", ('%' + search_type + '%',))
            else:
                cursor.execute("SELECT * FROM device")
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
            # 插入多条借用记录
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
            # 查询该用户未归还的该设备的借用记录
            cursor.execute("""
                SELECT record_id FROM device_record
                WHERE device_id=%s AND user_id=%s AND return_time IS NULL
                ORDER BY borrow_time ASC
                LIMIT %s
            """, (device_id, user['id'], return_count))
            records = cursor.fetchall()
            if not records or len(records) < return_count:
                return redirect(url_for('user_dashboard', return_msg="归还数量超过可归还数量"))
            # 批量归还
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
'''


'''
admin

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>管理员首页</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* 注册页面样式迁移 */
        .background-layer {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url("{{ url_for('static', filename='images/admin-bg.png') }}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
            z-index: -2;
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

        body {
            margin: 0;
            min-height: 100vh;
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Oxygen',
                'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
            color: #a5b4fc;
            background: transparent;
        }

        /* 顶部操作栏 - 保持原有样式 */
        .ribbon-bar {
            background: transparent;
            border-bottom: none;
            padding: 0.5rem 1.5rem;
            display: flex;
            align-items: center;
            backdrop-filter: blur(5px);
        }

        /* 标签页按钮 - 保持原有样式 */
        .ribbon-tab {
            color: #a5b4fc;
            background: transparent;
            border: none;
            font-size: 1.1rem;
            margin-right: 2rem;
            padding: 0.6rem 1.8rem;
            border-radius: 12px 12px 0 0;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            z-index: 1;
            border-bottom: 2px solid transparent;
        }

        .ribbon-tab.active, .ribbon-tab:hover {
            color: #818cf8;
            border-bottom: 2px solid #818cf8;
        }

        /* 用户信息区域 */
        .ribbon-user {
            margin-left: auto;
            font-size: 1.1rem;
            color: #a5b4fc;
            display: flex;
            align-items: center;
        }

        .ribbon-logout {
            margin-left: 1.5rem;
            padding: 0.3rem 0.8rem;
            background: transparent;
            border: 1px solid #a5b4fc;
            border-radius: 8px;
            color: #a5b4fc;
            transition: all 0.3s ease;
        }

        .ribbon-logout:hover {
            background: #818cf833;
            color: #818cf8;
        }

        /* 内容卡片 - 完全透明 */
        .ribbon-content {
            background: transparent;
            border-radius: 0;
            box-shadow: none;
            padding: 2.5rem 3rem;
            margin: 2.5rem auto 0 auto;
            max-width: 960px;
            backdrop-filter: none;
        }

        /* 提示框样式 */
        .alert-info {
            background-color: transparent;
            color: #a5b4fc;
            border: none;
            border-left: 3px solid #818cf8;
            border-radius: 6px;
            padding: 0.8rem 1.2rem;
        }

        /* 表格样式 */
        .table th {
            background-color: transparent;
            color: #a5b4fc;
            font-weight: 500;
            border-bottom: 1px solid #818cf833;
        }

        .table td {
            vertical-align: middle;
            color: #a5b4fc;
            border-bottom: 1px solid #818cf811;
            background-color: transparent;
        }

        /* 表单控件增强 */
        .form-control {
            border-radius: 10px;
            padding: 0.6rem 1rem;
            border: 1px solid #818cf833;
            background-color: transparent;
            color: #a5b4fc;
            transition: all 0.2s ease;
        }

        .form-control:focus {
            border-color: #818cf8;
            box-shadow: 0 0 0 3px rgba(165, 180, 252, 0.2);
        }

        /* 按钮样式 */
        .btn {
            border-radius: 10px;
            padding: 0.5rem 1.5rem;
            font-weight: 500;
            transition: all 0.3s ease;
            border: none;
        }

        .btn-success {
            background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
        }

        .btn-primary {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        }

        .btn-danger {
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        }

        .btn-warning {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        }

        /* 响应式布局优化 */
        @media (max-width: 768px) {
            .ribbon-tab {
                margin-right: 1rem;
                font-size: 0.9rem;
            }

            .ribbon-content {
                padding: 1.5rem 2rem;
                margin: 1.5rem auto 0 auto;
            }
        }
    </style>
    <script>
        function showTab(tab) {
            document.querySelectorAll('.ribbon-tab').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.ribbon-section').forEach(sec => sec.style.display = 'none');
            document.getElementById(tab + '-tab').classList.add('active');
            document.getElementById(tab + '-section').style.display = 'block';
        }

        window.onload = function() {
            showTab('add');
        }

        function confirmDelete(deviceId) {
            if (confirm('确定要删除该设备吗？此操作不可恢复！')) {
                const form = document.getElementById('delete-form-' + deviceId);
                form.submit();
            }
        }
    </script>
</head>
<body>
    <!-- 背景图片层 -->
    <div class="background-layer"></div>
    <!-- 半透明遮罩层 -->
    <div class="overlay"></div>

    <div class="ribbon-bar">
        <button class="ribbon-tab" id="add-tab" onclick="showTab('add')">添加设备</button>
        <button class="ribbon-tab" id="search-tab" onclick="showTab('search')">设备查询</button>
        <button class="ribbon-tab" id="stat-tab" onclick="showTab('stat')">借还统计</button>
        <div class="ribbon-user">
            管理员：{{ username }}
            <a href="{{ url_for('logout') }}" class="btn btn-outline-primary btn-sm ribbon-logout">退出登录</a>
        </div>
    </div>

    <div class="ribbon-content position-relative">
        <!-- 添加设备 -->
        <div id="add-section" class="ribbon-section" style="display:none;">
            <h3 class="mb-4 text-primary">添加设备</h3>
            <form method="post" action="{{ url_for('add_device') }}" class="mb-4">
                <div class="row g-4">
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
                        <button type="submit" class="btn btn-success">添加</button>
                    </div>
                </div>
            </form>
            {% if add_msg %}
            <div class="alert alert-info mt-3">{{ add_msg }}</div>
            {% endif %}
        </div>

        <!-- 设备查询 -->
        <div id="search-section" class="ribbon-section" style="display:none;">
            <h3 class="mb-4 text-primary">设备查询</h3>
            <form method="get" action="{{ url_for('admin_dashboard') }}" class="mb-4">
                <div class="row g-3 justify-content-center">
                    <div class="col-md-5">
                        <input type="text" name="search_type" class="form-control" placeholder="输入设备类型进行模糊查询">
                    </div>
                    <div class="col-md-2 d-grid">
                        <button type="submit" class="btn btn-primary">查询</button>
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
                            <th>操作</th>
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
                            <td>
                                <form id="delete-form-{{ d.device_id }}" method="post" action="{{ url_for('delete_device') }}" style="display:inline;">
                                    <input type="hidden" name="device_id" value="{{ d.device_id }}">
                                    <button type="button" class="btn btn-danger btn-sm" onclick="confirmDelete({{ d.device_id }})">删除</button>
                                </form>
                            </td>
                        </tr>
                    {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>

        <!-- 借还统计 -->
        <div id="stat-section" class="ribbon-section" style="display:none;">
            <h3 class="mb-4 text-primary">借还统计</h3>
            <form method="get" action="{{ url_for('device_stat') }}" class="mb-4">
                <div class="row g-3 justify-content-center">
                    <div class="col-md-4">
                        <input type="datetime-local" name="start_time" class="form-control" required>
                    </div>
                    <div class="col-md-4">
                        <input type="datetime-local" name="end_time" class="form-control" required>
                    </div>
                    <div class="col-md-2 d-grid">
                        <button type="submit" class="btn btn-warning">统计</button>
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
</body>
</html>
'''

'''
user

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>用户首页</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* 背景图层 */
        .background-layer {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url("{{ url_for('static', filename='images/user-bg.png') }}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
            z-index: -2;
        }

        /* 半透明遮罩层 */
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.1);
            z-index: -1;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Oxygen',
                'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
            color: #a5b4fc;
            background: transparent;
        }

        /* 顶部操作栏 */
        .ribbon-bar {
            background: transparent;
            border-bottom: none;
            padding: 0.5rem 1.5rem;
            display: flex;
            align-items: center;
            backdrop-filter: blur(5px);
        }

        /* 标签页按钮 */
        .ribbon-tab {
            color: #a5b4fc;
            background: transparent;
            border: none;
            font-size: 1.1rem;
            margin-right: 2rem;
            padding: 0.6rem 1.8rem;
            border-radius: 12px 12px 0 0;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            z-index: 1;
            border-bottom: 2px solid transparent;
        }

        .ribbon-tab.active, .ribbon-tab:hover {
            color: #818cf8;
            border-bottom: 2px solid #818cf8;
        }

        /* 用户信息区域 */
        .ribbon-user {
            margin-left: auto;
            font-size: 1.1rem;
            color: #a5b4fc;
            display: flex;
            align-items: center;
        }

        .ribbon-logout {
            margin-left: 1.5rem;
            padding: 0.3rem 0.8rem;
            background: transparent;
            border: 1px solid #a5b4fc;
            border-radius: 8px;
            color: #a5b4fc;
            transition: all 0.3s ease;
        }

        .ribbon-logout:hover {
            background: #818cf833;
            color: #818cf8;
        }

        /* 内容卡片 */
        .ribbon-content {
            background: transparent;
            border-radius: 0;
            box-shadow: none;
            padding: 2.5rem 3rem;
            margin: 2.5rem auto 0 auto;
            max-width: 960px;
            backdrop-filter: none;
        }

        /* 提示框样式 */
        .alert-info {
            background-color: transparent;
            color: #a5b4fc;
            border: none;
            border-left: 3px solid #818cf8;
            border-radius: 6px;
            padding: 0.8rem 1.2rem;
        }

        /* 表格样式 */
        .table th {
            background-color: transparent;
            color: #a5b4fc;
            font-weight: 500;
            border-bottom: 1px solid #818cf833;
        }

        .table td {
            vertical-align: middle;
            color: #a5b4fc;
            border-bottom: 1px solid #818cf811;
            background-color: transparent;
        }

        /* 表单控件 */
        .form-control {
            border-radius: 10px;
            padding: 0.6rem 1rem;
            border: 1px solid #818cf833;
            background-color: transparent;
            color: #a5b4fc;
            transition: all 0.2s ease;
        }

        .form-control:focus {
            border-color: #818cf8;
            box-shadow: 0 0 0 3px rgba(165, 180, 252, 0.2);
        }

        /* 按钮样式 */
        .btn {
            border-radius: 10px;
            padding: 0.5rem 1.5rem;
            font-weight: 500;
            transition: all 0.3s ease;
            border: none;
        }

        .btn-primary {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        }

        .btn-success {
            background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
        }

        .btn-warning {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        }

        /* 响应式布局 */
        @media (max-width: 768px) {
            .ribbon-tab {
                margin-right: 1rem;
                font-size: 0.9rem;
            }

            .ribbon-content {
                padding: 1.5rem 2rem;
                margin: 1.5rem auto 0 auto;
            }
        }
    </style>
    <script>
        function showTab(tab) {
            document.querySelectorAll('.ribbon-tab').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.ribbon-section').forEach(sec => sec.style.display = 'none');
            document.getElementById(tab + '-tab').classList.add('active');
            document.getElementById(tab + '-section').style.display = 'block';
        }

        window.onload = function() {
            showTab('search');
        }
    </script>
</head>
<body>
    <div class="background-layer"></div>
    <div class="overlay"></div>
    <div class="ribbon-bar">
        <button class="ribbon-tab" id="search-tab" onclick="showTab('search')">设备查询</button>
        <button class="ribbon-tab" id="borrow-tab" onclick="showTab('borrow')">借出设备</button>
        <button class="ribbon-tab" id="return-tab" onclick="showTab('return')">归还设备</button>
        <div class="ribbon-user">
            用户：{{ username }}
            <a href="{{ url_for('logout') }}" class="btn btn-outline-primary btn-sm ribbon-logout">退出登录</a>
        </div>
    </div>
    <div class="ribbon-content position-relative">
        <!-- 设备查询 -->
        <div id="search-section" class="ribbon-section" style="display:none;">
            <h3 class="mb-4 text-primary">设备库存查询</h3>
            <form method="get" action="{{ url_for('user_dashboard') }}" class="mb-4">
                <div class="row g-3">
                    <div class="col-md-6">
                        <input type="text" name="search_type" class="form-control" placeholder="输入设备类型进行模糊查询">
                    </div>
                    <div class="col-md-4">
                        <input type="text" name="search_model" class="form-control" placeholder="输入设备型号进行模糊查询">
                    </div>
                    <div class="col-md-2 d-grid">
                        <button type="submit" class="btn btn-primary">查询</button>
                    </div>
                </div>
            </form>
            <div class="table-responsive">
                <table class="table table-bordered table-hover align-middle">
                    <thead>
                        <tr>
                            <th>设备ID</th>
                            <th>类型</th>
                            <th>型号</th>
                            <th>价格</th>
                            <th>库存现货</th>
                        </tr>
                    </thead>
                    <tbody>
                    {% for d in devices %}
                        <tr>
                            <td>{{ d.device_id }}</td>
                            <td>{{ d.device_type }}</td>
                            <td>{{ d.device_model }}</td>
                            <td>{{ d.device_price }}</td>
                            <td>{{ d.stock_quantity }}</td>
                        </tr>
                    {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        <!-- 借出设备 -->
        <div id="borrow-section" class="ribbon-section" style="display:none;">
            <h3 class="mb-4 text-primary">借出设备</h3>
            <form method="post" action="{{ url_for('borrow_device') }}" class="mb-4">
                <div class="row g-3">
                    <div class="col-md-4">
                        <input type="number" name="device_id" class="form-control" placeholder="设备ID" required>
                    </div>
                    <div class="col-md-4">
                        <input type="number" name="borrow_count" class="form-control" placeholder="借出数量(最多5台)" min="1" max="5" required>
                    </div>
                    <div class="col-md-4 d-grid">
                        <button type="submit" class="btn btn-success">借出</button>
                    </div>
                </div>
            </form>
            {% if borrow_msg %}
                <div class="alert alert-info">{{ borrow_msg }}</div>
            {% endif %}
        </div>
        <!-- 归还设备 -->
        <div id="return-section" class="ribbon-section" style="display:none;">
            <h3 class="mb-4 text-primary">归还设备</h3>
            <form method="post" action="{{ url_for('return_device') }}" class="mb-4">
                <div class="row g-3">
                    <div class="col-md-4">
                        <input type="number" name="device_id" class="form-control" placeholder="设备ID" required>
                    </div>
                    <div class="col-md-4">
                        <input type="number" name="return_count" class="form-control" placeholder="归还数量" min="1" required>
                    </div>
                    <div class="col-md-4 d-grid">
                        <button type="submit" class="btn btn-warning">归还</button>
                    </div>
                </div>
            </form>
            {% if return_msg %}
                <div class="alert alert-info">{{ return_msg }}</div>
            {% endif %}
        </div>
    </div>
</body>
</html>'''