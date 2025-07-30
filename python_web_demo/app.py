from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # ���� session�������Զ���

# �˵����ݣ���ǰ̨����һ�£��ɹ���
menu = {
    "��������": 28,
    "������˿": 25,
    "���Ŷ���": 18,
    "��������": 16,
    "�׷�": 2,
    "����": 5,
    "������": 10,
    "�Ǵ��Ｙ": 32,
    "�Ļƹ�": 12,
    "����������": 20
}

# ǰ̨ҳ��
@app.route('/')
def index():
    return render_template('index.html')

# ��̨����ҳ�棨��ȥ����¼У�飬ֱ�ӿɷ��ʣ�
@app.route('/admin')
def admin_panel():
    return render_template('admin.html', menu=menu)

# �˵�����API����ɾ�ģ�
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
            return jsonify({'status': 'fail', 'msg': '�۸�����'})
    elif action == 'delete' and name in menu:
        del menu[name]
        return jsonify({'status': 'ok', 'menu': menu})
    elif action == 'modify' and name and price and name in menu:
        try:
            menu[name] = float(price)
            return jsonify({'status': 'ok', 'menu': menu})
        except:
            return jsonify({'status': 'fail', 'msg': '�۸�����'})
    return jsonify({'status': 'fail', 'msg': '��������'})

if __name__ == '__main__':
    print("Flask app is starting...")   # ������ʾ��������ȷ�ϳ�����ִ��
    app.run(debug=True)