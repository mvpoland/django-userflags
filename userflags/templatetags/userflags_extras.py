import re

from django import template
from django.contrib.auth.models import User
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from userflags.models import Flag


register = template.Library()


class FlagsNode(template.Node):
    def __init__(self, user_id, var_name):
        self.user_id = template.Variable(user_id)
        self.var_name = var_name

    def render(self, context):
        user_id = self.user_id.resolve(context)
        user = User.objects.get(pk=user_id)

        flags_of_user = user.flag_set.all()
        flags = Flag.objects.order_by('name')

        userflags = []
        for flag in flags:
            userflags.append({'flag': flag, 'enabled': flag in flags_of_user})

        context[self.var_name] = userflags
        return ''


def get_flags_for_user(parser, token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    user_id, var_name = m.groups()
    return FlagsNode(user_id, var_name)

register.tag('get_flags_for_user', get_flags_for_user)


class FlagNode(template.Node):
    def __init__(self, flag_name, var_name):
        self.flag_name = flag_name
        self.var_name = var_name

    def render(self, context):
        flags = Flag.objects.filter(name__iexact=self.flag_name)
        if len(flags) > 0:
            context[self.var_name] = flags[0]
        return ''


def get_flag(parser, token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    flag_name, var_name = m.groups()
    if not (flag_name[0] == flag_name[-1] and flag_name[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    return FlagNode(flag_name[1:-1], var_name)

register.tag('get_flag', get_flag)
