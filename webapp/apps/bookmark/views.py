from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import BookmarkForm

def home(request, template_name='bookmark/home.html'):
    form = BookmarkForm()

    return render_to_response(template_name, RequestContext(request, {
        'form': form,
        'order_by': request.session.get('order_by', 'newest'),
        }))