# # Import slugify()
# from django.utils.text import slugify


# def get_unique_slug(model_instance, sluggable_field_name, slug_field_name):
#     """Take a model instance, a sluggable field name (e.g. 'title')
#     on the model as a string, a slug field name (e.g. 'slug') on the
#     model as a string, and return a unique slug as a string."""

#     # Get the attribute that corresponds to sluggable_field_name (in our 
#     # case will be 'title') from model_instance (an instance of Article()),
#     # and slugify() it
#     slug = slugify(getattr(model_instance, sluggable_field_name))
    
#     # Not sure what this step is for
#     unique_slug = slug

#     # Set up a counter. This value will also be appended to the end
#     # of slugs in the event of duplicates
#     extension = 1

#     # Store the class of the received model instance in a variable
#     # because we need to access its model manager
#     ModelClass = model_instance.__class__

#     # In other words, 
#     while ModelClass._default_manager.filter(
#         **{slug_field_name: unique_slug}
#     ).exists():
#         unique_slug = '{}-{}'.format(slug, extension)
#         extension += 1

#     return unique_slug
