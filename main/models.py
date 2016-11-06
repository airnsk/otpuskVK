from django.db import models

# Create your models here.
class zapros(models.Model):


    muser_id = models.CharField(verbose_name='userid', max_length=255, unique=False)
    datezapros=models.DateField(verbose_name='date',auto_now=True)
    zarp_jan=models.IntegerField(verbose_name='jan',blank=True,null=True)
    zarp_feb=models.IntegerField(verbose_name='feb',blank=True,null=True)
    zarp_mar=models.IntegerField(verbose_name='mar',blank=True,null=True)
    zarp_apr=models.IntegerField(verbose_name='apr',blank=True,null=True)
    zarp_may=models.IntegerField(verbose_name='may',blank=True,null=True)
    zarp_jun=models.IntegerField(verbose_name='jun',blank=True,null=True)
    zarp_jul=models.IntegerField(verbose_name='jul',blank=True,null=True)
    zarp_aug=models.IntegerField(verbose_name='aug',blank=True,null=True)
    zarp_sep=models.IntegerField(verbose_name='sep',blank=True,null=True)
    zarp_oct=models.IntegerField(verbose_name='oct',blank=True,null=True)
    zarp_nov=models.IntegerField(verbose_name='nov',blank=True,null=True)
    zarp_dec=models.IntegerField(verbose_name='dec',blank=True,null=True)
    mdStart=models.IntegerField(verbose_name="startDate",blank=True,null=True)
    mdEnd=models.IntegerField(verbose_name="endDate",blank=True,null=True)
    startYear=models.IntegerField(verbose_name="startYear",blank=True,null=True)
    endYear=models.IntegerField(verbose_name="endYear",blank=True,null=True)

    def __unicode__(self):
        return self.muser_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True