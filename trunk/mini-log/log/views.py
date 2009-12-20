from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms

from log.models import Comment
import datetime


class CommentForm(forms.ModelForm):
    "Simple form for the Person model"

    class Meta:
        model = Comment


def index(request):
    data = {}
    if request.method == 'POST':
        new_comment = CommentForm(request.POST)
        if new_comment.is_valid():
            new_comment.save()
            return HttpResponseRedirect(reverse('main-log'))
    else:
        new_comment = CommentForm()
    data['method'] = request.method
    data['comments'] = Comment.objects.order_by("-date")
    data['form'] = new_comment
    return render_to_response("log/log.html", data)


def current_time(request, offset):
    if offset:
        offset = int(offset)
    else:
        offset = 0
    now = datetime.datetime.now()
    if offset > 0:
        now = now - datetime.timedelta(hours=offset)
    data = {"current_time": now, "offset": offset}
    return render_to_response("log/current_time.html", data)
