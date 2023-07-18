from models.order import Order
from datetime import datetime as time
from random import randint

orders=[Order(f"Customer {i+1}",(str(time.now())[8:10],str(time.now())[5:7],str(time.now())[:4]),randint(1,4),None) for i in range(5)]