# 读取ini配置文件需要使用Python3自带的configparser库
from configparser import ConfigParser   # Python2中是from ConfigParser import ConfigParser

class LoadingConfig(object):
    def __init__(self):
        self.path='C:\\Users\\jiangtan\\IdeaProjects\\2023\\Configerration\\configrauation.ini'
        con=self.readini()
        self.defualt_ual=con['env']['uat_url']
        print(self.defualt_ual)




    def readini(self):
        conf = ConfigParser()  # 需要实例化一个ConfigParser对象
        conf.read(self.path,encoding='utf-8')  # 需要添加上config.ini的路径，不需要open打开，直接给文件路径就读取，也可以指定encoding='utf-8'
        # print(conf.sections())  # 读取user段的name变量的值，字符串格式
        # print('读取配置文件',self.path)  # 读取变量的值，字符串格式
        return conf

    def allseaction(self):
        conf=ConfigParser()
        conf.read(self.path)
        print(conf['Role'])

        # for key, value in conf['Role'].items():
        #  print(key, value)  #循环输出ini列表



if __name__=='__main__':
    f=LoadingConfig()
    f.readini()
    f.allseaction()





