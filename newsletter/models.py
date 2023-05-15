from django.db import models
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from wagtail.models import Page

from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel # noqa
from wagtail.images.blocks import ImageChooserBlock

from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from django_cryptography.fields import encrypt

from hashlib import sha256


class Subscriber(models.Model):
    """Newsletter Subscriber model"""
    full_name = encrypt(models.CharField(max_length=256))
    email = encrypt(models.CharField(max_length=254))
    ident = models.CharField(max_length=1024)
    validated = models.BooleanField(default=False)
    token = models.CharField(default=None, max_length=1024, null=True, blank=True) # noqa

    def __str__(self):
        return self.full_name


class ContentBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=150)
    sub_heading = blocks.CharBlock(required=False, max_length=150)
    text_content = blocks.RichTextBlock()
    thumbnail = ImageChooserBlock(required=False)

    class Meta:
        form_classname = 'Content Block'
        template = 'newsletter/content_block.html'
        icon = 'doc-empty'


class NewsletterIndex(RoutablePageMixin, Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['Newsletter']
    max_count = 1

    intro_text = RichTextField(default='Some very helpful intro text here')

    # Texts and headers for subscription pages
    subscription_from_email = models.EmailField()
    subscribe_heading = models.CharField(max_length=100, default='Subscribe to our newsletter') # noqa
    subscribe_text = RichTextField(default='Please enter your name and email-address to subscribe to our newsletter') # noqa
    subscribe_success_heading = models.CharField(max_length=100, default='Thank you') # noqa
    subscribe_success_text = RichTextField(default='Thank you for subscribing. Please validate your email. A verification email has been sent to your email address.') # noqa
    subscribe_fail_heading = models.CharField(max_length=100, default="We're sorry") # noqa
    subscribe_fail_text = RichTextField(default='The email you entered may be already registered. Please Contact us to resolve the issue.') # noqa
    unsubscribe_heading = models.CharField(max_length=100, default='Unsubscribe to our newsletter') # noqa
    unsubscribe_text = RichTextField(default='Please enter your name and email-address to subscribe to our newsletter.') # noqa
    unsubscribe_success_heading = models.CharField(max_length=100, default="It's a sad day. :(") # noqa
    unsubscribe_success_text = RichTextField(default="You have successfully unsubscribed from our mailing list.\n We hope to see you again in the future") # noqa
    validate_success_heading = models.CharField(max_length=100, default='Thank you.') # noqa
    validate_success_text = RichTextField(default='our email has been validated. You are now officially subscribed to our newsletter.') # noqa
    validate_fail_heading = models.CharField(max_length=100, default='Sorry, something went wrong.') # noqa
    validate_fail_text = RichTextField(default='Your email could not be validated. Please contact us to solve this problem.') # noqa

    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
        MultiFieldPanel([
            FieldPanel('subscription_from_email'),
            FieldPanel('subscribe_heading'),
            FieldPanel('subscribe_text'),
            FieldPanel('subscribe_success_heading'),
            FieldPanel('subscribe_success_text'),
            FieldPanel('subscribe_fail_heading'),
            FieldPanel('subscribe_fail_text'),
        ], heading='Subscription Settings.'),
        MultiFieldPanel([
            FieldPanel('unsubscribe_heading'),
            FieldPanel('unsubscribe_text'),
            FieldPanel('unsubscribe_success_heading'),
            FieldPanel('unsubscribe_success_text'),
        ], heading='Unsubscribe Settings.'),
        MultiFieldPanel([
            FieldPanel('validate_success_heading'),
            FieldPanel('validate_success_text'),
            FieldPanel('validate_fail_heading'),
            FieldPanel('validate_fail_text')
        ], heading='Validation Settings.')
    ]

    def get_context(self, request, *args, **kwargs):
        '''Modidy page context here'''
        context = super().get_context(request, *args, **kwargs)
        # pagination 10 per page
        newsletters = Newsletter.objects.child_of(self).live().public().order_by('-date') # noqa
        context['newsletters'] = newsletters

        return context

    @route(r'^latest')
    def latest_newsletter(self, request, *args, **kwargs):
        newest = Newsletter.objects.child_of(self).live().public().order_by('-date') # noqa
        newest_post = newest.first().get_url()
        return redirect(newest_post)

    @route(r'^subscribe')
    def subscribe_page(self, request, *args, **kwargs):
        if request.method == 'GET':
            context = self.get_context(request, *args, **kwargs)
            return render(request, "newsletter/subscribe.html", context)
        elif request.method == 'POST':
            context = self.get_context(request, *args, **kwargs)
            name = request.POST.get('name')
            email = request.POST.get('email')
            token = sha256(bytes(name + email, encoding='utf-8')).hexdigest()
            ident = sha256(bytes(email, encoding='utf-8')).hexdigest()
            if not Subscriber.objects.filter(ident=ident):
                subscriber = Subscriber(full_name=name, email=email, ident=ident, token=token) # noqa
                subscriber.save()
                message = f'''
                    Thank you for subscribing to our newsletter
                    Please follow the link below to validate your email adress. If you cannot click the link. Copy it into your browser. # noqa
                    {NewsletterIndex.objects.live().public()[0].get_full_url()}/validate?token={token}">{NewsletterIndex.objects.live().public()[0].get_full_url()}/validate?token={token}
                '''
                html_message = f'''
                    <h3>Thank you for subscribing to our newsletter</h3>
                    <p>Please click the link below to validate your email adress.</p> # noqa
                    <a href="{NewsletterIndex.objects.live().public()[0].get_full_url()}/validate?token={token}">{NewsletterIndex.objects.live().public()[0].get_full_url()}/validate?token={token}</a> # noqa
                '''
                send_mail(
                    subject='Please verify your Email Address',
                    message=message,
                    html_message=html_message,
                    from_email=self.subscription_from_email,
                    recipient_list=[email],
                    fail_silently=True
                )
                context['token'] = html_message
                return render(request, "newsletter/subscribe_success.html", context) # noqa
            else:
                return render(request, 'newsletter/subscribe_fail.html', context) # noqa

    @route(r'^unsubscribe')
    def unsubscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)

        if request.method == 'GET':
            return render(request, "newsletter/unsubscribe.html", context)
        elif request.method == 'POST':
            email = request.POST.get('email')
            ident = sha256(bytes(email, encoding='utf-8')).hexdigest()
            subscribers = Subscriber.objects.filter(ident=ident)
            if subscribers:
                for subscriber in subscribers:
                    subscriber.delete()
            return render(request, "newsletter/unsubscribe_success.html", context) # noqa

    @route(r'^validate')
    def validate(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        token = request.GET.get('token')

        if token is None:
            return redirect(NewsletterIndex.objects.live().public()[0].get_url()) # noqa
        else:
            subscriber = Subscriber.objects.get(token=token)
            if subscriber:
                subscriber.validated = True
                subscriber.token = None
                subscriber.save()
                return render(request, "newsletter/validate_success.html", context) # noqa
            else:
                return render(request, "newsletter/validate_fail.html", context) # noqa


class Newsletter(Page):

    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    email_text = RichTextField()
    teaser = RichTextField(max_length=150, default='<p>This is a teaser text for a newsletter</p>') # noqa
    body = StreamField([
        ('content', ContentBlock()),
    ], use_json_field=True)
    notify_subscribers = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('author'),
            FieldPanel('date'),
            FieldPanel('email_text'),
        ], heading='Metadata'),
        FieldPanel('notify_subscribers', heading='Notify Newsletter Subscribers'), # noqa
        FieldPanel('body'),
    ]

    parent_page_types = ['NewsletterIndex']
    subpage_types = []

    class Meta:
        ordering = ['date']
