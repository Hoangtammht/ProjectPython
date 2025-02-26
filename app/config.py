import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://sa:Hoangtam39@localhost/TestVietQR?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
