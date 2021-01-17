class Subscriber:
	def __init__(self, name):
		self.name = name

	def update(self, msg):
		print(f"{self.name} updated with message: {msg}")
