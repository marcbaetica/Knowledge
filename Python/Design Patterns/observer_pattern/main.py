import time
from observer_libs.publisher import Publisher
from observer_libs.subscriber import Subscriber


sub1 = Subscriber("Subscriber 1")
sub2 = Subscriber("Subscriber 2")
sub3 = Subscriber("Subscriber 3")

publisher = Publisher()
publisher.register(sub1)
publisher.register(sub2)
publisher.register(sub3)
publisher.unregister(sub2)

publisher.push(f"This is a message at time {time.time()}")

publisher.unregister(sub1)

time.sleep(1)
publisher.push(f"This is a message at time {time.time()}")

publisher.unregister(sub3)
publisher.push(f"This is a message at time {time.time()}")
