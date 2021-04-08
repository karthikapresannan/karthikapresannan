def val_phno(func):
    def wrapper(phno):
        if len(phno)<10:
            raise Exception("invalid")
        else:
            return func(phno)
    return wrapper