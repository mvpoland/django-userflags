from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404

from userflags.models import Flag


def _redirect_when_possible(request):
    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponse('OK')


def link(request, user_id, flag_id):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)
    flag = get_object_or_404(Flag, pk=flag_id)
    flag.add_user(user)
    return _redirect_when_possible(request)


def unlink(request, user_id, flag_id):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)
    flag = get_object_or_404(Flag, pk=flag_id)
    flag.remove_user(user)
    return _redirect_when_possible(request)
