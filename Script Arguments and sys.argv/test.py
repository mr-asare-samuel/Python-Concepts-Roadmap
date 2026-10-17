import sys
print(sys.argv)

#run in the terminal: python test.py arg1 arg2 arg3
# this prints ['test.py', 'arg1', 'arg2', 'arg3']
"""
That’s all sys.argv is. The terminal splits what you typed by spaces, and Python gives you the words as a list. python3 itself is not in the list. Everything starts from the script name.

sys.argv[0] is 'test.py'
sys.argv[1] is 'hello'
sys.argv[2] is '42'

Notice '42' is in quotes. It’s text, not a number. Everything in sys.argv is text.
"""