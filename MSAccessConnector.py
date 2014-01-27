# coding: utf-8
__author__ = 'dtrillo'
import adodbapi

nl = "\n"
debug = True

class MSAccessConnector():
    """ Clase para trabajar con bases de datos Microsoft Access en Python usando "adodbapi"    """
    def __init__(self, fichero_MDB):
        """ Inicializa OBJETO MSAccess """
        self.ErrMsg = ''
        self.cadConexion = ''
        self.consultas = []     # Listado de consultas realizadas
        self.enConexion = False
        self.fichero_MDB = ''
        self.abreFicheroMDB(fichero_MDB)

    def abreFicheroMDB(self, fichero_MDB):
        if fichero_MDB != self.fichero_MDB and len(fichero_MDB) > 0:
            if self.enConexion: self.cierraConexion()
            self.fichero_MDB = fichero_MDB
            self.__creaCadConexion()   # Crea conexion
            self.enConexion = self.abreConexion()

    def __del__(self):
        """ Al eliminar el OBJETO, cierra la conexion y elimina la conexion        """
        self.cierraConexion()
        self.conn = None
        self.consultas = []

    def abreConexion(self):
        """ Abre Conexion con BdD para empezar a trabajar """
        if len(self.cadConexion) == 0:
            self.ErrMsg = 'Sin Cadena de Conexion'
            self.conn = None
            return False
        if len(self.ErrMsg)>0: return False

        try:
            self.ErrMsg = ''
            self.conn = adodbapi.connect(self.cadConexion) # connect to the database
            if debug: print "Conectado!"
            self.SQL_listado_vaciar()       # Reinicia Listado de consutlas SQL
            return True
        except Exception, e:
            self.ErrMsg = 'Error al abrir Conexion' + nl + str(e)
            self.conn = None
            return False

    def cierraConexion(self):
        """ Cierra la conexion """
        try:
            self.conn.close()
        except:
            self.SQL_listado_vaciar()
        finally:
            self.SQL_listado_vaciar()
            self.enConexion = False

    def ejecuta(self, sql):
        if self.enConexion == False or len(self.ErrMsg)>0:
            return [], True
        try:
            cur = self.conn.cursor()
            try:
                cur.execute(sql)
                result = cur.fetchall() # show the result
                cur.close() # close the cursor and connection
                self.__agregaConsulta(sql)
                return result, False
            except Exception, f:
                self.ErrMsg = 'Error al ejecutar SQL ' + nl + str(f)
                return [], True
        except Exception, e:
            self.ErrMsg = 'Error al iniciar cursor!' + nl + str(e)
            return [], True

    def __creaCadConexion(self):
        """ Crea Cadena de Conexion con MDB """
        if len(self.fichero_MDB) == 0:
            self.cadConexion = ''
            return False
        else:
            #self.cadConexion = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s' % self.fichero_MDB
            self.cadConexion = 'Provider=Microsoft.ACE.OLEDB.12.0; Data Source=%s;Persist Security Info=False;' % self.fichero_MDB
            return True

    # Trabajando con Lista de SQL realizadas
    def __agregaConsulta(self, qsql):
        """ La consulta SQL se ha realizado con exito, y la guardo en el listado """
        if len(qsql) > 0:
            if not (qsql in self.consultas):
                self.consultas.append(qsql)
            else:
                self.consultas.remove(qsql)  # La quito de donde esta
                self.consultas.append(qsql)  # Pero la agrego al final

    def SQL_ultima(self):
        """ Devuelve la ultima SQL realizada """
        return self.consultas[-1]

    def SQL_listado(self):
        """ Devuelve la lista de consultas SQL realizadas con la conexion ABIERTA """
        return self.consultas

    def SQL_listado_vaciar(self):
        """ Vacia el contenido de consultas SQL """
        self.consultas = []
