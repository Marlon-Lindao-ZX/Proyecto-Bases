import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Logging_ui import Logging_ui
from principal_ui import principal_ui
from mysql.connector.pooling import MySQLConnectionPool

class Logging():
    def __init__(self, parent=None):
        self.Logging=QtWidgets.QMainWindow()
        self.ui=Logging_ui()
        self.ui.setupUi(self.Logging)
        self.ui.btn_Ing.clicked.connect(self.ingresar)
        self.ui.btn_lim.clicked.connect(self.limpiar)

    def ingresar(self):
            self.usu = self.ui.txt_usu.text()
            self.pas = self.ui.txt_con.text()
            self.dbconfig = {  # configuracion que se va a pasar para conectar a la base de datos
                "user": self.usu,
                "password": self.pas,
                'host': '127.0.0.1',
                "database": "proyecto", }
            try:
                self.cnx = mysql.connector.connect( **self.dbconfig)  # se usa el mysql.connector para obtener una conexion pasandole la configuracion
                print("hola")
                QMessageBox.about(self.Logging, "Exito!", "Bienvenido usuario: " + self.usu)
                self.principal = main_hub(self.dbconfig)
                self.principal.principal.show()
                self.Logging.hide()
                self.cnx.close()  # cierro conexion


            except Exception:
                QMessageBox.about(self.Logging, "Error!", "El nombre de usuario y/o la contrasena no coinciden")

    def limpiar(self):
        self.ui.txt_usu.clear()
        self.ui.txt_con.clear()



class main_hub():
    def __init__(self, dbconfig):
        self.principal = QtWidgets.QMainWindow()  # defino una ventana que va a contener todos los widgets
        self.dbconfig = dbconfig
        self.ui = principal_ui()  # importo los widgets
        self.ui.setupUi(self.principal)

        self.ui.Mostrar_btn.clicked.connect(self.mostrar)  # ahora puedo manipular los widgets a traves de ui
        self.ui.Actualizar_btn.clicked.connect(self.borrar)
        self.ui.Insertar_btn.clicked.connect(self.insertar)
        self.ui.Borrar_btn.clicked.connect(self.borrar)
        self.ui.pushButton.clicked.connect(self.agregar_detalle)

        self.ui.Tabs.currentChanged.connect(self.limpiar_tabla)

        self.objeto_conexion = Db_conexion(self.dbconfig, self.principal)
        self.objeto_conexion.tabla_participacion(self.ui)

        self.objeto_conexion = Db_conexion(self.dbconfig, self.principal)
        self.objeto_conexion.poblar_combobox1(self.ui)

        self.objeto_conexion = Db_conexion(self.dbconfig, self.principal)
        self.objeto_conexion.poblar_combobox2(self.ui)

        self.ui.tableWidget.setColumnCount(3)


    def limpiar_tabla(self):
       self.ui.tableWidget_3.clear()
       self.ui.tableWidget_3.setRowCount(0)
       self.ui.tableWidget_3.setColumnCount(0)

       self.ui.tableWidget.clear()
       self.ui.tableWidget.setRowCount(0)
       self.ui.tableWidget.setColumnCount(0)
       self.ui.linetotal.setText("0")


    def agregar_detalle(self):
        self.lista=[]
        self.Item = self.ui.comboBox_2.currentText()

        self.Item=self.Item.split()

        for i in self.Item:
            self.lista.append(i)

        self.cantidad=self.ui.lineEdit_3.text()
        self.lista.append(self.cantidad)


        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

        self.row = self.ui.tableWidget.rowCount()


        self.col = 0
        for i in self.lista:


            self.ui.tableWidget.setItem(self.row-1, self.col, QtWidgets.QTableWidgetItem(str(i)))
            self.col=self.col+1

        print(self.row)

        twi0 = self.ui.tableWidget.item(self.row - 1, 1).text()

        twi1 = self.ui.tableWidget.item(self.row - 1, 2).text()

        self.total=float(twi0)*float(twi1)


        self.total=float(self.ui.linetotal.text())+ self.total
        self.ui.linetotal.setText(str(self.total))



    def mostrar(self):
            self.objeto_conexion = Db_conexion(self.dbconfig, self.principal)#Se le pasa la configuracion de
            # la db para crear una instancia de la clase

            self.objeto_conexion.mostrar(self.ui)#usa la funcion mostrar definida dentreo de la clase

    def borrar(self):
            self.objeto_conexion = Db_conexion(self.dbconfig, self.principal)

            self.objeto_conexion.borrar(self.ui)

    def insertar(self):
            self.objeto_conexion = Db_conexion(self.dbconfig, self.principal)

            self.objeto_conexion.insertar(self.ui)

class Db_conexion():#clase que maneja todo_lo relacionado con la conexion a la base de datos incuyendo todas las operaciones C.R.U.D

    def __init__(self, dbconfig,window):
        self.window=window
        self.dbconfig = dbconfig
        self.colnames=0
        self.cnxpool = self.create_pool(pool_name="assa", pool_size=1)

    def create_pool(self, pool_name, pool_size):
        return mysql.connector.pooling.MySQLConnectionPool(pool_name=pool_name, pool_size=pool_size, **self.dbconfig)

    def mostrar(self,ui):

        try:

            self.index = ui.Tabs.currentIndex()

            self.currentTabText = ui.Tabs.tabText(self.index)

            self.cnx = self.cnxpool.get_connection()

            self.cur = self.cnx.cursor(buffered=True)

            self.query = 'SELECT * FROM ' + self.currentTabText


            if self.currentTabText=="Persona":
                self.tipo=str(ui.comboBox.currentText())
                if self.tipo=='Miembro':
                    self.query = 'SELECT Cedula,Nombre,Apellido FROM ' + self.tipo+" join Persona on "+"Miembro.Cod_miembro=Persona.Cedula"
                if  self.tipo=='Entrenador':
                    self.query = 'SELECT Cedula,Nombre,Apellido FROM ' + self.tipo + " join Persona on " + "Entrenador.Cod_entrenador=Persona.Cedula"

            if self.currentTabText == "Clase":
                self.query = 'SELECT id_clase,entrenador AS "Cedula entrenador",Nombre,Apellido,horario,Descripcion FROM ' + self.currentTabText + " join Persona on " + "Clase.entrenador=Persona.Cedula join Disciplina on Clase.disciplina=Disciplina.Id_disciplina"

            if self.currentTabText=="Participacion":
                self.cedula=ui.line1_5.text()
                if self.cedula=="":
                    self.query= 'SELECT PerM.Cedula AS "Cedula Miembro",PerM.Nombre AS "Nombre Miembro",PerM.Apellido AS "Apellido Miembro",PerE.Nombre AS "Nombre Entrenador",PerE.Apellido AS "Apellido Entrenador",C.horario,D.descripcion FROM Participacion as P join Persona as PerM on P.id_miembro=PerM.Cedula join Clase as C on P.id_clase=C.id_clase join Disciplina as D on C.disciplina=D.Id_disciplina join Persona as PerE on C.entrenador=PerE.Cedula order by PerM.Cedula,C.horario'
                else:
                    self.query = 'SELECT PerM.Cedula AS "Cedula Miembro",PerM.Nombre AS "Nombre Miembro",PerM.Apellido AS "Apellido Miembro",PerE.Nombre AS "Nombre Entrenador",PerE.Apellido AS "Apellido Entrenador",C.horario,D.descripcion FROM Participacion as P join Persona as PerM on P.id_miembro=PerM.Cedula join Clase as C on P.id_clase=C.id_clase join Disciplina as D on C.disciplina=D.Id_disciplina join Persona as PerE on C.entrenador=PerE.Cedula WHERE PerM.Cedula='+self.cedula+' order by PerM.Cedula,C.horario'

            if self.currentTabText=="Venta":
                self.query = "SELECT * FROM Factura where Tipo_transaccion='venta'"

            if self.currentTabText=="Compra":
                self.query = "SELECT * FROM Factura where Tipo_transaccion='compra'"




            self.cur.execute(self.query)

            self.rowcount = self.cur.rowcount

            self.colnames = [desc[0] for desc in self.cur.description]

            self.colcount=len(self.colnames)

            ui.tableWidget_3.horizontalHeader().setStretchLastSection(True)
            ui.tableWidget_3.setRowCount(self.rowcount)  ##set number of rows
            ui.tableWidget_3.setColumnCount(self.colcount)
            ui.tableWidget_3.setHorizontalHeaderLabels(self.colnames)
            row = 0

            while True:
                sqlRow = self.cur.fetchone()
                if sqlRow == None:
                    break  ##stops while loop if there is no more lines in sql table
                for col in range(0, self.colcount):  ##otherwise add row into tableWidget
                    ui.tableWidget_3.setItem(row, col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))


                row += 1

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

        self.cur.close()
        self.cnx.close()

    def poblar_combobox1(self,ui):
        self.cnx = self.cnxpool.get_connection()
        self.cur = self.cnx.cursor(buffered=True)
        self.query = 'SELECT descripcion FROM  disciplina'
        self.cur.execute(self.query)
        self.disciplinas=self.cur.fetchall()

        self.lista=[]

        for i in self.disciplinas:
            self.lista.append(i[0])

        ui.comboBox_4.addItems(self.lista)

        self.cur.close()
        self.cnx.close()

    def poblar_combobox2(self, ui):
        self.cnx = self.cnxpool.get_connection()
        self.cur = self.cnx.cursor(buffered=True)
        self.query = 'SELECT * FROM implemento'
        self.cur.execute(self.query)
        self.implementos = self.cur.fetchall()


        self.lista = []

        for i in self.implementos:
            print(i)
            self.lista.append(i[2]+" "+str(i[1]))

        ui.comboBox_2.addItems(self.lista)

        self.cur.close()
        self.cnx.close()


    def tabla_participacion(self,ui):
        self.cnx = self.cnxpool.get_connection()

        self.cur = self.cnx.cursor(buffered=True)

        self.query = 'SELECT id_clase,entrenador AS "Cedula entrenador",Nombre,Apellido,horario,Descripcion FROM  Clase join Persona on Clase.entrenador=Persona.Cedula join Disciplina on Clase.disciplina=Disciplina.Id_disciplina'

        self.cur.execute(self.query)

        self.rowcount = self.cur.rowcount
        print(self.rowcount)

        self.colnames = [desc[0] for desc in self.cur.description]
        print(self.colnames)

        self.colcount = len(self.colnames)
        print(self.colcount)

        ui.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        ui.tableWidget_4.setRowCount(self.rowcount)  ##set number of rows
        ui.tableWidget_4.setColumnCount(self.colcount)
        ui.tableWidget_4.setHorizontalHeaderLabels(self.colnames)
        row = 0

        while True:
            sqlRow = self.cur.fetchone()

            if sqlRow == None:

                break  ##stops while loop if there is no more lines in sql table
            for col in range(0, self.colcount):  ##otherwise add row into tableWidget
                ui.tableWidget_4.setItem(row, col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))

            row += 1




        self.cur.close()
        self.cnx.close()



    def borrar(self,ui):

        try:
            self.index = ui.Tabs.currentIndex()
            self.currentTabText = ui.Tabs.tabText(self.index)
            self.cnx = self.cnxpool.get_connection()
            self.cur = self.cnx.cursor(buffered=True)
            self.query = 'SELECT * FROM ' + self.currentTabText+' LIMIT 0'
            self.cur.execute(self.query)
            self.colnames = [desc[0] for desc in self.cur.description]


            if self.currentTabText=="Persona" and ui.comboBox.currentText()=="Entrenador":
                self.row = ui.tableWidget_3.currentRow()
                self.field1 = ui.tableWidget_3.item(self.row, 0).text()
                self.query = """DELETE FROM Entrenador  WHERE cod_entrenador""" + """=%s"""
                print(self.query)
                self.cur.execute(self.query, (self.field1,))
                self.cnx.commit()

            else:
                self.row = ui.tableWidget_3.currentRow()
                self.field1 = ui.tableWidget_3.item(self.row, 0).text()
                self.query = """DELETE FROM Entrenador  WHERE """ + self.colnames[0] + """=%s"""
                print(self.query)
                self.cur.execute(self.query, (self.field1,))
                self.cnx.commit()


            #
            # if self.index == 1:
            #
            #         self.row = ui.tableWidget_2.currentRow()
            #         self.field1 = ui.tableWidget_2.item(self.row, 0).text()
            #         self.query = """DELETE FROM """ + self.currentTabText + """ WHERE """ + self.colnames[0] + """=%s"""
            #         self.cur.execute(self.query, (self.field1,))
            #         self.cnx.commit()

        except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))

        # if index == 2:
        #
        #     self.r = ui.tableWidget_3.currentRow()
        #     self.field1 = ui.tableWidget_3.item(self.r, 0).text()
        #
        #     try:
        #         self.query = """DELETE FROM """ + currentTabText + """ WHERE """ + self.colnames[0] + """=%s"""
        #         self.cur.execute(self.query, (self.field1,))
        #         self.cnx.commit()


        self.cur.close()
        self.cnx.close()

    def insertar(self,ui):

        try:
            self.index = ui.Tabs.currentIndex()
            self.currentTabText = ui.Tabs.tabText(self.index)
            self.cnx = self.cnxpool.get_connection()
            self.cur = self.cnx.cursor(buffered=True)

            if self.currentTabText == "Persona":

                self.insert_tuple = (ui.line1_1.text(), ui.line1_2.text(), ui.line1_3.text())
                self.query = """INSERT INTO """ + self.currentTabText + """ VALUES (%s,%s,%s)"""
                self.cur.execute(self.query, self.insert_tuple)


                if ui.comboBox.currentText()=="Miembro":
                    self.query = """INSERT INTO miembro VALUES (%s)"""
                    self.insert_tuple = (ui.line1_1.text(),)
                    self.cur.execute(self.query, self.insert_tuple)


                if ui.comboBox.currentText()=="Entrenador":
                    self.query = """INSERT INTO entrenador (cod_entrenador) VALUES (%s)"""
                    self.insert_tuple = (ui.line1_1.text(),)
                    self.cur.execute(self.query, self.insert_tuple)




            if self.currentTabText == "Disciplina":
                    self.insert_tuple = (ui.line1_4.text(), )
                    self.query = """INSERT INTO """ + self.currentTabText + """(descripcion) VALUES (%s)"""
                    self.cur.execute(self.query, self.insert_tuple)


            if self.currentTabText == "Clase":
                    self.Clase=str(ui.comboBox_4.currentText())


                    self.query1="Select Id_disciplina from Disciplina Where Descripcion='"+self.Clase+"'"
                    self.cur.execute(self.query1)
                    self.id_disciplina=self.cur.fetchall()[0][0]

                    self.t=ui.timeEdit.time()
                    self.t_string =self.t.toString(ui.timeEdit.displayFormat())
                    print(self.t_string)

                    self.insert_tuple = (ui.lineEdit_5.text(),self.id_disciplina,self.t_string )
                    self.query = """INSERT INTO """ + self.currentTabText +"""(entrenador,disciplina,horario)"""+""" VALUES (%s,%s,%s)"""
                    self.cur.execute(self.query, self.insert_tuple)

            if self.currentTabText == "Participacion":
                self.row = ui.tableWidget_4.currentRow()
                self.id_clase = ui.tableWidget_4.item(self.row, 0).text()
                print(self.id_clase)

                self.insert_tuple =(ui.line1_5.text(),self.id_clase,)
                print(str(ui.line1_5))
                self.query = """INSERT INTO """ + self.currentTabText +""" VALUES (%s,%s)"""
                self.cur.execute(self.query, self.insert_tuple)

            if self.currentTabText == "Inventario":

                self.insert_tuple =(ui.line1_6.text(),ui.lineEdit_6.text())

                self.query = """INSERT INTO """ + self.currentTabText +"""(descripcion,stock) VALUES (%s,%s)"""
                self.cur.execute(self.query, self.insert_tuple)

            if self.currentTabText == "Implemento":

                self.insert_tuple =(ui.lineEdit.text(),ui.lineEdit_2.text(),ui.lineEdit_7.text())

                self.query = """INSERT INTO """ + self.currentTabText +"""(descripcion,precio_actual,stock) VALUES (%s,%s,%s)"""
                self.cur.execute(self.query, self.insert_tuple)

            if self.currentTabText == "Venta":
                self.total=float(ui.linetotal.text())
                self.miembro=ui.lineEdit_4.text()
                self.insert_tuple =(self.total,self.currentTabText,self.miembro)

                self.query = """INSERT INTO  Factura (monto_total,tipo_transaccion,cod_miembro) VALUES (%s,%s,%s)"""

                self.cur.execute(self.query, self.insert_tuple)

                self.row=ui.tableWidget.rowCount()

                # for i in range(0,self.row):
                #     self.query_id="Select cod_implemento from implemento WHERE descripcion="+ui.tableWidget.item(self.row - 1, 2).text()
                #     self.cur.execute(self.query_id)
                #     self.cod=self.cur.fetchall()[0]
                #
                #
                #     self.insert_tuple = (6,self.cod, )
                #
                #     self.query = """INSERT INTO  Factura (monto_total,tipo_transaccion,cod_miembro) VALUES (%s,%s,%s)"""




                #
                # for row in allRows(0, allRows):
                #     precio = self.ui.tableWidget.item(row, 1)
                #     self.total=
                #
                #     twi0.text() + ' ' + twi1.currentText() + ' ' + twi2.currentText()


            self.cnx.commit()
            self.cur.close()
            self.cnx.close()


        except mysql.connector.Error as err:

            print("Something went wrong: {}".format(err))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myMainWindow = Logging()

    myMainWindow.Logging.show()#muestra la ventana principal que conitene sus respectivos widgets
    sys.exit(app.exec_())