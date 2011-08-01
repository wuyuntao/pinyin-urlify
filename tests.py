# -*- coding: UTF-8 -*-

import unittest
from urlify import urlify

class PinYinTestCase(unittest.TestCase):
    def testChinese(self):
        self.assertEqual(urlify(u'公共的模'),
                         u'gong-gong-de-mo')

    def testEnglish(self): 
        self.assertEqual(urlify(u'WOW! We Say ENGLISH!!!'),
                         u'wow-we-say-english')

    def testWestern(self): 
        self.assertEqual(urlify(u'ÀÞβ Λğ-Ґє'),
                         u'athb-lg-gye')

    def testMixedText(self):
        self.assertEqual(urlify(u'  公共的  模asdf!　'),
                         u'gong-gong-de-mo-asdf')

    def testHyphen(self):
        self.assertEqual(urlify(u'公共-的模'),
                         u'gong-gong-de-mo')

    def testEmpty(self):
        self.assertEqual(urlify(u''),
                         u'default')

    def testNotInMaps(self):
        self.assertEqual(urlify(u'コにちわ'),
                         u'default')

    def testStopWords(self):
        self.assertEqual(urlify(u'hello, this is an blahblah'),
                         u'hello-blahblah')

    def testReservedWords(self):
        self.assertEqual(urlify(u'  blog  '),
                         u'default')

    def testMaxLengthLimit(self):
        self.assertEqual(urlify(u'urlstring url instance class request embodies. Example, data headers, calling:'),
                         u'urlstring-url-instance-class-request-embodies-exam')

    def testHyphen(self):
        self.assertEqual(urlify(u'Hello•Hello'),
                         u'xuan-feng-dao-ying-2008-imagetunnel')
        #self.assertEqual(urlify(u'旋风倒影•2008•Imagetunnel'),
        #                 u'xuan-feng-dao-ying-2008-imagetunnel')
        #self.assertEqual(urlify(u'旋风倒影•2008•Imagetunnel'),
        #                 u'xuan-feng-dao-ying-2008-imagetunnel')

    def testUnderline(self):
        self.assertEqual(urlify(u'pinyin urlify_30'), 'pinyin-urlify-30')

if __name__ == '__main__':
    unittest.main()
