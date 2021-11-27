from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal


class Wallets(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    value = models.DecimalField(max_digits=19, decimal_places=0,)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="walletss", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('user_info_wallets_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('user_info_wallets_update', args=(self.pk,))



class Invoice(models.Model):
    DRAFT='dr'
    PAYED='pa'

    ORDER_STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PAYED,'Payed'),
    )

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    order_status=models.CharField(verbose_name=_("pay_status"),max_length=4,choices=ORDER_STATUS_CHOICES,default=DRAFT)

    # Relationship Fields
    request = models.ForeignKey(
        'transportation_company.Request',
        on_delete=models.CASCADE, related_name="invoices", 
    )
    from_wallet =  models.ForeignKey(
        'user_info.Wallets',
        on_delete=models.CASCADE, related_name="invoices_from", 
    )
    to_wallet =  models.ForeignKey(
        'user_info.Wallets',
        on_delete=models.CASCADE, related_name="invoices_to", 
    )
    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('user_info_invoice_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('user_info_invoice_update', args=(self.pk,))



# class Invoice(models.Model):
#     #list of status choices :paid _ unsuccessful paiment-> in transactions. deliverd
#     DRAFT='dr'
#     PAYED='pa'
#     PENDING='pe'
#     CONFIRMED='co'
#     DELIVERED='de'

#     ORDER_STATUS_CHOICES = (
#         (DRAFT, 'Draft'),
#         (PAYED,'Payed'),
#     )

#     DELIVER_STATUS_CHOICES = (
#         # todo azashoon bepors confirm ro fiziki daran ya na
#         (PENDING, 'Pending'),
#         (CONFIRMED, 'Confirmed'),
#         (DELIVERED, 'Delivered'),
#     )

#     order_status=models.CharField(verbose_name=_("pay_status"),max_length=4,choices=ORDER_STATUS_CHOICES,default=DRAFT)
#     deliver_status = models.CharField(verbose_name=_("deliver_status"), max_length=4, choices=DELIVER_STATUS_CHOICES, default=PENDING)
#     #TODO shange shipping_number into u_id (ask erfan)
#     shipping_number=models.CharField(max_length=24,null=True,blank=True) #POSTAL TRACKING CODE

#     # seller = models.ForeignKey(Seller,verbose_name=_("seller"), on_delete=models.SET_NULL, null=True) #from seller you can also undrestand which restaurant it is
#     customer = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_("customer"), null=True,blank=True, on_delete=models.SET_NULL)
#     # u can search usage of through in here:https://docs.djangoproject.com/en/2.2/topics/db/models/
#     # product_items = models.ManyToManyField(ProductVariation,verbose_name=_("product items"), through="OrderedItem")  #
#     total_price=models.DecimalField(verbose_name=_("total price"),default=Decimal('0.00'),max_digits=19, decimal_places=0,null=True,blank=True)  # totalCost #todo #decimal 2 or 3?)
#     #serial_number (is it secure if i use id for each invoice??? or should i make serial number myself?)
#     description=models.CharField(verbose_name=_("description"),max_length=200 , null=True, blank=True)
#     date=models.DateTimeField(verbose_name=_("date"),auto_now_add=True ,null=True) #todo how to make this automatic and JALALI
#     # address = models.TextField(verbose_name=_("address"),null=True,default="-1")
#     # address = models.ForeignKey("users.Address",on_delete=models.PROTECT,default="-1") #if a user has address in inovice I dont let the user to delete
#     #todo what about default and on_delete? talk to erfan
#     discount_code = models.ForeignKey("DiscountCode" ,on_delete=models.SET("deleted"), related_name="discount_payments", null=True,blank=True) #It's first model of discounting
#     promotional_code = models.ForeignKey("PromotionalCode", on_delete=models.SET("deleted"), related_name="promo_payments",null=True, blank=True) #it's user base
#     shipping_price =models.DecimalField(verbose_name=_("shipping price"),default=Decimal('0.00'),max_digits=19, decimal_places=0,null=True,blank=True) 
#     vtax = models.DecimalField(verbose_name=_("value added price"),default=Decimal('0.00'),max_digits=19, decimal_places=0,null=True,blank=True) 
#     class Meta:
#         ordering = ('-pk',)
#         verbose_name = _('Invoice')
#         verbose_name_plural = _('Invoices')

class Transaction(models.Model):
    SATAUS_CHOICES = (
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('pending',"Pending")
    )
    # Fields
    refId = models.CharField(_("trackingCode"), max_length=100) #todo BIG_TODO what about verbose name
    bankRefId = models.CharField(verbose_name=_("bankRefId"),blank=True,null=True,max_length=100)
    status = models.CharField(verbose_name=_("status"),max_length=10, choices=SATAUS_CHOICES)
    statusNum = models.IntegerField(verbose_name=_("status number"))
    authority = models.CharField(verbose_name=_("authority"),max_length=20)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Relationship Fields
    wallet=models.ForeignKey(Wallets,verbose_name=_("wallet"), on_delete=models.PROTECT,related_name="transactions")

    class Meta:
        ordering = ('-pk',)
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')

    def __str__(self):
        return str(self.pk)

class DiscountCode(models.Model): #FIRST MODEL OF DISCOUNTING we use it in invoice
    # is_used = models.BooleanField(default=False)
    code = models.CharField(max_length=64, db_index=True, unique=True, blank=True,
                            help_text='It will be fill, if you leave it empty. ex: cz6nX')
    percentage = models.SmallIntegerField(validators=(
        MinValueValidator(1), MaxValueValidator(100)))
    maximum_value = models.IntegerField(default=0) #TODO needed?
    expire_at = models.DateField()
    # inventory = models.IntegerField(default=1)
    # one_time = models.BooleanField(default=False) #todo ??????
    def __str__(self):
        return self.code


class OccasionalDiscount(models.Model): #Second way of discounting : it makes impact in product variation discount price
    title=models.CharField(max_length=200)
    # product_variation=models.ForeignKey(ProductVariation)
    percentage = models.SmallIntegerField(validators=(
        MinValueValidator(1), MaxValueValidator(100)))
    #TODO BIG todo : make sure just related items see this

    def __str__(self):
        return self.title  #+"_"+str(self.id)

class PromotionCodeStrategy(models.Model):
    # minimum_expendable_value = models.IntegerField(default=0)
    # maximum_expendable_value = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0) #todo ??????????
    expire_time = models.IntegerField(default=5)
    is_for_first_order = models.BooleanField(default=False)
    percentage = models.SmallIntegerField(validators=(
        MinValueValidator(1), MaxValueValidator(100)))
    maximum_value = models.IntegerField(default=0)

class PromotionalCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=64, db_index=True, unique=True, blank=True,
                            help_text='It will be fill, if you leave it empty. ex: cz6nX')
    # inventory = models.IntegerField() #todo ??????????????
    percentage = models.SmallIntegerField(validators=(
        MinValueValidator(1), MaxValueValidator(100)))
    # minimum_expendable_value = models.IntegerField(default=0)
    maximum_value = models.IntegerField(default=0)
    num_of_used = models.IntegerField(default=0, editable=False) # ye adad bezar va har dafe tyeki azash kam kon

    expire_at = models.DateField()
    disable =  models.BooleanField(default=False)
