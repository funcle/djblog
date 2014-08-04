#/usr/bin/python
#-*- coding:utf-8 -*-

import re
import json
import datetime

from django.utils import timezone, simplejson
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from models import Essay, Type, Comment
from essay.templatetags.context_processor import globals_var
# Create your views here.

class QuerySetEncoder(simplejson.JSONEncoder):
    """
    Encoding QuerySet into JSON format.
    """
    def default(self, object):
        try:
            return serializers.serialize("python", object,
                                          ensure_ascii = False )
        except:
            return simplejson.JSONEncoder.default(self, object )


def index(request):

    essays = Essay.objects.filter(
        display=True
        ).order_by('-ctime').all()[:3]

    rs = globals_var(request)
    rs.update(essays=essays)

    return render_to_response('essay/index.html', rs)


def types(request, tname=None):
    
    tobj = Type.objects.filter(
        interfacename=tname
        )[0]
    if not tobj:
        return u'<h1>404</h1>'
    essays = Essay.objects.filter(
        type_id=tobj.id,
        display=True
        ).order_by('-ctime').all()

    rs = globals_var(request)
    rs.update(essays=essays)

    return render_to_response('essay/types.html', rs)
 

def display(request, ym):

    ym_reg = re.compile(r'^\d{4}-\d{2}$')
    if not ym_reg.match(ym):
        return u'404'

    year, month = ym.split('-')
    current_year = datetime.date.today().year
    if not 1970<=int(year)<=current_year or not 0<int(month)<13:
        return u"404"

    start = datetime.date(int(year), int(month), 1)
    end = datetime.date(int(year), int(month)+1, 1) - datetime.timedelta(days=1)

    essays = Essay.objects.filter(
        ctime__gte=start,
        ).exclude(
        ctime__gte=end,
        ).filter(
        display=True
        ).order_by('-ctime').all()

    rs = globals_var(request)
    rs.update(essays=essays)

    return render_to_response('essay/types.html', rs)


def essay_detail(request, id):

    essay = Essay.objects.filter(
        id=id,
        display=True
        )[0]
    if not essay:
        return u'<h1>404</h1>'

    rs = globals_var(request)
    rs.update(essay=essay)

    return render_to_response('essay/essay.html', rs)


def comments(request, id):
    
    essay = Essay.objects.get(pk=id)
    comments = Comment.objects.filter(
        essay_id=essay.id
        ).order_by('-ctime').all()

    render_data = dict(essay=essay, comments=comments)

    rs = globals_var(request)
    rs.update(render_data)

    return render_to_response('essay/comments.html', rs)


@csrf_exempt
def comments_add(request):

    essay_id = request.POST.get("essay_id", '')
    username = request.POST.get("username", '')
    comments = request.POST.get("comments", '')
    req_ip = request.META['REMOTE_ADDR']

    if essay_id in (""," ", ):
        result = dict(status=False, msg=u'404')
    else:
        comment = Comment(essay_id=essay_id, username=username, comment=comments,
            req_ip=req_ip, low_num=0, up_num=0, ctime=timezone.now())
        comment.save()
        result = dict(status=True, msg=u'200')
    
    result = simplejson.dumps(result, cls=QuerySetEncoder)
    return HttpResponse(result)
    
def contact(request):

    return render_to_response('essay/contact.html')
