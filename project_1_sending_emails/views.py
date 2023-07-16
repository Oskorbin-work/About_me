from django.shortcuts import render


from base.models import Base, ContentBody


def index(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Main Page")[0]
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path[4:-1],
        'base_data': f'base/js/data/{request.path[1:3]}.js',
    }
    return render(request, 'projects/sharing_emails/index.html', context=context)