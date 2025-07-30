前后端运行步骤
1. 安装 Python 和 Flask
安装 Python 3.6 及以上
安装 Flask（命令行执行）：
bash
pip install flask
2. 准备后端代码
将你整理好的 app.py 放在 python_web_demo 目录下。
确保 templates 目录下有 index.html 和 admin.html。
3. 运行 Flask 后端
进入项目目录，命令行输入：

bash
cd python_web_demo
python app.py
若一切正常，命令行会输出：

Code
Flask app is starting...
 * Serving Flask app "app"
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
4. 访问前后端页面
前台页面：http://127.0.0.1:5000/
后台管理：http://127.0.0.1:5000/admin
如果你的 HTML 里有引用 static 文件夹下的 CSS/JS，Flask 会自动处理。

