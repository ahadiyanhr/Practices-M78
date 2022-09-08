import unittest
import sys
sys.path.append('.\\')

from core import managers as mng
from core.utils import create_tables
from users import models as usmdl


class DBManagerTest(unittest.TestCase):

    def setUp(self):
        self.db_manager = mng.DBManager()
        create_tables()

    def test_create_success(self):
        self.u1 = usmdl.User('Akbar', 'babaii', '09121231234', '0123456789', 20, 'ThisIsPassword')
        res = self.db_manager.create(self.u1)
        
        self.assertIsInstance(res, int)
        self.assertEqual(self.u1.id, res)

    def test_read_success(self):
        if not hasattr(self, 'u1'):
            self.test_create_success()
        self.db_manager = mng.DBManager()
        u = self.db_manager.read(usmdl.User, self.u1.id)
        
        self.assertEqual(vars(u), vars(self.u1))

    def test_update_success(self):
        if not hasattr(self, 'u1'):
            self.test_create_success()
        new_first_name = 'Reza'
        self.u1.first_name = new_first_name
        self.db_manager = mng.DBManager()
        self.db_manager.update(self.u1)

        self.db_manager = mng.DBManager()
        read_u = self.db_manager.read(usmdl.User, self.u1.id)
        self.assertEqual(read_u.first_name, new_first_name)

    def test_delete_success(self):
        if not hasattr(self, 'u1'):
            self.test_create_success()
        id = self.u1.id

        self.db_manager = mng.DBManager()
        self.db_manager.delete(self.u1)
        
        self.assertRaises(Exception, self.db_manager.read, usmdl.User, id)

    def tearDown(self) -> None:
        try:
            self.db_manager.delete(self.u1)
        except:
            pass
        del self.db_manager
    
if __name__ == '__main__':
    unittest.main()
