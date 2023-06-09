# Generated by Django 4.2.1 on 2023-05-12 20:47

from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields
import wagtail.blocks
import wagtail.contrib.routable_page.models
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField(verbose_name='Post date')),
                ('email_text', wagtail.fields.RichTextField()),
                ('teaser', wagtail.fields.RichTextField(default='<p>This is a teaser text for a newsletter</p>', max_length=150)),
                ('body', wagtail.fields.StreamField([('content', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=150)), ('sub_heading', wagtail.blocks.CharBlock(max_length=150)), ('text_content', wagtail.blocks.RichTextBlock()), ('thumbnail', wagtail.images.blocks.ImageChooserBlock(required=False))]))], use_json_field=True)),
                ('notify_subscribers', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date'],
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewsletterIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro_text', wagtail.fields.RichTextField(default='Some very helpful intro text here')),
                ('subscription_from_email', models.EmailField(max_length=254)),
                ('subscribe_heading', models.CharField(default='Subscribe to our newsletter', max_length=100)),
                ('subscribe_text', wagtail.fields.RichTextField(default='Please enter your name and email-address to subscribe to our newsletter')),
                ('subscribe_success_heading', models.CharField(default='Thank you', max_length=100)),
                ('subscribe_success_text', wagtail.fields.RichTextField(default='Thank you for subscribing. Please validate your email. A verification email has been sent to your email address.')),
                ('subscribe_fail_heading', models.CharField(default="We're sorry", max_length=100)),
                ('subscribe_fail_text', wagtail.fields.RichTextField(default='The email you entered may be already registered. Please Contact us to resolve the issue.')),
                ('unsubscribe_heading', models.CharField(default='Unsubscribe to our newsletter', max_length=100)),
                ('unsubscribe_text', wagtail.fields.RichTextField(default='Please enter your name and email-address to subscribe to our newsletter.')),
                ('unsubscribe_success_heading', models.CharField(default="It's a sad day. :(", max_length=100)),
                ('unsubscribe_success_text', wagtail.fields.RichTextField(default='You have successfully unsubscribed from our mailing list.\n We hope to see you again in the future')),
                ('validate_success_heading', models.CharField(default='Thank you.', max_length=100)),
                ('validate_success_text', wagtail.fields.RichTextField(default='our email has been validated. You are now officially subscribed to our newsletter.')),
                ('validate_fail_heading', models.CharField(default='Sorry, something went wrong.', max_length=100)),
                ('validate_fail_text', wagtail.fields.RichTextField(default='Your email could not be validated. Please contact us to solve this problem.')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', django_cryptography.fields.encrypt(models.CharField(max_length=256))),
                ('email', django_cryptography.fields.encrypt(models.CharField(max_length=254))),
                ('ident', models.CharField(max_length=1024)),
                ('validated', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, default=None, max_length=1024, null=True)),
            ],
        ),
    ]
