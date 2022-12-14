import controller


def search_data(base, to_search):
    try:
        result = base[to_search]
        return result
    except:
        return 0
