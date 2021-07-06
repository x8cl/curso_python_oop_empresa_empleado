import unittest
from empleado import Empleado

class test_Empleado(unittest.TestCase):

    """ Prueba para obtener sueldo """
    def test01_Empleado(self):
        empleado1 = Empleado("111-1", "Juan", "Perez", 180)
        self.assertEqual(empleado1.sueldo, 1800000)
    
    """ Prueba para obtener sueldo con horas extra """
    def test02_Empleado(self):
        empleado2 = Empleado("222-2", "Juanita", "Perez", 200, 12000)
        self.assertEqual(empleado2.sueldo, 2640000)
    
    """ Prueba para obtener email """
    def test03_Empleado(self):
        empleado2 = Empleado("222-2", "Juanita", "Perez", 200, 12000)
        self.assertEqual(empleado2.email, "jua.perez@coding-dojo.com")

    """ Prueba para obtener email nombre menos de 3 caracteres """
    def test04_Empleado(self):
        empleado2 = Empleado("222-2", "Ed", "Perez", 200, 12000)
        self.assertEqual(empleado2.email, "ed.perez@coding-dojo.com")

    
    
    
    
    def setUp(self):
        pass
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()