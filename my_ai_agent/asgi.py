"""
ASGI config for my_ai_agent project.
ASGI是异步的

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/

接受网络请求，默认的

"""

import os

from django.core.asgi import get_asgi_application



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_ai_agent.settings")

application = get_asgi_application()
