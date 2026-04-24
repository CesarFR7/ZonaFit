from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = "SELECT * FROM cliente ORDER BY id"
    SELECCIONAR_ID = "SELECT * FROM cliente WHERE id = %s"
    INSERTAR = "INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s,%s,%s)"
    ACTUALIZAR = "UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM cliente WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Ocurrio un error al seleccinar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valor = (id,)
            cursor.execute(cls.SELECCIONAR_ID, valor)
            registro = cursor.fetchone()
            # Mapeo de clase-tabla cliente
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
            return cliente
        except Exception as e:
            print(f"Ocurrio un error al seleccinar clientes por id: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            print(valores)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrio un error la insertar un cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrio un error al actualizar: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            id = (cliente.id,)
            cursor.execute(cls.ELIMINAR, id)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrio un error al eliminar: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == "__main__":
    # Insertar cliente
    # cliente1 = Cliente(nombre="Lucia", apellido="Mendez", membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f"Clientes insertaados: {clientes_insertados}")

    # Actualizar cliente
    # cliente2 = Cliente(3, "Olga", "Mendez", 400)
    # clientes_actalizados = ClienteDAO.actualizar(cliente2)
    # print(f"Clientes actualizados: {clientes_actalizados}")

    # # Eliminar cliente
    # cliente3 = Cliente(id=3)
    # cliente_eliminado = ClienteDAO.eliminar(cliente3)
    # print(f"Clientes eliminados: {cliente_eliminado}")

    # # Seleccionar los clientes
    # clientes = ClienteDAO.seleccionar()
    # for cliente in clientes:
    #     print(cliente)

        # Seleccionar los clientes
    cliente = ClienteDAO.seleccionar_id(1)
    print(cliente)
