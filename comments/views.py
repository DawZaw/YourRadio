from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Comment

# Create your views here.
def add_comment(request, **kwargs):
    if request.method == 'POST':
        user = request.user
        post = request.POST.get('comment-text')
        date = timezone.now()
        current_url = request.META.get("HTTP_REFERER")
        try:
            page = "-".join(current_url.split('artists/')[1].split('/')[:-1])
        except IndexError:
            page = "-".join(current_url.split('users/')[1].split('/')[:-1])
        Comment.objects.create(user=user, post=post, date=date, page=page)
        messages.info(request, "Comment has been added.")
    return HttpResponseRedirect(current_url)