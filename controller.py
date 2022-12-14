import model
import view
import logger


def run():
    # new_contact = ''
    to_search = view.cont_to_search()
    base = logger.get_base()
    result_search = model.search_data(base, to_search)
    if result_search != 0:
        view.show_contacts(to_search, result_search)
    else:
        new_contact = view.added_contact(to_search)
        logger.added_number(to_search, new_contact)
        view.contact_write(to_search, new_contact)
