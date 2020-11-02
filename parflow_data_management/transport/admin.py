from django.contrib import admin
from .models import authorized_key, key_pair

admin.site.register(authorized_key.AuthorizedKey)
admin.site.register(key_pair.KeyPair)
