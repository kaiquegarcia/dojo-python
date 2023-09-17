import unittest

class DecodeTest(unittest.TestCase):
    def setUp(self):
        self.encoder = MorseEncoder()
    
    def test_letter_a(self):
        self.assertEqual(self.encoder.decode('.-'), 'a')
    
    def test_letter_b(self):
        self.assertEqual(self.encoder.decode('-...'), 'b')
    
    def test_letter_c(self):
        self.assertEqual(self.encoder.decode('-.-.'), 'c')
    
    def test_letter_d(self):
        self.assertEqual(self.encoder.decode('-..'), 'd')
    
    def test_letter_e(self):
        self.assertEqual(self.encoder.decode('.'), 'e')
    
    def test_letter_f(self):
        self.assertEqual(self.encoder.decode('..-.'), 'f')
    
    def test_letter_g(self):
        self.assertEqual(self.encoder.decode('--.'), 'g')
    
    def test_letter_h(self):
        self.assertEqual(self.encoder.decode('....'), 'h')
    
    def test_letter_i(self):
        self.assertEqual(self.encoder.decode('..'), 'i')
    
    def test_letter_j(self):
        self.assertEqual(self.encoder.decode('.---'), 'j')
    
    def test_letter_k(self):
        self.assertEqual(self.encoder.decode('-.-'), 'k')
    
    def test_letter_l(self):
        self.assertEqual(self.encoder.decode('.-..'), 'l')
    
    def test_letter_m(self):
        self.assertEqual(self.encoder.decode('--'), 'm')
    
    def test_letter_n(self):
        self.assertEqual(self.encoder.decode('-.'), 'n')
    
    def test_letter_o(self):
        self.assertEqual(self.encoder.decode('---'), 'o')
    
    def test_letter_p(self):
        self.assertEqual(self.encoder.decode('.--.'), 'p')
    
    def test_letter_q(self):
        self.assertEqual(self.encoder.decode('--.-'), 'q')
    
    def test_letter_r(self):
        self.assertEqual(self.encoder.decode('.-.'), 'r')
    
    def test_letter_s(self):
        self.assertEqual(self.encoder.decode('...'), 's')
    
    def test_letter_t(self):
        self.assertEqual(self.encoder.decode('-'), 't')
    
    def test_letter_u(self):
        self.assertEqual(self.encoder.decode('..-'), 'u')
    
    def test_letter_v(self):
        self.assertEqual(self.encoder.decode('...-'), 'v')
    
    def test_letter_w(self):
        self.assertEqual(self.encoder.decode('.--'), 'w')
    
    def test_letter_x(self):
        self.assertEqual(self.encoder.decode('-..-'), 'x')
    
    def test_letter_y(self):
        self.assertEqual(self.encoder.decode('-.--'), 'y')
    
    def test_letter_z(self):
        self.assertEqual(self.encoder.decode('--..'), 'z')
    
    def test_word_hello(self):
        self.assertEqual(self.encoder.decode('.... . .-.. .-.. ---'), 'hello')
    
    def test_word_world(self):
        self.assertEqual(self.encoder.decode('.-- --- .-. .-.. -..'), 'world')
    
    def test_phrase_hello_world(self):
        self.assertEqual(self.encoder.decode('.... . .-.. .-.. ---/.-- --- .-. .-.. -..'), 'hello world')

if __name__ == '__main__':
    unittest.main()