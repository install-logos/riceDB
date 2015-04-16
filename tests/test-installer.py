from ricedb.rice import installer
from ricedb import ricemain
import unittest, os, sys
import argparse

class testInstaller(unittest.TestCase):
    """
    Testing the Rice download and installer methods
    """
    def setUp(self):
        self.test_prog = "i3"
        self.test_package = "test1"
        self.test_url = "http://github.com/install-logos/example-repo/archive/master.zip"


    def test_download(self):
        i3_test = installer.Installer(
            self.test_prog, 
            self.test_package,
            self.test_url 
        )

        i3_test.download()
        self.assertTrue(os.path.exists(os.path.expanduser("~/.rdb/i3/test1")))
        self.assertTrue(os.path.isdir(os.path.expanduser("~/.rdb/i3/test1")))

    def test_install(self):
        i3_test = installer.Installer(
            self.test_prog, 
            self.test_package, 
            self.test_url
        )
        i3_test.download()
        i3_test.install(True)
        self.assertFalse(os.path.exists(os.path.expanduser("~/.rdb/i3/test1/file1.conf")))
        self.assertTrue(os.path.exists(os.path.expanduser("~/.rdb/i3/test1/install.json")))

    def test_sync(self):

        awesome_test = ricemain.Rice()
        awesome_test.install_rice("awesome","okrice",True)
        self.assertTrue(os.path.exists(os.path.expanduser("~/.rdb/awesome/okrice/install.json")))
        self.assertFalse(os.path.exists(os.path.expanduser("~/.rdb/awesome/okrice/file1.conf")))
        self.assertTrue(os.path.exists(os.path.expanduser("~/.config/awesome/file1.conf")))

        
       # todo 

    def tearDown(self):
        os.system("rm -rf ~/.rdb/i3/test1/")
# Add in Query Return Test

# Add in Package Initialization Test

# Entire Pipeline should be tested

if __name__=="__main__":
    unittest.main()

