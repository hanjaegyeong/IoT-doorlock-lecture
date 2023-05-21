import random
from flask import Flask, render_template, request
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




#3번째 수업!

# 일반리스트 버튼출력
@app.route('/a', methods=['GET'])
def a():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    return render_template('a.html', numbers = numbers)






# 랜덤리스트 버튼출력 - import
@app.route('/b', methods=['GET'])
def b():
    random_list = list(range(0,10))
    numbers = random.sample(random_list, 10)
    return render_template('b.html', numbers = numbers)





# 특수기호 포함 랜덤리스트 버튼출력
@app.route('/c', methods=['GET'])
def c():
    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    numbers = random.sample(random_list, 12)
    return render_template('c.html', numbers = numbers)







# 패스워드를 1로 설정하고, 다른값이 들어오면 도어락을 끝내보자
# 패스워드 설정 - import 
@app.route('/d', methods=['GET'])
def d():
    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    numbers = random.sample(random_list, 12)
    return render_template('e.html', numbers = numbers)









# d에서 입력한 값이 1 이 아니면 view1 띄우게 하자
# 패스워드 설정2
@app.route('/e', methods=['GET'])
def e():
    password = '1'
    # d에서 GET받은 number 가져다쓰기!
    number = request.args["number"]

    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    numbers = random.sample(random_list, 12)
    
    if password == number:
        return render_template('a.html', numbers = numbers)
    else:
        return render_template('view1.html', numbers = numbers)








# e 리턴페이지 f로 바꿔서 d~g 까지 이어지도록 해보자
@app.route('/f', methods=['GET'])
def f():
    password = '2'
    number = request.args["number"]

    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    numbers = random.sample(random_list, 12)
    
    if password == number:
        return render_template('g.html', numbers = numbers)
    else:
        return render_template('view1.html', numbers = numbers)








@app.route('/g', methods=['GET'])
def g():
    password = '3'
    number = request.args["number"]

    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    numbers = random.sample(random_list, 12)
    
    if password == number:
        return render_template('a.html', numbers = numbers)
    else:
        return render_template('view1.html', numbers = numbers)


if __name__ == '__main__':
    app.run(port = 5000, debug = True)
