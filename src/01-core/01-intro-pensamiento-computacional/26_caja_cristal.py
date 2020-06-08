import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class CajaCristalTest(unittest.TestCase):
    def test_si_es_mayor(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_no_es_mayor(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()