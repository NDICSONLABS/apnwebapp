import json

import django.forms
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
# Create your models here.
from django.db.models import CharField
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, FORM_FIELD_CHOICES, \
    AbstractFormSubmission
from wagtail.contrib.forms.views import SubmissionsListView
from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from home.block import CTABlock


class Partner(models.Model):
    """Partner model"""

    class PartnershipType:
        VOLUNTEER = 'VOLUNTEER'
        FOUNDING_PARTNER = 'FOUNDING PARTNER'
        DONOR = 'DONOR'
        PARTNERSHIP = (
            (VOLUNTEER, 'VOLUNTEER'),
            (FOUNDING_PARTNER, 'FOUNDING PARTNER'),
            (DONOR, 'DONOR'),
        )

    full_name = models.CharField(max_length=256)
    email = models.CharField(max_length=254)
    partnership_type = models.CharField(max_length=255, choices=PartnershipType.PARTNERSHIP)

    # validated = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class PartnershipPage(Page):
    template_name = "partnership/partnership_page.html"

    intro = RichTextField(
        default="""APN welcomes partners from different countries and ministries all over the world to support and facilitate the realization of its mission. Partnership is established by a longterm commitment to either financially support the mission, and/or volunteer skill/time for service. You can partner financially by subscribing for a periodic contribution and/or by volunteering your time and skills. """)  # noqa

    body = StreamField([
        ("CTA", CTABlock())
    ], use_json_field=True)
    content_panels = Page.content_panels + [
        # MultiFieldPanel([
        # InlinePanel('carousel', max_num=5, min_num=1, label="Carousel Image")], heading="Hero Section"), # noqa
        # MultiFieldPanel([
        #     InlinePanel('testimonial', max_num=4, min_num=1, label="Testimony")], heading="Testimonial Section"), # noqa
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    def get_context_data(self, **kwargs):
        context = super(PartnersPage, self).get_context_data(**kwargs)
        print(context)
        return context

    class Meta:
        verbose_name = 'Partnership Page'
        verbose_name = 'Partnerships Page'


class PartnersPage(RoutablePageMixin, Page): pass


# @route(r'^volunteer')
# def volunteer(self, request, *args, **kwargs):
#     if request.method == 'GET':
#         context = self.get_context(request, *args, **kwargs)
#         return render(request, "partnership/volunteer.html", context)
# # elif request.method == 'POST':
#     context = self.get_context(request, *args, **kwargs)
#     name = request.POST.get('name')
#     email = request.POST.get('email')
# if not FormsPage.objects.filter(page_type="volunteer_form"):
#     subscriber = Subscriber(full_name=name, email=email, ident=ident, token=token) # noqa
#     subscriber.save()
#     message = f'''
#         Thank you for subscribing to our newsletter
#         Please follow the link below to validate your email adress. If you cannot click the link. Copy it into your browser. # noqa
#         {NewsletterIndex.objects.live().public()[0].get_full_url()}/validate?token={token}">{NewsletterIndex.objects.live().public()[0].get_full_url()}/validate?token={token}
#     '''
#     html_message = f'''
#         <h3>Thank you for subscribing to our newsletter</h3>
#         <p>Please click the link below to validate your email adress.</p> # noqa
#         <a href="{NewsletterIndex.objects.live().public()[0].get_full_url()}/validate?token={token}">{NewsletterIndex.objects.live().public()[0].get_full_url()}/validate?token={token}</a> # noqa
#     '''
#     send_mail(
#         subject='Please verify your Email Address',
#         message=message,
#         html_message=html_message,
#         from_email=self.subscription_from_email,
#         recipient_list=[email],
#         fail_silently=True
#     )
#     context['token'] = html_message
#     return render(request, "partnership/email_success.html", context)

#
# class FormField(AbstractFormField):
#     page = ParentalKey(
#         'FormsPage',
#         on_delete=models.CASCADE,
#         related_name='form_fields',
#     )
#
#
# class FormsPage(AbstractEmailForm):
#     template = "forms/forms_page.html"
#     # This is the default path.
#     # If ignored, Wagtail adds _landing.html to your template name
#     landing_page_template = "forms/forms_page_landing.html"
#
#     intro = RichTextField(blank=True)
#     thank_you_text = RichTextField(blank=True)
#     page_type = CharField(max_length=255, blank=False, choices=(
#         ('contact_form', "Contact Form"),
#         ('donation_form', "Donation Form"),
#         ('volunteer_form', "Volunteer Form")
#     ), default='contact_form')
#
#     content_panels = AbstractEmailForm.content_panels + [
#         FieldPanel('intro'),
#         FieldPanel('page_type'),
#         InlinePanel('form_fields', label='Form Fields'),
#         FieldPanel('thank_you_text'),
#         MultiFieldPanel([
#             FieldRowPanel([
#                 FieldPanel('from_address', classname="col6"),
#                 FieldPanel('to_address', classname="col6"),
#             ]),
#             FieldPanel("subject"),
#         ], heading="Email Settings"),
#     ]

def filename_to_title(filename):
    from os.path import splitext
    if filename:
        result = splitext(filename)[0]
        result = result.replace('-', ' ').replace('_', ' ')
        return result.title()


class FormField(AbstractFormField):
    FORM_FIELD_CHOICES = list(FORM_FIELD_CHOICES) + [('file_upload', 'Upload File')]
    field_type = models.CharField(
        verbose_name=('field type'),
        max_length=16,
        choices=FORM_FIELD_CHOICES)
    page = ParentalKey('FormsPage', related_name='form_fields', on_delete=models.CASCADE)


class ExtendedFormBuilder(FormBuilder):
    def create_file_upload_field(self, field, options):
        return django.forms.FileField(**options)

    # FIELD_TYPES = FormBuilder
    # FIELD_TYPES.update({
    #     'document': create_document_upload_field,
    # })


class CustomSubmissionsListView(SubmissionsListView):
    """
    further customisation of submission list can be done here
    """
    paginate_by = 50  # show more submissions per page, default is 20
    ordering = ('submit_time',)  # order submissions by oldest first, normally newest first
    ordering_csv = ('-submit_time',)  # order csv export by newest first, normally oldest first

    # override the method to generate csv filename
    def get_csv_filename(self):
        """ Returns the filename for CSV file with page slug at start"""
        filename = super().get_csv_filename()
        return self.form_page.slug + '-' + filename


class CustomFormSubmission(AbstractFormSubmission):
    # important - adding this custom model will make existing submissions unavailable
    # can be resolved with a custom migration

    def get_data(self):
        """
        Here we hook in to the data representation that the form submission returns
        Note: there is another way to do this with a custom SubmissionsListView
        However, this gives a bit more granular control
        """

        file_form_fields = [
            field.clean_name for field in self.page.specific.get_form_fields()
            if field.field_type == 'file_upload'
        ]

        data = super().get_data()

        for field_name, field_vale in data.items():
            if field_name in file_form_fields:
                # now we can update the 'representation' of this value
                # we could query the FormUploadedFile based on field_vale (pk)
                # then return the filename etc.
                pass

        return data


class FormUploadedFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    field_name = models.CharField(blank=True, max_length=254)


class FormsPage(AbstractEmailForm):
    form_builder = ExtendedFormBuilder

    def serve(self, request, *args, **kwargs):
        # if self.get_submission_class().objects.filter(page=self, user__pk=request.user.pk).exists():
        #     return render(
        #         request,
        #         self.template,
        #         self.get_context(request)
        #     )
        if request.method == 'POST':
            # form = self.get_form(request.POST, page=self, user=request.user)  # Original line
            form = self.get_form(request.POST, request.FILES, page=self, user=request.user)
            print("validity: ", form.is_valid(), form)
            print(request.POST, "\n\n", request.FILES, "\n\n", self, "\n\n", request.user)
            if form.is_valid():
                self.process_form_submission(form)
                return render(
                    request,
                    self.get_landing_page_template(request),
                    self.get_context(request)
                )
        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context['form'] = form
        return render(
            request,
            self.get_template(request),
            context
        )

    def get_submission_class(self):
        """
        Returns submission class.
        Important: will make your existing data no longer visible, only needed if you want to customise
        the get_data call on the form submission class, but might come in handy if you do it early

        You can override this method to provide custom submission class.
        Your class must be inherited from AbstractFormSubmission.
        """

        return CustomFormSubmission

    def process_form_submission(self, form):
        """
        Accepts form instance with submitted data, user and page.
        Creates submission instance.

        You can override this method if you want to have custom creation logic.
        For example, if you want to save reference to a user.
        """

        file_form_fields = [field.clean_name for field in self.get_form_fields() if field.field_type == 'file_upload']

        for (field_name, field_value) in form.cleaned_data.items():
            if field_name in file_form_fields:
                uploaded_file = FormUploadedFile.objects.create(
                    file=field_value,
                    field_name=field_name
                )

                # store a reference to the pk (as this can be converted to JSON)
                form.cleaned_data[field_name] = uploaded_file.pk

        return self.get_submission_class().objects.create(
            form_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder),
            page=self,
        )

    def get_form_fields(self):
        return self.form_fields.all()

    # def process_form_submission(self, form):
    #     return self.get_submission_class().objects.create(
    #         form_data=form.cleaned_data,
    #         page=self, user=form.user
    #     )

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    template = "forms/forms_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "forms/forms_page_landing.html"

    page_type = CharField(max_length=255, blank=False, choices=(
        ('contact_form', "Contact Form"),
        ('donation_form', "Donation Form"),
        ('volunteer_form', "Volunteer Form")
    ), default='contact_form')

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('page_type'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Settings"),
    ]
