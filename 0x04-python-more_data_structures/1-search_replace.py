#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def searchelement(element):
        return element if element != search else replace
    return list(map(searchelement, my_list))
