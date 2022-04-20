from bson.objectid import ObjectId
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import base64
import pprint
from sshtunnel import SSHTunnelForwarder
from flask import Flask, jsonify, render_template, url_for, redirect, session

import pymongo
import bcrypt
import json
from pymongo import results
from pymongo import MongoClient


from flask_login import login_user, logout_user, login_required, LoginManager, current_user
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
import datetime

from roleacc import roles_required


app = Flask(__name__, template_folder='template')


# เชื่อมฐานข้อมูล
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["parkingtest"]
mycol = mydb["f_other"]
mycol2 = mydb["f2"]
mycol3 = mydb["f3"]
mycol4 = mydb["f4"]


# # ดึงข้อมูลชั้น 2
# @app.route('/getdataf2', methods=['GET'])
# def getdata():
#     output = []
#     for a in mycol2.find():
#         output.append(
#             {'count_IN': a['count_IN'], 'count_OUT': a['count_OUT'], 'currentTime': a['currentTime'], })
#     return jsonify(output)

# # ดึงข้อมูลชั้น 3


# @app.route('/getdataf3', methods=['GET'])
# def getdataf3():
#     output = []
#     for a in mycol3.find():
#         output.append(
#             {'count_IN': a['count_IN'], 'count_OUT': a['count_OUT'], 'currentTime': a['currentTime']})
#     return jsonify(output)


# # ดึงข้อมูลชั้น 4
# @app.route('/getdataf4', methods=['GET'])
# def getdataf4():
#     output = []
#     for a in mycol4.find():
#         output.append(
#             {'count_IN': a['count_IN'], 'count_OUT': a['count_OUT'], 'currentTime': a['currentTime']})
#     return jsonify(output)




# หน้าแรก
@app.route('/nstda/parking/home')
@login_required
# @roles_required('admin')
def home():
    # return render_template('home.html', role_required=user_rold(), email_required= user_email())
    return render_template('home.html', roles_required=(str(check_user_rold())).split(","))

# หน้าประวัติ
@app.route('/nstda/parking/history')
@login_required
def history():
    return render_template('history.html', roles_required=(str(check_user_rold())).split(","))

# หน้ากล้อง
# ไม่ได้ใช่แล้ว
# @app.route('/nstda/parking/device')
# def device():
#     return render_template('device.html')


@app.route('/nstda/parking/devicenew')
@login_required
def devicenew():
    return render_template('devicenew.html', roles_required=(str(check_user_rold())).split(","))


@app.route('/nstda/parking/devicehistory1')
@login_required
def devicehistory1():
    return render_template('devicehistory1.html')


@app.route('/nstda/parking/devicehistory2')
@login_required
def devicehistory2():
    return render_template('devicehistory2.html')


@app.route('/nstda/parking/devicehistory3')
@login_required
def devicehistory3():
    return render_template('devicehistory3.html')


@app.route('/nstda/parking/devicehistory4')
@login_required
def devicehistory4():
    return render_template('devicehistory4.html')


@app.route('/nstda/parking/devicehistory5')
@login_required
def devicehistory5():
    return render_template('devicehistory5.html')


@app.route('/nstda/parking/devicehistory6')
@login_required
def devicehistory6():
    return render_template('devicehistory6.html')


@app.route('/nstda/parking/devicehistory7')
@login_required
def devicehistory7():
    return render_template('devicehistory7.html')


@app.route('/nstda/parking/devicehistory8')
@login_required
def devicehistory8():
    return render_template('devicehistory8.html')


@app.route('/nstda/parking/deviceinfo1')
@login_required
def deviceinfo1():
    return render_template('deviceinfo1.html')


@app.route('/nstda/parking/deviceinfo2')
@login_required
def deviceinfo2():
    return render_template('deviceinfo2.html')


@app.route('/nstda/parking/deviceinfo3')
@login_required
def deviceinfo3():
    return render_template('deviceinfo3.html')


@app.route('/nstda/parking/deviceinfo4')
@login_required
def deviceinfo4():
    return render_template('deviceinfo4.html')


@app.route('/nstda/parking/deviceinfo5')
@login_required
def deviceinfo5():
    return render_template('deviceinfo5.html')


@app.route('/nstda/parking/deviceinfo6')
@login_required
def deviceinfo6():
    return render_template('deviceinfo6.html')


@app.route('/nstda/parking/deviceinfo7')
@login_required
def deviceinfo7():
    return render_template('deviceinfo7.html')


@app.route('/nstda/parking/deviceinfo8')
@login_required
def deviceinfo8():
    return render_template('deviceinfo8.html')


@app.route('/nstda/parking/contact')
@login_required
def contact():
    return render_template('contact.html', roles_required=(str(check_user_rold())).split(","))


@app.route('/nstda/parking/update')
@login_required
def deviceupdate():
    return render_template('update.html', roles_required=(str(check_user_rold())).split(","))


@app.route('/nstda/parking/adddevice1')
@login_required
def adddevice1():
    return render_template('adddevice1.html', roles_required=(str(check_user_rold())).split(","))


@app.route('/nstda/parking/adddevice2')
@login_required
def adddevice2():
    return render_template('adddevice2.html', roles_required=(str(check_user_rold())).split(","))




# # ดึงข้อมูลกล้องตัวที่ 1
# @app.route('/getdatadevice1', methods=['GET'])  # ดึงข้อมูลกล้อง 1
# def getdatadevice1():
#     output = []
#     for a in mycol2.find({'id': 'Camrea_id:B12F02N01'}):
#         output.append({'id': a['id'], 'building': a['building'], 'floor': a['floor'], 'event': a['event'], 'count_IN': a['count_IN'],
#                       'count_OUT': a['count_OUT'], 'currentTime': a['currentTime'], 'image': a['image'], 'restartTime': a['restartTime']})
#     return jsonify(output)

# # ดึงข้อมูลกล้องตัวที่ 2


# @app.route('/getdatadevice2', methods=['GET'])  # ดึงข้อมูลกล้อง 2
# def getdatadevice2():
#     output = []
#     for a in mycol2.find({'id': 'Camrea_id:B12F02N02'}):
#         output.append({'id': a['id'], 'building': a['building'], 'floor': a['floor'], 'event': a['event'], 'count_IN': a['count_IN'],
#                       'count_OUT': a['count_OUT'], 'currentTime': a['currentTime'], 'image': a['image'], 'restartTime': a['restartTime']})
#     return jsonify(output)

# # ดึงข้อมูลกล้องตัวที่ 3


# @app.route('/getdatadevice3', methods=['GET'])  # ดึงข้อมูลกล้อง 3
# def getdatadevice3():
#     output = []
#     for a in mycol2.find({'id': 'Camrea_id:B12F02N03'}):
#         output.append({'id': a['id'], 'building': a['building'], 'floor': a['floor'], 'event': a['event'], 'count_IN': a['count_IN'],
#                       'count_OUT': a['count_OUT'], 'currentTime': a['currentTime'], 'image': a['image'], 'restartTime': a['restartTime']})
#     return jsonify(output)

# # ดึงข้อมูลกล้องตัวที่ 4


# @app.route('/getdatadevice4', methods=['GET'])  # ดึงข้อมูลกล้อง 4
# def getdatadevice4():
#     output = []
#     for a in mycol3.find({'id': 'Camrea_id:B12F03N07'}):
#         output.append({'id': a['id'], 'building': a['building'], 'floor': a['floor'], 'event': a['event'], 'count_IN': a['count_IN'],
#                       'count_OUT': a['count_OUT'], 'currentTime': a['currentTime'], 'image': a['image'], 'restartTime': a['restartTime']})
#     return jsonify(output)

# # ดึงข้อมูลกล้องตัวที่ 5


# @app.route('/getdatadevice5', methods=['GET'])  # ดึงข้อมูลกล้อง 5
# def getdatadevice5():
#     output = []
#     for a in mycol3.find({'id': 'Camrea_id:B12F03N08'}):
#         output.append({'id': a['id'], 'building': a['building'], 'floor': a['floor'], 'event': a['event'], 'count_IN': a['count_IN'],
#                       'count_OUT': a['count_OUT'], 'currentTime': a['currentTime'], 'image': a['image'], 'restartTime': a['restartTime']})
#     return jsonify(output)

# # ดึงข้อมูลกล้องตัวที่ 6


# @app.route('/getdatadevice6', methods=['GET'])  # ดึงข้อมูลกล้อง 6
# def getdatadevice6():
#     output = []
#     for a in mycol3.find({'id': 'Camrea_id:B12F03N09'}):
#         output.append({'id': a['id'], 'building': a['building'], 'floor': a['floor'], 'event': a['event'], 'count_IN': a['count_IN'],
#                       'count_OUT': a['count_OUT'], 'currentTime': a['currentTime'], 'image': a['image'], 'restartTime': a['restartTime']})
#     return jsonify(output)

# # ดึงข้อมูลกล้องตัวที่ 7


# @app.route('/getdatadevice7', methods=['GET'])  # ดึงข้อมูลกล้อง 7
# def getdatadevice7():
#     output = []
#     for a in mycol4.find({'id': 'Camrea_id:B12F04N13'}):
#         output.append({'id': a['id'], 'building': a['building'], 'floor': a['floor'], 'event': a['event'], 'count_IN': a['count_IN'],
#                       'count_OUT': a['count_OUT'], 'currentTime': a['currentTime'], 'image': a['image'], 'restartTime': a['restartTime']})
#     return jsonify(output)

# # ดึงข้อมูลกล้องตัวที่ 8


# @app.route('/getdatadevice8', methods=['GET'])  # ดึงข้อมูลกล้อง 8
# def getdatadevice8():
#     output = []
#     for a in mycol4.find({'id': 'Camrea_id:B12F04N15'}):
#         output.append({'id': a['id'], 'building': a['building'], 'floor': a['floor'], 'event': a['event'], 'count_IN': a['count_IN'],
#                       'count_OUT': a['count_OUT'], 'currentTime': a['currentTime'], 'image': a['image'], 'restartTime': a['restartTime']})
#     return jsonify(output)


# #ฟั่งชั่นบันทึกไฟล์ยังไม่สมบูรณ์
# cursor = ใส่คอลเล็คชั่นที่ต้องการ[yom7dข้อมูลเช่น-mycol.find()
# mongo_docs = list(cursor)
# mongo_docs = mongo_docs[:1] # slice the list
# print ("total docs:", len(mongo_docs))
# docs = pandas.DataFrame(columns=[])
# for num, doc in enumerate(mongo_docs):
#     doc["_id"] = str(doc["_id"])
#     doc_id = doc["_id"]
# series_obj = pandas.Series( doc, name=doc_id )
# docs = docs.append(series_obj)
# json_export = docs.to_json() # return JSON data
# print ("\nJSON data:", json_export)
# docs.to_json("dataupdate.json")



# @app.route('/insert2',methods=['POST'])
# def insert2():
#     if request.method=='POST':
#         floor=request.form['floor']
#         number=request.form['number']
#         apirealtime=request.form['apirealtime']
#         apihistory=request.form['apihistory']
#         apidevice=request.form['apidevice']
#         apiinfo=request.form['apiinfo']
#         user=request.form['user']
#         password=request.form['password']

#         mycol.insert({'Floor' : request.form.get('floor'),'ID Number' : request.form.get('number'),'Api Realtime' : request.form.get('apirealtime'),'Api History' : request.form.get('apihistory')
#         ,'Api Device' : request.form.get('apidevice'),'Api Info' : request.form.get('apiinfo'),'User' : request.form.get('user'),'Password' : request.form.get('password')})

#     cursor = mycol.find()
#     mongo_docs = list(cursor)
#     mongo_docs = mongo_docs[:1] # slice the list
#     print ("total docs:", len(mongo_docs))
#     docs = pandas.DataFrame(columns=[])
#     for num, doc in enumerate(mongo_docs):
#         doc["_id"] = str(doc["_id"])
#         doc_id = doc["_id"]
#     series_obj = pandas.Series( doc, name=doc_id )
#     docs = docs.append(series_obj)
#     json_export = docs.to_json() # return JSON data
#     print ("\nJSON data:", json_export)
#     docs.to_json("dataupdate.json")


#     return redirect(url_for("devicenew"))

# @app.route('/update2', methods=['POST'])
# def update2():
#     if request.method == 'POST':
#         emptycarnumber2 = request.form['emptycarnumber2']

#         myupdate.insert(
#             {'จำนวนรถในลานจอดรถชั้น2': request.form.get('emptycarnumber2')})
#     return redirect(url_for("update"))


# @app.route('/update3', methods=['POST'])
# def update3():
#     if request.method == 'POST':
#         emptycarnumber3 = request.form['emptycarnumber3']

#         myupdate.insert(
#             {'จำนวนรถในลานจอดรถชั้น3': request.form.get('emptycarnumber3')})
#     return redirect(url_for("update"))


# @app.route('/update4', methods=['POST'])
# def update4():
#     if request.method == 'POST':
#         emptycarnumber4 = request.form['emptycarnumber4']

#         myupdate.insert(
#             {'จำนวนรถในลานจอดรถชั้น4': request.form.get('emptycarnumber4')})
#     return redirect(url_for("update"))

#     # myupdate คือ คอลเล็คชั่นเก็บข้อมูลอัพเดท


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# =========================================================================
# ==================================================
# ฟังชั่นบันทึกข้อมูลชุดที่1ลงใน MongoDB
@app.route('/insert1', methods=['POST'])
@login_required
def insert1():
    if request.method == 'POST':
        number = request.form['number']
        type = request.form['type']
        building = request.form['building']
        floor = request.form['floor']
        event = request.form['event']
        sensor = request.form['sensor']
        pixel = request.form['pixel']
        framerate = request.form['framerate']
        light = request.form['light']
        daynight = request.form['daynight']
        lens = request.form['lens']
        ir = request.form['ir']

        # ใส่คอลเล็คชั่นที่ต้องการเก็บข้อมูลเช่น-mycol.insert({'หมายเลขกล้อง': request.form.get('number'), 'รุ่น': request.form.get('type'), 'ตึกที่ติดตั้ง': request.form.get('building'), 'ชั้นที่ติดตั้ง': request.form.get('floor'), 'หน้าที่': request.form.get('event'), 'เซนเซอร์รับภาพ': request.form.get(
        #     'sensor'), 'จำนวนพิกเซล': request.form.get('pixel'), 'Frame Rate': request.form.get('framerate'), 'แสงต่ำสุดที่รับภาพได้': request.form.get('light'), 'ระบบ Day/Night': request.form.get('daynight'), 'เลนส์': request.form.get('lens'), 'ระยะIRไกลสุด': request.form.get('ir')})
    return redirect(url_for("adddevice2"))


# ฟังชั่นบันทึกข้อมูลชุดที่2ลงใน MongoDB
@app.route('/insert2', methods=['POST'])
@login_required
def insert2():
    if request.method == 'POST':
        floor = request.form['floor']
        number = request.form['number']
        apirealtime = request.form['apirealtime']
        apihistory = request.form['apihistory']
        apidevice = request.form['apidevice']
        apiinfo = request.form['apiinfo']
        user = request.form['user']
        password = request.form['password']

        # ใส่คอลเล็คชั่นที่ต้องการเก็บข้อมูลเช่น-mycol.insert({'Floor': request.form.get('floor'), 'ID Number': request.form.get('number'), 'Api Realtime': request.form.get('apirealtime'), 'Api History': request.form.get(
        #     'apihistory'), 'Api Device': request.form.get('apidevice'), 'Api Info': request.form.get('apiinfo'), 'User': request.form.get('user'), 'Password': request.form.get('password')})

    return redirect(url_for("devicenew"))


@app.route('/insertcontact', methods=['POST'])
@login_required
def insertcontact():
    if request.method == 'POST':
        Name = request.form['Name']
        typeEmail = request.form['Email']
        institution = request.form['institution']
        Message = request.form['Message']

        # mycol.insert({'ชื่อ': request.form.get('Name'), 'อีเมล': request.form.get(
        #     'Email'), 'หน่วยงาน': request.form.get('institution'), 'ข้อความ': request.form.get('Message')})
    return redirect(url_for("contact"))





# ===========================================================
# OHM 15-10-64
# ===========================================================


ua = "c29yYXdpdA=="
pa = "T2htQDIwMjI="
MONGO_HOST = "203.185.67.133"
MONGO_DB = "parking_test_account"
MONGO_USER = (str(base64.b64decode(ua), 'utf-8'))
MONGO_PASS = (str(base64.b64decode(pa), 'utf-8'))
server = SSHTunnelForwarder(
    (MONGO_HOST, 22),
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=('127.0.0.1', 27017)
)
server.start()

client = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
db = client[MONGO_DB]
users = db['test']
roles = db['test_roles']


class User:
    def __init__(self, id, username, role):
        self._id = id
        self.username = username
        self.role = role

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    @staticmethod
    def is_admin():
        return self.role == 'admin'

    def get_id(self):
        return self.username


app.config["DEBUG"] = True
app.config['SECRET_KEY'] = "my-secret-key-for-development"
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(username):
    u = users.find_one({"email": username})
    if not u:
        return None
    return User(username=u['email'], role=u['role'], id=u['_id'])


def user_rold():
    if current_user.is_authenticated:
        return (current_user.role)
    else:
        return ('general')

def user_email():
    if current_user.is_authenticated:
        return (current_user.username)
    else:
        return ('')

def check_user_rold():
    if current_user.is_authenticated:
        return ('%s,%s' % (current_user.role, current_user.username))
    else:
        return ('general,')






@app.route('/nstda/parking/admin/users', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def admin_show_all_users():
    return render_template('admin-users.html', all_roles=roles.find(), all_users=users.find(), roles_required=(str(check_user_rold())).split(","))



@app.route('/nstda/parking/admin/delete-user/<user_id>', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def admin_delete_user(user_id):
    delete_user = users.find_one({'_id': ObjectId(user_id)})
    if delete_user:
        users.delete_one(delete_user)
        return redirect(url_for('admin_show_all_users'))
    return redirect(url_for('admin_show_all_users'))


@app.route('/nstda/parking/admin/edit-user/<user_id>', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def admin_edit_user(user_id):
    edit_user = users.find_one({'_id': ObjectId(user_id)})
    if edit_user:
        return render_template('admin-users-edit.html', user=edit_user, all_roles=roles.find(), roles_required=(str(check_user_rold())).split(","))
    return redirect(url_for('admin_show_all_users'))


    
@app.route('/nstda/parking/admin/update-user/<user_id>', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def admin_update_user(user_id):
    if request.method == 'POST':
        form = request.form
        password = request.form['password']

        users.replace_one({'_id': ObjectId(user_id)},
                          {
            'name': form['name'],
            'email': form['email'],
            # 'password': generate_password_hash(password, method='sha256'),
            'password': password,
            'role': form['role'],
            'date_added': form['date_added'],
            'date_modified': datetime.datetime.now()
        }, upsert=True)
        return redirect(url_for('admin_show_all_users'))
    return render_template('admin-users.html', all_roles=roles.find(), all_users=users.find(), roles_required=(str(check_user_rold())).split(","))



@app.route('/nstda/parking/login')
def login():
    return render_template('login.html')

# process method post login
@app.route('/nstda/parking/login', methods=['POST'])
def login_post():
    # next_url = request.args.get('next')
    # print(next_url)
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    # print(email)
    # print(password)
    # print(remember)

    user = users.find_one({"email": email})
    if (not user or not check_password_hash(user['password'], password) or (not user)):
        return render_template('login.html')
    user_obj = User(username=user['email'], role=user['role'], id=user['_id'])
    login_user(user_obj, remember=remember)
    # return render_template('home.html')
    return redirect(url_for('home', roles_required=check_user_rold()))
    # return render_template('home.html',roles_required=check_user_rold())

@app.route('/nstda/parking/signup')
def signup():
    return render_template('register.html')

@app.route('/nstda/parking/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = users.find_one({"email": email})

    if user:
        # flash('Email address already exists')
        return redirect(url_for('signup'))

    role = 'basic'

    new_user = {
        'name': name,
        'email': email,
        'password': generate_password_hash(password, method='sha256'),
        'role': role,
        'date_added': datetime.datetime.now(),
        'date_modified': datetime.datetime.now()
    }

    users.insert_one(new_user)
    return redirect(url_for('login'))
    

@app.route('/nstda/parking/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
    # return render_template('home.html')
    # return redirect(url_for('home.index'))





if __name__ == "__main__":
    app.run(debug=True)
