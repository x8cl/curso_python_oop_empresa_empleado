
class Empresa:

    def __init__(self, razonSocial, empleados = []):
        self.razonSocial = razonSocial
        self.empleados = empleados

    def contratar_empleado(self, nuevo_empleado):
        for i in self.empleados:
            if i.rut == nuevo_empleado.rut:
                return False
        nuevo_empleado.obtener_email(self.empleados)
        self.empleados.append(nuevo_empleado)
        return True
        
    def despedir_empleado(self, rut):
        for i in self.empleados:
            if rut == i.rut:
                self.empleados.remove(i)
                return True
        return False

    def obtener_total_hrs_extra(self):
        totHextra = 0
        for i in self.empleados:
            totHextra += i.obtener_horas_extra()
        return totHextra

    def obtener_total_sueldos(self):
        totSueldos = 0
        for i in self.empleados:
            totSueldos += i.obtener_sueldo()
        return totSueldos
    