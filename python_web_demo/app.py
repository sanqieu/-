from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 用于 session，可以自定义

# 菜单数据（与前台保持一致，可管理）
menu = {
    "宫保鸡丁": 28,
    "鱼香肉丝": 25,
    "麻婆豆腐": 18,
    "红烧茄子": 16,
    "米饭": 2,
    "可乐": 5,
    "酸辣汤": 10,
    "糖醋里脊": 32,
    "拍黄瓜": 12,
    "西红柿炒蛋": 20
}

# 前台页面
@app.route('/')
def index():
    return render_template('index.html')

# 后台管理页面（已去除登录校验，直接可访问）
@app.route('/admin')
def admin_panel():
    return render_template('admin.html', menu=menu)

# 菜单管理API（增删改）
@app.route('/admin/menu', methods=['POST'])
def admin_menu_api():
    action = request.form.get('action')
    name = request.form.get('name')
    price = request.form.get('price')
    if action == 'add' and name and price:
        try:
            menu[name] = float(price)
            return jsonify({'status': 'ok', 'menu': menu})
        except:
            return jsonify({'status': 'fail', 'msg': '价格有误'})
    elif action == 'delete' and name in menu:
        del menu[name]
        return jsonify({'status': 'ok', 'menu': menu})
    elif action == 'modify' and name and price and name in menu:
        try:
            menu[name] = float(price)
            return jsonify({'status': 'ok', 'menu': menu})
        except:
            return jsonify({'status': 'fail', 'msg': '价格有误'})
    return jsonify({'status': 'fail', 'msg': '参数错误'})

if __name__ == '__main__':
    print("Flask app is starting...")   # 启动提示，方便你确认程序已执行
    app.run(debug=True)