for i in range(1980, 2017) :
    url = 'http://www.ndbc.noaa.gov/view_text_file.php?filename=45005h{0}.txt.gz&dir=data/historical/stdmet/'
    print(url.format(i))