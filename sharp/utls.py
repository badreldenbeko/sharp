# -*- coding: utf-8 -*-
from django.utils.text import slugify

'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''
import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)

    return slug


def upload_location(instance, filename):
    name = filename.split('.')
    Klass = str(instance.__class__.__name__)
    location = '{}/{}/{}.jpg'.format(Klass, instance.slug, name)
    return location


def get_filename(filename):
    return filename.upper()


def get_video_name(instance):
    video_n = instance.link.split('=')[1]
    video = video_n.split('&')[0]
    return video
