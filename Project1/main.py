def do_stuff(num):
    try:
        result = int(num)+5
        return result
    except ValueError as err:
        return err
