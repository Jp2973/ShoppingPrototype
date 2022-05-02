def tableView(headers, data, spaces: int = 15) -> None:
    """
    :param headers: List of header tuples with [(name of header, the key value for the data rows)]
    :param data: List of dictionary objects containing row data
    :param spaces: Optional argument for defining the ammount of space each column is given
    """
    [print (f"{header:^{spaces}}", end="") for header, _ in headers]
    for row in data:
        print()
        for _, col_name in headers:
            try:
                print(f"{row.get(col_name):^{spaces}}", end="")
            except:
                print(f"{'N/A':^{spaces}}", end="")
    print()



if __name__ == '__main__':
    tableView([("Price", "price"), ("Title", "title"), ("Author", "author")], [{"price": 5.8, "title": "A time to kill", "author": "Grisham"}, {"price": 18.90, "title": "Kid Lawyer", "author": "Grisham"}, {"price": 40, "title": "Helter Skelter", "author": "Gentry"}], spaces=25)