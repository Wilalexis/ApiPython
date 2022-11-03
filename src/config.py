from distutils.command.config import config
from distutils.debug import DEBUG


class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'admin'
    MYSQL_DB = 'db_clientes'

config = {
    'development' : DevelopmentConfig
}