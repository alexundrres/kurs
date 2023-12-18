from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class BD:
    def __init__(self):
        super(BD, self).__init__()
        self.rabotai()

    def rabotai(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("portal.db")
        if not db.open():
            return False
        query = QSqlQuery()
        query.exec("""CREATE TABLE IF NOT EXISTS ученики (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      имя TEXT,
                      фамилия TEXT,
                      логин TEXT,              
                      пароль TEXT,
                      возраст INTEGER,              
                      номер_телефона TEXT,
                      super_user TEXT DEFAULT no)""")
        return True