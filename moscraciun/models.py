from django.db import models


class Wishing(models.Model):
    # Gender Choices
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    # Status Choices
    STATUS_CHOICES = [
        ('NOT_APPLIED', 'Not Applied'),
        ('APPLIED', 'Applied'),
        ('CONFIRMED', 'Confirmed'),
    ]

    # Fields
    name = models.CharField(max_length=100, verbose_name="Child's Name")
    age = models.PositiveIntegerField(verbose_name="Age")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    wishing_items = models.TextField(verbose_name="Wishing Items")  # List stored as text
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='NOT_APPLIED', verbose_name="Status")
    image = models.ImageField(upload_to='letters/', blank=True, null=True, verbose_name="Letter Image")  # New field

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set on every save

    def __str__(self):
        return f"{self.name} ({self.get_gender_display()} - Age {self.age})"

    class Meta:
        verbose_name = "Wishing"
        verbose_name_plural = "Wishings"
        ordering = ['name']


class Elf(models.Model):
    name = models.CharField(max_length=100, verbose_name="Elf Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email Address")
    associated_letter = models.ForeignKey('Wishing', on_delete=models.CASCADE, related_name='elves', verbose_name="Associated Letter")

    # New attribute for gift status
    sent = models.BooleanField(default=False, verbose_name="Gift Sent")  # Indicates if the gift was sent

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set on every save

    def __str__(self):
        return f"Elf: {self.name} ({self.email}) - Sent: {'Yes' if self.sent else 'No'}"
