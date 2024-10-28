# -*- coding: utf-8 -*-

from jinja2.filters import pass_context


@pass_context
def commentif(context, text, cond=True, style="plain", **kw):
    """Apply comment filter if cond is True"""
    comment = context.environment.filters["comment"]

    if cond:
        return comment(text, style, **kw)
    else:
        return text


class FilterModule(object):
    """Ansible port jinja2 filters"""

    def filters(self):
        return {
            "commentif": commentif,
        }
