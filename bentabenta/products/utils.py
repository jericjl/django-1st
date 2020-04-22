import random
import string

from django.utils.text import slugify

def random_string_genereator(size=10, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug= None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    
    Klass = instance.__class__
    qs_exist = Klass.objects.filter(slug=slug).exists()
    if qs_exist:
        new_slug ="{slug}-{randstr}".format(
                    slug = slug,
                    randstr = random_string_genereator(size = 4)
                    )
        return unique_slug_generator(instance , new_slug = new_slug)
    return slug
            