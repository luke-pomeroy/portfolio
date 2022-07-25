import environ
from django import template

env = environ.Env()
environ.Env.read_env()

register = template.Library()


@register.simple_tag
def get_env_var(key):
    return env(key)