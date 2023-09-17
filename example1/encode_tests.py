import unittest
from example1.encoder import MorseEncoder

class EncodeTest(unittest.TestCase):
    def setUp(self):
        self.encoder = MorseEncoder()
    
    def test_letter_a(self):
        self.assertEqual(self.encoder.encode('a'), '.-')
    
    def test_letter_b(self):
        self.assertEqual(self.encoder.encode('b'), '-...')
    
    def test_letter_c(self):
        self.assertEqual(self.encoder.encode('c'), '-.-.')
    
    def test_letter_d(self):
        self.assertEqual(self.encoder.encode('d'), '-..')
    
    def test_letter_e(self):
        self.assertEqual(self.encoder.encode('e'), '.')
    
    def test_letter_f(self):
        self.assertEqual(self.encoder.encode('f'), '..-.')
    
    def test_letter_g(self):
        self.assertEqual(self.encoder.encode('g'), '--.')
    
    def test_letter_h(self):
        self.assertEqual(self.encoder.encode('h'), '....')
    
    def test_letter_i(self):
        self.assertEqual(self.encoder.encode('i'), '..')
    
    def test_letter_j(self):
        self.assertEqual(self.encoder.encode('j'), '.---')
    
    def test_letter_k(self):
        self.assertEqual(self.encoder.encode('k'), '-.-')
    
    def test_letter_l(self):
        self.assertEqual(self.encoder.encode('l'), '.-..')
    
    def test_letter_m(self):
        self.assertEqual(self.encoder.encode('m'), '--')
    
    def test_letter_n(self):
        self.assertEqual(self.encoder.encode('n'), '-.')
    
    def test_letter_o(self):
        self.assertEqual(self.encoder.encode('o'), '---')
    
    def test_letter_p(self):
        self.assertEqual(self.encoder.encode('p'), '.--.')
    
    def test_letter_q(self):
        self.assertEqual(self.encoder.encode('q'), '--.-')
    
    def test_letter_r(self):
        self.assertEqual(self.encoder.encode('r'), '.-.')
    
    def test_letter_s(self):
        self.assertEqual(self.encoder.encode('s'), '...')
    
    def test_letter_t(self):
        self.assertEqual(self.encoder.encode('t'), '-')
    
    def test_letter_u(self):
        self.assertEqual(self.encoder.encode('u'), '..-')
    
    def test_letter_v(self):
        self.assertEqual(self.encoder.encode('v'), '...-')
    
    def test_letter_w(self):
        self.assertEqual(self.encoder.encode('w'), '.--')
    
    def test_letter_x(self):
        self.assertEqual(self.encoder.encode('x'), '-..-')
    
    def test_letter_y(self):
        self.assertEqual(self.encoder.encode('y'), '-.--')
    
    def test_letter_z(self):
        self.assertEqual(self.encoder.encode('z'), '--..')
    
    def test_word_hello(self):
        self.assertEqual(self.encoder.encode('hello'), '.... . .-.. .-.. ---')
    
    def test_word_world(self):
        self.assertEqual(self.encoder.encode('world'), '.-- --- .-. .-.. -..')
    
    def test_phrase_hello_world(self):
        self.assertEqual(self.encoder.encode('hello world'), '.... . .-.. .-.. ---/.-- --- .-. .-.. -..')

if __name__ == '__main__':
    unittest.main()