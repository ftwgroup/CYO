from django.db import models
import datetime

class Audition(models.Model):
    EXPERIENCE_CHOICES = (
        ('so','School Orchestra'),
        ('sb','school_band'),
        ('jb','jazz_band'),
        ('sc','school_chrous'),
        ('w1', 'wind_symphony_1'),
        ('w2', 'Wind Symphony'),
        ('co', 'COYO'),
        ('ot', 'Other'),
        )
    last = models.CharField('First Name', max_length=255)
    first = models.CharField('Last Name', max_length=255)
    email = models.CharField('Email Address', max_length=255)
    phone1 = models.IntegerField('Primary Phone Number \(XXX\)XXX\-XXXX', max_length=10)
    phone2 = models.IntegerField('Secondary Phone Number \(XXX\)XXX\-XXXX', max_length=10)
    experience = models.CharField('Experience', max_length=2, choices=EXPERIENCE_CHOICES)
    address = models.CharField('Address Number and Street)', max_length=255)
    city = models.CharField('City', max_length=255)
    birthday = models.DateTimeField('Your Birthday MMDDYYYY')
    submit_time = datetime.time

class AuditionerBackground(models.Model):
    audition = models.ForeignKey(Audition)
    instrument1 = models.CharField('Primary Instrument', max_length=255)
    teacher1 = models.CharField('Teacher Name', max_length=255)
    years1 = models.IntegerField('Years Played')
    instrument2 = models.CharField('Secondary Instrument', max_length=255)
    teacher2 = models.CharField('Teacher Name', max_length=255)
    years2 = models.IntegerField('Years Played')
    school = models.CharField('SchoolInstitution', max_length=255)
    grad_year = models.IntegerField('Graduation Year', max_length=4)
    school_director = models.CharField('School MusicOrchestra Director', max_length=255)
    audition_piece = models.CharField('Audition Piece Title', max_length=255)
    audition_piece_composer = models.CharField('Audition Piece Composer', max_length=255)
    additional_experience = models.TextField()

class ParentalInfo(models.Model):
    audition = models.ForeignKey(Audition)
    parent1 = models.CharField('Name of Parent/Guardian 1', max_length=255)
    parent2 = models.CharField('Name of Parent/Guardian 2', max_length=255)
    parent1_occupation = models.CharField('Parent 1 Occupation', max_length=255)
    parent2_occupation = models.CharField('Parent 2 Occupation', max_length=255)
