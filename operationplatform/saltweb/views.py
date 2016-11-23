#coding:utf-8
import salt.client
import time
from common import CJsonEncoder
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import RequestContext
from models import userinfo
from models import saltcommandhistory
from models import article
from models import comment
from models import chatmodel
import json
# Create your views here.
#定义检测登陆的装饰器
def checklogin(func):
    def warper(request,*args,**kwargs):
        if request.session.get('is_login',None):
            return func(request,*args,**kwargs)
        else:
            return render_to_response('login.html',{'logingo':"请重新登录"},context_instance=RequestContext(request))
    return warper
################################################################################################################################################
def logout(request):
    if request.session.get('is_login',None):
        del request.session['is_login']
        return render_to_response('login.html',context_instance=RequestContext(request))
    else:
        return render_to_response('login.html',context_instance=RequestContext(request))
def login(request):
    username=request.POST.get('username',None)
    password=request.POST.get('password',None)
    if all([username,password]):
        num=userinfo.objects.filter(username=username,password=password).count()
        if num>=1:
            request.session['is_login']={'username':username}
            return redirect('/index/',context_instance=RequestContext(request))
        else:
            return render_to_response('login.html',{'loginfo':"用户名或密码错误"},context_instance=RequestContext(request))
    else:
        return render_to_response('login.html',context_instance=RequestContext(request))
@checklogin
def index(request):
    loginstatus=request.session.get('is_login',None)
    return render_to_response('index.html',{'username':loginstatus['username']},context_instance=RequestContext(request))
def register(request):
    return render_to_response('register.html',context_instance=RequestContext(request))
def createuser(request):
    username=request.POST.get('username',None)
    password=request.POST.get('password',None)
    if all([username,password]):
        try:
            userinfo.objects.create(username=username,password=password)
        except Exception,e:
            pass
        else:
            return render_to_response('register.html',{'registerinfo':"注册成功"})
def checkuser(request):
    username=request.POST.get('username',None)
    user_num=userinfo.objects.filter(username=username).count()
    print user_num
    if user_num>0:
        responseresult={'status':1,'message':"用户名已存在"}
        return HttpResponse(json.dumps(responseresult))
    else:
        responseresult={'status':0,'message':"恭喜您！用户名可用"}
        return HttpResponse(json.dumps(responseresult))
def getusername(request):
    loginstatus=request.session.get('is_login',None)
    username=loginstatus['username']
    return HttpResponse(username)
@checklogin
def saltcontrol(request):
    loginstatus=request.session.get('is_login',None)
    username=loginstatus['username']
    tgt_type=request.POST.get('miniontype','glob')
    minion=request.POST.get('minion',None)
    saltmodule=request.POST.get('module',None)
    module_arg=request.POST.get('arg',None)
    try:
        saltcommandhistory.objects.create(username=username,minions=minion,miniontype=tgt_type,module=saltmodule,arg=module_arg)
    except Exception,e:
        print e.message
    else:
        print "ok"
    local = salt.client.LocalClient()
    if module_arg:
        result=local.cmd(minion,saltmodule,arg=(module_arg,),expr_form=tgt_type)
    else:
        result=local.cmd(minion,saltmodule,expr_form=tgt_type)
#    return render_to_response("index.html",{"dicts":result,'username':loginstatus['username']},context_instance=RequestContext(request))
    return HttpResponse(json.dumps(result))

@checklogin
def showcmdhistory(request):
    cmdhistoryresult=saltcommandhistory.objects.all()
    return render(request,'commandhistory.html',{'cmddicts':cmdhistoryresult})
@checklogin
def saltbbs(request):
    articlelist=article.objects.all()
    return render(request,'saltbbs.html',{'articlelist':articlelist})
@checklogin
def addviews(request):
    id=request.POST.get('id',None)
    print id
    if id:
        obj=article.objects.get(id=id)
        temp=obj.views+1
        obj.views=temp
        obj.save()
        viewsnum=article.objects.get(id=id).views
        print article.objects.filter(id=id).values('views')[0]['views']
        print viewsnum
        return HttpResponse(viewsnum)
@checklogin
def addcomment(request):
    loginstatus=request.session.get('is_login',None)
    username=loginstatus['username']
    id=request.POST.get('id',None)
    content=request.POST.get('content',None)
    articleobj=article.objects.get(id=id)
    userobj=userinfo.objects.get(username=username)
    print content
    print 1
    try:
        comment.objects.create(username=userobj,articlename=articleobj,content=content)
    except Exception,e:
        print e
        return HttpResponse("error")
    else:
        commenttime=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
        ret={'username':username,'content':content,'datetime':commenttime}
        return HttpResponse(json.dumps(ret))
@checklogin
def showcomments(request):
    id=request.POST.get('id',None)
    print id
    articleobj=article.objects.filter(id=id)
    commentlist=comment.objects.filter(articlename=articleobj).values('username__username','createtime','content').order_by("createtime")
    temp=list(commentlist)
    return HttpResponse(json.dumps(temp,cls=CJsonEncoder))
@checklogin
def chathome(request):
    loginstatus=request.session.get('is_login',None)
    username=loginstatus['username']
    userobj=userinfo.objects.get(username=username)
    chatmessage=request.POST.get('message',None)
    try:
        chatmodel.objects.create(username=userobj,chatcontent=chatmessage)
        chatid=chatmodel.objects.all().order_by("-createtime")[0].id
        print chatid
    except Exception,e:
        print e
        return HttpResponse("error")
    else:
        chattime=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
        ret={"id":chatid,'chattime':chattime,"username":username}
        return HttpResponse(json.dumps(ret))
@checklogin
def checkchat(request):
    chatid=request.POST.get('id',None)
    chatlist=list(chatmodel.objects.filter(id__gt=chatid).values('username__username','createtime','chatcontent'))
    chatnewid=chatmodel.objects.all().order_by("-createtime")[0].id
    ret={"id":chatnewid,"chatinfo":chatlist}
    return HttpResponse(json.dumps(ret,cls=CJsonEncoder))
