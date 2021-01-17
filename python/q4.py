# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:55:11 2020

@author: Asifulla K
"""
class CryptoSquareTest(unittest.TestCase):
    def test_empty_string(self):
         self.assertEqual(encode(''), '')
         self.assertEqual(cipher_text(''), '')
    def test_lowercase(self):
        self.assertEqual(encode('A'), 'a')
        self.assertEqual(cipher_text('A'), 'a')
    def test_remove_spaces(self):
        self.assertEqual(encode('  b '), 'b')
        self.assertEqual(cipher_text('  b '), 'b')
    def test_remove_punctuation(self):
        self.assertEqual(encode('@1,%!'), '1')
        self.assertEqual(cipher_text('@1,%!'), '1')
    def test_9chars_results_3chunks(self):
        self.assertEqual(encode('This is fun!'), 'tsf hiu isn')
        self.assertEqual(cipher_text('This is fun!'), 'tsf hiu isn')
    def test_8chars_results_3chunks_ending_space(self):
        self.assertEqual(encode('Chill out.'), 'clu hlt io ')
        self.assertEqual(cipher_text('Chill out.'), 'clu hlt io ')
    def test_54chars_results_7chunks_2ending_space(self):
         self.assertEqual(
            encode('If man was meant to stay on the ground, '
                   'god would have given us roots.'),
            cipher_text('If man was meant to stay on the ground, '
                        'god would have given us roots.'),
             'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau ')
        