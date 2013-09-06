from django.db import models



Country_CHOICES = (
    (u'India', u'India'),
    (u'Nepal', u'Nepal'),
    (u'America', u'America'),
    (u'London', u'London'),
    (u'Peris', u'Peris'),
)

CURRENCY_CHOICES = (
    (u'R', u'Rupees'),
    (u'D', u'Dollar'),
    (u'Ry', u'Ryal'),
)
class Project_title(models.Model):
	
	project_title=models.CharField(
						max_length=50,
						verbose_name="Project Title"
						)
	Country=models.CharField(
					max_length=10,
					choices=Country_CHOICES
					)

	lat=models.FloatField()
	
	lng=models.FloatField()
	
	Status=models.CharField(
					max_length=50,
					verbose_name="status"
					)
	
	Type_of_units=models.CharField(
						verbose_name="Type of Unit",
						max_length=50
						)
	Starting_Price=models.IntegerField()
	
	Ending_Price=models.IntegerField()
	
	Currency=models.CharField(
					max_length=2,
					verbose_name="Currency",
					choices=CURRENCY_CHOICES
					)
	
	Developer_name=models.CharField(
						max_length=20,
						verbose_name="Developer Name"
							)
	Developer_website=models.URLField(max_length=200)
	
	Developer_logo=models.FileField(null=True, upload_to="images")
	
	Developer_financing=models.CharField(
							max_length=30,
							verbose_name="Developer Financing"
							)
	
	Availability=models.CharField(
						max_length=30,
						verbose_name="Purchase Availability For Foreigners"
						)
	Review_link=models.URLField(max_length=200)
	
	def __unicode__(self):
		return self.project_title
	
	class Meta:
		verbose_name="Project"
		verbose_name_plural="Projects" 
