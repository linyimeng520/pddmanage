from django.contrib import admin

# Register your models here.
from .models import *


class PromotersUserinfosAdmin(admin.ModelAdmin):
    list_display = ("user", "cookies", "pid", "state", "adddata")


class UserPidbindinginfosAdmin(admin.ModelAdmin):
    list_display = ("pid", "uid", "bindingtime", "state", "lasttime", "id")


class UserinfosAdmin(admin.ModelAdmin):
    search_fields = ['token']
    list_display = ("token", "types", "adddata", "uploadtime", "lasttime", "order", "id")


class VideoReleaseinfosAdmin(admin.ModelAdmin):
    list_display = ("id", "uid", "feedid", "adddata", "urlmd5", "uploadstate", "uploadtime", "shareid",
                    "pid", "releasestate", "releasetime")


class VideoResourcesAdmin(admin.ModelAdmin):
    list_display = ("goodsid", "types", "client", "state", "feedid", "adddata", "addtime", "time", "primaryuid")


admin.site.register(PromotersUserinfos, PromotersUserinfosAdmin)
admin.site.register(UserPidbindinginfos, UserPidbindinginfosAdmin)
admin.site.register(UserWorkinginfos)
admin.site.register(Userinfos, UserinfosAdmin)
admin.site.register(VideoReleaseinfos, )
admin.site.register(VideoResources, VideoResourcesAdmin)

