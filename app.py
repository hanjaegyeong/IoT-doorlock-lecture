from flask import Flask, render_template
app = Flask(__name__)

# http://127.0.0.1:500/abc 주소의 페이지 만들기
@app.route('/abc',methods=['GET'])
def abc():
    return 'hello'

# 파이썬 변수 출력하기
@app.route('/a1', methods=['GET'])
def a1():
    num = 1
    return render_template('view1.html',  number = num)

# 파이썬 변수 넣은 버튼, 클릭하면 /a1 주소로 이동
@app.route('/a2', methods=['GET'])
def a2():
    good = 5
    return render_template('view2.html', good = good)


if __name__ == '__main__':
    app.run(port = 5000, debug = True)
