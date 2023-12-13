import unittest

from unittest.loader import makeSuite


from test_cases.framework import Test
from test_cases.framework import TestMediumPage
from test_cases.dashboard import TestDashboardPageLanguage
from test_cases.add_player import TestAddPlayerPage
from test_cases.add_player import TestAddPlayerForm
from test_cases.add_player import TestUpdateLastCreatedPlayerForm
from test_cases.add_player import TestUpdateWrongLastCreatedPlayerForm
from test_cases.login_to_the_system import TestLoginPage
from test_cases.login_to_the_system import TestLoginPageWrongData



def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(Test))
   test_suite.addTest(makeSuite(TestMediumPage))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestLoginPageWrongData))
   test_suite.addTest(makeSuite(TestDashboardPageLanguage))
   test_suite.addTest(makeSuite(TestAddPlayerPage))
   test_suite.addTest(makeSuite(TestAddPlayerForm))
   test_suite.addTest(makeSuite(TestUpdateLastCreatedPlayerForm))
   test_suite.addTest(makeSuite(TestUpdateWrongLastCreatedPlayerForm))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
