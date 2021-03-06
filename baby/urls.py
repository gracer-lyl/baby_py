# coding: UTF-8

from baby import app
from flask.ext import restful
from restfuls.doctor_restful import BabyList, BabyCollect, DoctorInfo, Search,\
    Search_View, DeleteSearchHistoryAll, MeetingNotice
from restfuls.baby_restful import BabyInfo, ParentingGuide
from restfuls.login_register import DoLogin, RegisterData, AlterPassword, DoRegisterDoctor
from baby.controls.user_feature_control import to_login, to_update_password, to_register
from baby.controls.baby_control import to_grow_line, to_raise
from baby.controls.doctor_control import to_meeting

# # 后台Admin
# admin = Admin(name=u'小宇')
# # 初始化app
# admin.init_app(app)
#
# # 上传图片路径
# file_path = os.path.join(os.path.dirname(__file__), 'static')
# admin.add_view(Yu_File(file_path, '/static/', name='文件'))
# yu_picture_path = os.path.join(os.path.dirname(__file__), 'static/system/baby_picture')
# admin.add_view(Yu_Picture_File(yu_picture_path, 'baby/static/system/baby_picture/', name='YuImage', category=u'Yu'))

# html页面访问路劲
app.add_url_rule('/html/login.html/', 'to_login', to_login, methods={ 'GET', 'POST'})
app.add_url_rule('/html/password.html/', 'to_update_password', to_update_password, methods={'GET', 'POST'})
app.add_url_rule('/html/register.html', 'to_register', to_register, methods={'GET', 'POST'})
app.add_url_rule('/html/grow_line.html', 'to_grow_line', to_grow_line, methods={ 'GET', 'POST'})
app.add_url_rule('/html/raise.html', 'to_raise', to_raise, methods={'GET', 'POST'})
app.add_url_rule('/html/meeting.html', 'to_meeting', to_meeting, methods={'GET', 'POST'})

# 接口访问路径
api = restful.Api(app)

api.add_resource(BabyList, '/restful/baby/list')
api.add_resource(BabyCollect, '/restful/baby/collect/list')
api.add_resource(DoctorInfo, '/restful/doctor/info')
api.add_resource(Search, '/restful/doctor/search')
api.add_resource(Search_View, '/restful/doctor/search/history')
api.add_resource(DeleteSearchHistoryAll, '/restful/doctor/delete/search_history')
api.add_resource(MeetingNotice, '/restful/doctor/meeting/notice')
api.add_resource(BabyInfo, '/restful/baby/info')
api.add_resource(ParentingGuide, '/restful/baby/parenting/guide')
api.add_resource(DoLogin, '/restful/html/do/login')
api.add_resource(RegisterData, '/restful/html/register/data')
api.add_resource(AlterPassword, '/restful/html/alter/password')
api.add_resource(DoRegisterDoctor, '/restful/html/do/register')