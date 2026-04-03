import threading


def hello():
	print("hello world")
t = threading.Timer(2, hello)
t.start()