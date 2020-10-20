# 1. import unittest dari standar library
import unittest


# 2. buat class baru yang inherit dari TestClass
class TestSum(unittest.TestCase):
    
    # 3. setiap unit, dibuat method sendiri, dengan parameter self
    def test_sum(self):
        
        # 4. gunakan assert method yang sesuai
        self.assertEqual(sum([1, 2, 3]), 6, "Hasilnya harus 6")
        
    # 3.
    def test_sum_tuple(self):
        
        # 4.
        self.assertEqual(sum((1, 2, 1)), 6, 'Hasilnya harus 6')
        
# 5. masuk CLI untuk menjalankan unittest.main()
if __name__ == "__main__":
    unittest.main()