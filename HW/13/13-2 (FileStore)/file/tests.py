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

    # def test_update_success(self):
    #     if not hasattr(self, 'f1'):
    #         self.test_create_success()
    #     new_first_name = 'Reza'
    #     self.f1.first_name = new_first_name
    #     self.db_manager = DBManager()
    #     self.db_manager.update(self.u1)

    #     self.db_manager = DBManager()
    #     read_u = self.db_manager.read(User, self.u1.id)
    #     self.assertEqual(read_u.first_name, new_first_name)

    # def test_delete_success(self):
    #     if not hasattr(self, 'u1'):
    #         self.test_create_success()
    #     id = self.u1.id

    #     self.db_manager = DBManager()
    #     self.db_manager.delete(self.u1)
        
    #     self.assertRaises(Exception, self.db_manager.read, User, id)

    # def tearDown(self) -> None:
    #     try:
    #         self.db_manager.delete(self.f1)
    #     except:
    #         pass
    #     del self.db_manager
    
if __name__ == '__main__':
    unittest.main()