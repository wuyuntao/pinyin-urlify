#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

The PinYinMap is scrapped from pyzh project

The WesternMaps are scrapped from django admin

"""
import re


WesternMaps = [ LatinMap, LatinSymbolMap, GreekMap, TurkishMap, \
                RussianMap, UkrainianMap, CzechMap, PolishMap, LatvianMap ]

PinYinMap = dict([(ord(k), v[0])for k, v in PinYinMap.items()])

for i in xrange(len(WesternMaps)):
    WesternMaps[i] = dict([(ord(k), v) for k, v in WesternMaps[i].items()])

RemoveList = [u'a', u'an', u'as', u'at', u'before', u'but', u'by', u'for', u'from',
              u'is', u'in', u'into', u'like', u'of', u'off', u'on', u'onto', u'per',
              u'since', u'than', u'the', u'this', u'that', u'to', u'up', u'via',
              u'with']

ReservedList = [u'blog', u'edit', u'delete', u'new', u'popular', u'wiki']


def urlify(urlstring, default='default', max_length=50,
           remove_list=RemoveList, reserved_list=ReservedList):
    '''
    populates a normalized urlstring

    '''

    slug = ''

    re_alnum = re.compile(r'[\w\s\-]+')
    re_remove = re.compile('|'.join([r'\b%s\b' % word for word in remove_list]))
    re_reserved = re.compile('|'.join([r'\b%s\b' % word for word in reserved_list]))
    re_space = re.compile(r'[\s_\-]+')

    for char in urlstring:
        if len(slug) >= max_length:
            break
        if re_alnum.match(char):
            slug += char
            continue
        char_ord = ord(char)
        if char_ord in PinYinMap:
            slug += u' ' + PinYinMap[char_ord] + u' '
            continue
        for dict in WesternMaps:
            if char_ord in dict:
                slug += dict[char_ord]
                break

    slug = re_remove.sub(u'', slug.lower())
    slug = re_space.sub(u'-', slug.strip())
    if slug is '' or re_reserved.match(slug):
        slug = default

    return slug

