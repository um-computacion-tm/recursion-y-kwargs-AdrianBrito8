import unittest

def buscar_datos(*nombres_apellidos, database):
    for key, persona in database.items():
        if all(nombre_apellido in persona.values() for nombre_apellido in nombres_apellidos):
            return key
    return None

class TestBuscarDatos(unittest.TestCase):
    def setUp(self):

        self.database = {
            1: {
                "nombre1": "Pablo",
                "nombre2": "Diego",
                "apellido1": "Ruiz",
                "apellido2": "Picasso"
            },
            2: {
                "nombre1": "Elio",
                "apellido1": "Anci"
            },
            3: {
                "nombre1": "Elias",
                "nombre2": "Marcos",
                "nombre3": "Luciano",
                "apellido1": "Marcelo",
                "apellido2": "Gonzalez"
            }
        }

    def test_persona_existente(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", database=self.database)
        print("id para persona existente:", resultado)
        self.assertEqual(resultado, 1)

    def test_persona_con_un_solo_nombre_y_apellido(self):
        resultado = buscar_datos("Elio", "Anci", database=self.database)
        print("id persona con un solo nombre y apellido:", resultado)
        self.assertEqual(resultado, 2)

    def test_persona_con_multiples_nombres_y_apellidos(self):
        resultado = buscar_datos("Elias", "Marcos", "Luciano", "Marcelo", "Gonzalez", database=self.database)
        print("id persona con múltiples nombres y apellidos:", resultado)
        self.assertEqual(resultado, 3)

    def test_persona_que_no_existe(self):
        resultado = buscar_datos("Juan", "Perez", database=self.database)
        print("id persona que no existe:", resultado)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()

