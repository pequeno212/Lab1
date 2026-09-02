import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shay/a/aldana0/ece569-fall2026/Lab1/ws1/src/install/mypubsub'
