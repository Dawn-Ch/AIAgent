"""
WSGI config for my_ai_agent project.
WSGI是同步的

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/

接受网络请求，默认的

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_ai_agent.settings")

application = get_wsgi_application()
