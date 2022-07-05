from django.db import models

EXPERIENCE_TYPES = [
        ('WORK', 'Work Experience'),
        ('EDUCATION', 'Education'),
        ('COURSE', 'Course'),
    ]    

class Experience(models.Model):
    type = models.CharField(max_length=10, choices=EXPERIENCE_TYPES, default='WORK')
    title = models.CharField(max_length=100, help_text='Job or course title.')
    organisation = models.CharField(max_length=100, help_text='Workplace or university.')
    order = models.PositiveIntegerField(default=1)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.organisation}: {self.title}'
    
    class Meta:
        ordering = ['type', 'order']


class ExperiencePoint(models.Model):
    experience = models.ForeignKey('Experience', on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    order = models.PositiveIntegerField(default=1)
    current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text
        
    class Meta:
        ordering = ['order']

class KeySkill(models.Model):
    text = models.TextField(max_length=1000)
    order = models.PositiveIntegerField(default=1)
    current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
        
    class Meta:
        ordering = ['order']


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    demo_url = models.URLField(null=True, blank=True)
    git_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='images')
    order = models.PositiveIntegerField(default=1)
    current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
            
    class Meta:
        ordering = ['order']
