from django.contrib.auth.models import User
from datetime import date
from django.db import models
import uuid
from tinymce.models import HTMLField
from PIL import Image
from django.utils.translation import gettext_lazy as _



class CarModel(models.Model):
    make = models.CharField(_('Make'), max_length=100, help_text=_('Enter the car make'))
    model = models.CharField(_('Model'), max_length=100, help_text=_('Enter the car model'))

    class Meta:
        verbose_name = _('Car Model')
        verbose_name_plural = _('Car Models')

    def __str__(self):
        return f'{self.make} {self.model}'


class Car(models.Model):
    license_plate = models.CharField(_('License Plate'), max_length=20, help_text=_('Enter the car license plate'))
    vin = models.CharField(_('VIN Code'), max_length=50, help_text=_('Enter the car VIN code'))
    customer = models.CharField(_('Customer'), max_length=100, help_text=_('Enter the customer name or company'))
    description = HTMLField(_('Description'), blank=True, null=True, help_text=_('Enter the car model description'))
    car_model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True, help_text=_('Select the car model'))
    cover = models.ImageField(_('Photo'), upload_to='covers', null=True)

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

    def __str__(self):
        return f'{self.license_plate} ({self.car_model})'



class Service(models.Model):
    name = models.CharField(_('Service'), max_length=100, help_text=_('Enter the service name (e.g., Oil Change)'))
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, help_text=_('Enter the service price (e.g., 50.00)'))

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return f'{self.name} ({self.price} EUR)'


class Order(models.Model):

    @property
    def is_overdue(self):
        if self.return_date and date.today() > self.return_date:
            return True
        return False

    STATUS_CHOICES = [
        ('NEW', _('New')),
        ('IN_PROGRESS', _('In Progress')),
        ('COMPLETED', _('Completed')),
        ('CANCELLED', _('Cancelled')),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text=_('Unique order ID'))
    customer = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    date = models.DateTimeField(_('Date'), help_text=_('Enter the order date'), null=True, blank=True)
    description = HTMLField(_('Description'), blank=True, null=True, help_text=_('Enter the car model description'))
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, help_text=_('Select the car for the order'))
    status = models.CharField(
        _('Status'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='NEW',
        help_text=_('Select the order status')
    )

    class Meta:
        ordering = ['-date']
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'Order {self.id}'


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, help_text=_('Select the order to which the line belongs'))
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, help_text=_('Select the performed service'))
    quantity = models.PositiveIntegerField(_('Quantity'), help_text=_('Enter the quantity of performed services'))

    class Meta:
        verbose_name = _('Order Line')
        verbose_name_plural = _('Order Lines')

    def __str__(self):
        return f'{self.order} - {self.service} ({self.quantity} pcs)'


class OrderReview(models.Model):
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(_('Review'), max_length=2000)

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        ordering = ['-date_created']


class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return f"{self.user.username} profile"
