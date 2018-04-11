# -*- encoding: utf-8 -*-

from main import main


__all__ = ['main']


if __debug__:
    from main import application
    __all__ += ['application', 'const']


# vim: ts=4 sw=4 sts=4 et:
