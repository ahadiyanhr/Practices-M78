import unittest
import sys
sys.path.append('.\\')

import core.managers as mng
from core.utils import create_tables
from configs import DB_CONNECTION
from file import models as flmdl
from users import models as usmdl


class DBManagerTest(unittest.TestCase):

    def setUp(self):
        self.db_manager = mng.DBManager()
        create_tables()

    def test_create_success(self):
        self.f1 = flmdl.File('File1', '1990-02-08', '2010-10-30', 2, 'ThisIsPassword')
        res = self.db_manager.create(self.f1)
        
        self.assertIsInstance(res, int)
        self.assertEqual(self.f1.id, res)

    def test_read_success(self):
        if not hasattr(self, 'f1'):
            self.test_create_success()
        self.db_manager = mng.DBManager()
        f = self.db_manager.read(flmdl.File, self.f1.id)
        
        self.assertEqual(vars(f), vars(self.f1))

    def test_update_success(self):
        if not hasattr(self, 'f1'):
            self.test_create_success()
        new_file_name = 'myBooks'
        self.f1.file_name = new_file_name
        self.db_manager = mng.DBManager()
        self.db_manager.update(self.f1)

        self.db_manager = mng.DBManager()
        read_u = self.db_manager.read(flmdl.File, self.f1.id)
        self.assertEqual(read_u.file_name, new_file_name)

    def test_delete_success(self):
        if not hasattr(self, 'f1'):
            self.test_create_success()
        id = self.f1.id

        self.db_manager = mng.DBManager()
        self.db_manager.delete(self.f1)
        
        self.assertRaises(Exception, self.db_manager.read, flmdl.File, id)

    def tearDown(self) -> None:
        try:
            self.db_manager.delete(self.f1)
        except:
            pass
        del self.db_manager
    
if __name__ == '__main__':
    unittest.main()