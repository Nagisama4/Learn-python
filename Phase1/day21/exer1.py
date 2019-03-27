def access_limite(func):
    def wrapper(*args, **kwargs):
    	print("access limite")
    	return func(*args,**kwargs)
    return wrapper

@access_limite
def enter_background():
	print("enter background")

@access_limite
def delete_order(order_id):
	print("delete order", order_id)


enter_background()
delete_order(101)