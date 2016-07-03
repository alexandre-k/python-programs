# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Ip(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    hostname = models.TextField(blank=True, null=True)  # This field type is a guess.
    ip = models.TextField(blank=True, null=True)  # This field type is a guess.
    area = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ip'

    def __str__(self):
        return self.ip


class Switch(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    hostname = models.TextField(blank=True, null=True)  # This field type is a guess.
    ip = models.TextField(blank=True, null=True)  # This field type is a guess.
    model = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'switch'

    def __str__(self):
        return self.hostname


class Switchport(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    port = models.TextField(blank=True, null=True)  # This field type is a guess.
    ip = models.TextField(blank=True, null=True)  # This field type is a guess.
    duplex = models.TextField(blank=True, null=True)  # This field type is a guess.
    speed = models.IntegerField(blank=True, null=True)
    switch_hostname = models.ForeignKey(Switch, models.DO_NOTHING, db_column='switch_hostname')

    class Meta:
        managed = False
        db_table = 'switchport'

    def __str__(self):
        return self.port, "in ", self.switch_hostname
