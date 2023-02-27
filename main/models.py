from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField



class Profile(models.Model):
    SUPPORT = 'SUP'
    KOTON = 'KTN'
    LCWAIKIKI = 'LCW'
    DEFACTO = 'DFC'
    COLINS = 'CLS'

    COMPANIES = [
        (SUPPORT, 'Support'),
        (KOTON, 'Koton'),
        (LCWAIKIKI, 'LcWaikiki'),
        (DEFACTO, 'DeFacto'),
        (COLINS, "Colin's"),
    ]
    COMPANY_CHOICES = [(c[0], c[1]) for c in COMPANIES]


    RUSSIA = "RU"
    KAZAKHSTAN = "KZ"
    MACEDONIA = "MK"
    GEORGIA = "GE"
    ROMANIA = "RO"
    UZBEKISTAN = "UZ"
    

    COUNTRIES = [
        (RUSSIA, 'Russia'),
        (KAZAKHSTAN, 'Kazakhstan'),
        (MACEDONIA, 'Macedonia'),
        (ROMANIA, 'Romania'),
        (UZBEKISTAN, 'Uzbekistan'),
    ]

    COUNTRY_CHOICES = [(c[0], c[1]) for c in COUNTRIES]


    company = models.CharField(max_length=3, choices=COMPANY_CHOICES, blank=True)
    country = models.CharField(max_length=3,choices=COUNTRY_CHOICES, blank=True)    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50)
    
    
    def __str__(self) -> str:
        return str(self.user)


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    ticket_image = models.ImageField((""), upload_to='images/tickets', null=True, blank=True)
    content = QuillField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=3, choices=Profile.COMPANY_CHOICES, blank=True)
    country = models.CharField(max_length=3, choices=Profile.COUNTRY_CHOICES, blank=True) 
    status = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False)
    solved_by = models.ForeignKey(User, null=True, blank=True,related_name='%(class)s_requests_created', on_delete=models.CASCADE)



    def save(self, *args, **kwargs):
        profile = self.author.profile
        self.company = profile.company
        self.country = profile.country
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    