from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80, )
    ad_username = models.CharField(max_length=255, null=True)
    talk_username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    blacklisted = models.BooleanField()
    w9_on_file = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=80, )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return str(self.name)

class Committee(models.Model):
    name = models.CharField(max_length=80, )
    chair_ad_group = models.CharField(max_length=80)
    team_ad_group = models.CharField(max_length=80)
    instructors_ad_group = models.CharField(max_length=80)
    wiki_home = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
class Room(models.Model):
    name = models.CharField(max_length=80, )
    exclusive = models.BooleanField(null=False, default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Tool(models.Model):
    name = models.CharField(max_length=80, )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

#class Registration(models.Model):
#    name = models.CharField(max_length=255, )
#    email = models.CharField(max_length=255, )
#    phone = models.CharField(max_length=255, )
#    ad_username = models.CharField(max_length=255,  )
#    send_text = models.BooleanField(default=True)
#    status = models.CharField(max_length=255, )
#    attended = models.BooleanField(default=False)
#    ad_assigned = models.BooleanField(default=False)
#    event_id = models.ForeignKey(Event)
#    edit_key = models.CharField(max_length=255) # TODO: find out what this does
#    transaction_id = models.CharField(max_length=255, ) # TODO: is this needed?
#    created = models.DateTimeField(auto_now_add=True)
#    modified = models.DateTimeField(auto_now=True)

class Prerequisite(models.Model):
    name = models.CharField(max_length=80, )
    ad_group = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Honorarium(models.Model):
    name = models.CharField(max_length=80, )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class EventTools(models.Model):
    name = models.CharField(max_length=80, )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Event(models.Model):
    name = models.CharField(max_length=80, )
    short_description = models.CharField(max_length=255, )
    long_description = models.TextField()
    advisories = models.TextField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    booking_start = models.DateField()
    booking_end = models.DateTimeField()
    cost = models.DecimalField(max_digits=15,decimal_places=2)
    eventbrite_link = models.CharField(max_length = 255) # TODO: do we want this still?
    meetup_link = models.CharField(max_length = 255) # TODO: do we want this?
    free_spaces = models.IntegerField()
    paid_spaces = models.IntegerField() # TODO: should it be possible to enable both if an event is paid?  What order are registrations filled?
    members_only = models.BooleanField()
    age_restriction = models.IntegerField(max_length=3, default=0)
    attendeees_require_approval = models.BooleanField(default=False)
    attendee_cancellation_end = models.DateTimeField()
    extend_registration = models.IntegerField(max_length=11, default=0)
    class_number = models.IntegerField(max_length=1, default=0)
    sponsored = models.BooleanField(default=False)
    status = models.CharField(max_length=20,default='pending')
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True )
    contact_id = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True )
    #fulfills_prerequisite_id = models.ForeignKey(Prerequisite, on_delete=models.SET_NULL, null=True, blank=True)
    #requires_prerequisite_id = models.ForeignKey(Prerequisite, on_delete=models.SET_NULL, null=True, blank=True)
    #part_of_id = models.ForeignKey(Event, on_delete=models.SET_DEFAULT blank=True) # TODO: figure out how to do this in Django
    #copy_of_id = models.ForeignKey(Event, on_delete=models.SET_DEFAULT blank=True)
    rejected_by = models.ForeignKey(Contact,related_name='%(class)s_rejected_contact_id', on_delete=models.SET_NULL, null=True, blank=True)
    rejection_reason = models.CharField(max_length = 255, blank=True)
    created_by = models.ForeignKey(Contact, related_name='%(class)s_created_contact_id', on_delete=models.SET_NULL, null=True)
    cancel_notification = models.BooleanField(default=True)
    reminder_notification = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

#class CategoryEvent(models.Model):
#    category_id = models.ForeignKey(Category)
#    event_id = models.ForeignKey(Event)
#    created = models.DateTimeField(auto_now_add=True)
#    modified = models.DateTimeField(auto_now=True)
