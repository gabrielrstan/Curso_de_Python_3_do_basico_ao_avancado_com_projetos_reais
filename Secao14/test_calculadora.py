from unittest import TestCase, main

from calculadora import soma, subtrai


class TestCalculadora(TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 20, 30),
            (-10, 20, 10),
            (1.5, 2.5, 4.0),
            (10, 10.5, 20.5),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saidas):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma('10', 10)

    def test_soma_y_nao_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma(10, '10')

    def test_subtrai_5_e_5_deve_retornar_0(self):
        self.assertEqual(subtrai(5, 5), 0)

    def test_subtrai_5_negativo_e_5_deve_retornar_menos_10(self):
        self.assertEqual(subtrai(-5, 5), -10)

    def test_subtrai_varias_entradas(self):
        x_y_saidas = (
            (10, 20, -10),
            (-10, 20, -30),
            (1.5, 2.5, -1.0),
            (10, 10.5, -0.5),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saidas):
                x, y, saida = x_y_saida
                self.assertEqual(subtrai(x, y), saida)

    def test_subtrai_x_nao_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            subtrai('10', 10)

    def test_subtrai_y_nao_int_ou_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            subtrai(10, '10')


if __name__ == '__main__':
    main(verbosity=2)
