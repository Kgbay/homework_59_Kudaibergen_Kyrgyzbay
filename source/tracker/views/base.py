from django.views.generic import ListView, RedirectView

from tracker.models import Task


class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('-created_at')
    paginate_by = 3
    paginate_orphans = 1

class IndexRedirectView(RedirectView):
    pattern_name = 'index'