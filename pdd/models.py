# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = '__efmigrationshistory'


class PromotersUserinfos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=128)  # Field name made lowercase.
    cookies = models.TextField(db_column='Cookies')  # Field name made lowercase.
    adddata = models.TextField(db_column='AddData')  # Field name made lowercase.
    pid = models.CharField(db_column='Pid', unique=True, max_length=128)  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'promoters_userinfos'
        verbose_name = "PID管理"
        verbose_name_plural = "PID管理"


class UserPidbindinginfos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    uid = models.CharField(db_column='Uid', max_length=64)  # Field name made lowercase.
    pid = models.CharField(db_column='Pid', max_length=128)  # Field name made lowercase.
    bindingtime = models.DateTimeField(db_column='BindingTime')  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user_pidbindinginfos'
        verbose_name = "Token绑定PID管理"
        verbose_name_plural = "Token绑定PID管理"


class UserWorkinginfos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    types = models.CharField(db_column='Types', max_length=32)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=128)  # Field name made lowercase.
    locktime = models.DateTimeField(db_column='LockTime')  # Field name made lowercase.
    expiretime = models.DateTimeField(db_column='ExpireTime')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user_workinginfos'
        verbose_name = "工作锁管理"
        verbose_name_plural = "工作锁管理"


class Userinfos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    types = models.CharField(db_column='Types', max_length=32)  # Field name made lowercase.
    token = models.CharField(db_column='Token', unique=True, max_length=128)  # Field name made lowercase.
    uid = models.CharField(db_column='Uid', max_length=64)  # Field name made lowercase.
    uin = models.CharField(db_column='Uin', max_length=128)  # Field name made lowercase.
    adddata = models.TextField(db_column='AddData')  # Field name made lowercase.
    uploadtime = models.DateTimeField(db_column='UploadTime')  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime')  # Field name made lowercase.
    order = models.IntegerField(db_column='Order')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'userinfos'
        verbose_name = "Token管理"
        verbose_name_plural = "Token管理"


class VideoReleaseinfos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    uid = models.CharField(db_column='Uid', max_length=64)  # Field name made lowercase.
    feedid = models.CharField(db_column='FeedId', max_length=64)  # Field name made lowercase.
    urlmd5 = models.CharField(db_column='UrlMd5', max_length=32)  # Field name made lowercase.
    uploadstate = models.IntegerField(db_column='UploadState')  # Field name made lowercase.
    uploadtime = models.DateTimeField(db_column='UploadTime')  # Field name made lowercase.
    shareid = models.CharField(db_column='ShareId', max_length=64)  # Field name made lowercase.
    pid = models.CharField(db_column='Pid', max_length=128)  # Field name made lowercase.
    releasestate = models.IntegerField(db_column='ReleaseState')  # Field name made lowercase.
    releasetime = models.DateTimeField(db_column='ReleaseTime')  # Field name made lowercase.
    adddata = models.TextField(db_column='AddData')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'video_releaseinfos'
        verbose_name = "视频发布管理"
        verbose_name_plural = "视频发布管理"


class VideoResources(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    types = models.CharField(db_column='Types', max_length=32)  # Field name made lowercase.
    client = models.CharField(db_column='Client', max_length=32)  # Field name made lowercase.
    primaryuid = models.CharField(db_column='PrimaryUid', max_length=64)  # Field name made lowercase.
    feedid = models.CharField(db_column='FeedId', unique=True, max_length=64)  # Field name made lowercase.
    goodsid = models.CharField(db_column='GoodsId', max_length=64)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    adddata = models.TextField(db_column='AddData')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'video_resources'
        verbose_name = "视频资源管理"
        verbose_name_plural = "视频资源管理"
