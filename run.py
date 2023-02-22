import os

import pytest




if __name__=='__main__':
    pytest.main(["case/test_login2.py","-s","--alluredir","report/allure-report"])
    os.system("allure generate report/allure-report -o")
    os.system("allure serve report/allure-report")
    #os.system("allure generate 报告需要的数据 -o 报告存放目录 --clean")
    #-o生成
    #allure generate生成报告指令，把../report/tmp 的文件-o生成报告out out一下，生成的报告放在../report/report
    #--clean把上次报告清除一下用--clean
    #allure报告生成的是一个服务，（本地服务）和jinkins结合，放在整个里面去集成，放到公共服务器里面
