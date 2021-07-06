from empresa import Empresa

class Empleado:

    def __init__(self, rut, nombre, apellido, hTrabajadas, vHora = 10000):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.hTrabajadas = hTrabajadas
        self.vHora = vHora
        self.limMensual = 180
        self.factorHextra = 2
        self.email = ""
        self.sueldo = self.obtener_sueldo()

    def obtener_sueldo(self):
        sueldo = 0
        if self.hTrabajadas > self.limMensual:
            sueldo = (self.obtener_horas_extra() * self.vHora * self.factorHextra) + (self.limMensual * self.vHora)
        else:
            sueldo = self.hTrabajadas * self.vHora
        return sueldo

    def obtener_email(self,empleados):
        nombre = self.nombre.lower()[0:3]
        apellido = self.apellido.lower()
        dominio = "@coding-dojo.com"
        contador = 1
        email = f"{nombre}.{apellido}{dominio}"
        if empleados == []:
            self.email = email
        else:
            for i in empleados:
                if i.nombre.lower()[0:3] == nombre and i.apellido.lower() == apellido:
                    contador += 1
                    print(contador)
            if contador == 1:
                self.email = email
            else:
                email = f"{nombre}.{apellido}{contador}{dominio}"
        self.email = email
        return email

    def obtener_horas_extra(self):
        if self.hTrabajadas > self.limMensual:
            return self.hTrabajadas - self.limMensual
        return 0

    def info_empleado(self):
        datosEmpleado = ("-")*50 + "\n"
        datosEmpleado += f"RUT\t\t: {self.rut}\n"
        datosEmpleado += f"Nombre completo\t: {self.nombre} {self.apellido}\n"
        datosEmpleado += f"e-mail\t\t: {self.email}\n"
        datosEmpleado += f"Sueldo\t\t: {self.sueldo}\n"
        if self.obtener_horas_extra() > 0:
            datosEmpleado += f"Horas Extra\t: {self.obtener_horas_extra()}\n"
        return datosEmpleado


