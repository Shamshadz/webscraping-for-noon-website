from django.db import models
from django.template.defaultfilters import slugify 

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=200, primary_key=True,unique=True)
    slug = models.SlugField(null=True,blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.state)
        return super().save(*args, **kwargs)

    def __str__(self):
        # Return a string that represents the instance
        return f"{self.state}"



class Categorie(models.Model):
    job_categorey = models.CharField(max_length=200, primary_key=True)
    slug = models.SlugField(null=True,blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.job_categorey)
        return super().save(*args, **kwargs)

    def __str__(self):
        # Return a string that represents the instance
        return f"{self.job_categorey}"



class SubCategorie(models.Model):
    job_categorey = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING)
    job_sub_categorey = models.CharField(max_length=200, primary_key=True)
    slug = models.SlugField(null=True,blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.job_sub_categorey)
        return super().save(*args, **kwargs)

    def __str__(self):
        # Return a string that represents the instance
        return f"{self.job_sub_categorey}"


class CompanyDetail(models.Model):
    name = models.CharField(max_length=200,primary_key=True,unique=True)
    description = models.CharField(max_length=2000)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    job_sub_categorey = models.ForeignKey(SubCategorie, on_delete=models.DO_NOTHING)
    slug = models.SlugField(null=True,blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        # Return a string that represents the instance
        return f"{self.name}"



class JobDetail(models.Model):
    job_position = models.CharField(max_length=200,unique=True)
    company = models.ForeignKey(CompanyDetail, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=300)
    job_sub_categorey = models.ForeignKey(SubCategorie, on_delete=models.DO_NOTHING)

    slug = models.SlugField(null=True,blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.job_position)
        return super().save(*args, **kwargs)

    def __str__(self):
        # Return a string that represents the instance
        return f"{self.job_position}"