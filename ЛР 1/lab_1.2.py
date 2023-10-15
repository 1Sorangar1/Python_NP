# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_in_Mb = 1.44
Kbs_in_Mb = 1024
Bs_in_Kb = 1024
disk_size_in_Bs = disk_size_in_Mb * Kbs_in_Mb * Bs_in_Kb
symbols_in_line = 25
lines_in_page = 50
pages_in_book = 100
symbol_size_in_Bs = 4
book_size_in_Bs = symbols_in_line * lines_in_page * pages_in_book * symbol_size_in_Bs


print("Количество книг, помещающихся на дискету:", int(disk_size_in_Bs//book_size_in_Bs))
