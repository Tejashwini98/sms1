from django.db import models
from django.contrib.auth.models import User

CAST_CHOICES = (
    ('hindu','hindu'),
    ('muslim','muslim'),
    ('general','general'),
    ('sc','sc'),
    ('st','st'),
)

STATUS_CHOICES = (
    ("processing", "processing"),
    ("reject", "reject"),
    ("approve", "approve"),
    ("pending", "pending"),
)

class Application(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adhar_card = models.ImageField(upload_to="adhar_cards")
    USN = models.CharField(max_length=20)
    college = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    caste = models.CharField(max_length=50, choices=CAST_CHOICES)
    merit = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default = "pending")
    college_id_card = models.ImageField(upload_to="id_cards", null=True)
    certificate = models.ImageField(upload_to="certificates", null=True)
    income_certificates = models.ImageField(upload_to="income_certificates", null=True)
    marks_cards_10th = models.ImageField(upload_to="marks_cards_10th", null=True)
    
    def __str__(self):
        return self.user.username


class Scheme(models.Model):
    introduction = models.TextField()
    income_ceiling = models.TextField()
    value_of_scholarship = models.TextField()
    how_and_when_to_apply =  models.TextField()
    publish = models.BooleanField(default=True)