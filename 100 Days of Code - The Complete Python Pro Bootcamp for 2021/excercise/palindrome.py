import unittest

def palindrome(text):
    test = []
    result = []
    for i in range(0,(len(text))):
        test.append(text[i])
    for i in range(1,(len(text)+1)):
        result.append(text[-i])
    for i in range(0,len(result)):
        if test[i] == result[i]:
            return True
        else:
            return False

#print(palindrome("kodok"))
class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(palindrome("budi"), False)
        self.assertEqual(palindrome("kodok"), True)
        self.assertEqual(palindrome("baso"), False)
        self.assertEqual(palindrome("ada"), True)


if __name__ == '__main__':
    unittest.main()
