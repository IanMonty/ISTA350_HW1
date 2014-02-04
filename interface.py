"""
Author: <your name>
Date: <the date>
Class: ISTA 350
Section Leader: <your section leader>

Description:
<summary of this program>
"""

import functools

@functools.total_ordering
class Binary2C:
    """
    Class representing a two's compliment binary number.
    """

    def __init__(self, num_string = "0"):
        """
        The constructor takes any string of 0's and 1's,
        including the empty string. Characters other than 0 or 1 in the string
        raise a RuntimeError
        """
        
        if num_string == "":
            num_string = "0"

        self.num_list = []
        
        for i in range(len(num_string)):
            # check for valid input, raise error if not
            self.num_list.append(int(num_string[i]))
            
        self.trim()
            
    def trim(self): 
        """
        Remove extraneous leading 0's and 1's from a Binary2C object.
        This method modifies self, it does not create a new instance.
        """

        while len(self.num_list) > 1 and self.num_list[0] == self.num_list[1]:
            self.num_list.pop(0)
            
    def __repr__(self):
        """
        Return a string representation of a Binary2C object.
        Must not contain any extraneous leading 0's or 1's.
        """
        return ''.join(str(bit) for bit in self.num_list)

    def __add__(self, b2c):
        """
        Return a new Binary2C instance that = self + b2c
        """
        
        if(len(self.num_list) < len(b2c.num_list)):
        	first = self.num_list
        	second = b2c.num_list
        	for i in range(len(b2c.num_list) - len(self.num_list)):
        		first.insert(0,self.num_list[0])
        elif(len(self.num_list) > len(b2c.num_list)):
        	first = self.num_list
        	second = b2c.num_list
        	for i in range(len(self.num_list) - len(b2c.num_list)):
        		second.insert(0,b2c.num_list[0])
        else:
        	first = self.num_list
        	second = b2c.num_list
        
        print(first)
        print(second)
        
        hold = 0
        answer_str = ''
        for i in range(len(first)):
        	j =len(first) - i -1
        	if(first[j] + second[j] + hold == 3):
        		answer_str = '1' + answer_str
        		hold = 1
        	elif(first[j] + second[j] + hold == 2):
        		answer_str = '0' + answer_str
        		hold = 1
        	elif(first[j] + second[j] + hold == 1):
        		answer_str = '1' + answer_str
        		hold = 0
        	elif(first[j] + second[j] + hold == 0):
        		answer_str = '0' + answer_str
        		hold = 0
        	else:
        		print('ERROR')
        answer_str = str(hold) + answer_str
        answer = Binary2C(answer_str)
        self.trim()
        b2c.trim()
        return answer
        	

    def __neg__(self):
        """
        Return a new Binary2C instance that = -self
        """

    def __sub__(self, b2c):
        """
        Return a new Binary2C instance that = self - b2c
        """

    def __int__(self):
        """
        Return the integer value of the Binary2C object
        """

    def __eq__(self, b2c):
        """
        Return True if self == b2c, False otherwise
        """

    def __lt__(self, b2c):
        """
        Return True if self < b2c, False otherwise
        """

    def __abs__(self):
        """
        Return a new Binary2C instance that is the absolute value of self
        """



            