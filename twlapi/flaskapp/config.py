'''
@author: A. Ayeva
'''
# -*- coding: utf-8 -*-


class Config(object):
    """
    Common configurations
    """


    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../../twlapi.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
   


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig
}

#DEBUG = True
