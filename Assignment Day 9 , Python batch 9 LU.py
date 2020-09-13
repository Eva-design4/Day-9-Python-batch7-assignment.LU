#!/usr/bin/env python
# coding: utf-8

# # Question 1

# Write a python function for finding if a given number is prime or not and do unit testing on it using Pylint and unit testing library

# In[31]:


get_ipython().run_cell_magic('writefile', 'prime.py', '\n\'\'\'creating a python file to find out if a given number is prime or not\n\'\'\'\ndef is_prime(num):\n    \'\'\' Function to check for prime number\n    \'\'\'\n    if num >= 1:\n        for i in range(2, num):\n            if num%i == 0:\n                res = " not prime "\n            else:\n                res = "is prime"\n            print(res)\n        ')


# In[32]:


get_ipython().system('pylint "prime.py"')


# In[37]:


get_ipython().run_cell_magic('writefile', 'primeUnitTest.py', '\nimport unittest\nimport prime\n\nclass testPrime(unittest.TestCase):\n    def testSinglePrime(self):\n        x = 9\n        result = prime.is_prime(x)\n        self.assertTrue(result, "Prime")\n        \n    def testingDoublePrime(self):\n        y = 5 \n        result = prime.is_prime(y)\n        self.assertTrue(result, "Prime")\n\nif __name__ == "__main__":\n    unittest.main()')


# In[38]:


get_ipython().system('python primeUnitTest.py')


# # Question  2

# Make a small generator program for returning armstrong numbers betwwen 1-1000 in a generator object.
# 

# In[2]:


lst = list(range(1,1000+1))

def armstrong(lst):    
    for num in lst:
        s = 0
        temp = num
        while temp > 0:
            d = temp % 10
            s += d ** 3
            temp //= 10
        if num == s:
            yield num


# In[3]:


list(armstrong(lst))


# In[ ]:




