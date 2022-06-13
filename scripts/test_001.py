import allure
import pytest
import sys, os
sys.path.append(os.getcwd())


class Test_Abc:
    @allure.step(title="第一个测试页面")
    # 严重级别
    # @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.severity(allure.severity_level.BLOCKER)
    def test_abc_001(self):
        allure.attach("描述", "断言失败")
        assert 1
        # assert 0

    @allure.step(title="第二个测试页面")
    # 严重级别
    # @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    # bug地址
    @allure.issue("http://www.baidu.com/bug/test_abc_001", "断言失败~~~")
    # 测试用例地址
    @allure.testcase("http://www.baidu.com/test_abc_001")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_abc_001(self):
        allure.attach("描述", "断言失败")
        # assert 1
        assert 0


if __name__ == '__main__':
    # pytest.main(["-s --alluredir report", "test_001.py"])
    pytest.main(["test_001.py", "-s", "--alluredir", "../report"])
    # 每一次运行都删除上一次报告数据
    # os.system("allure generate ../report -o ./report --clear")
