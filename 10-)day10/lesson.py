def format_name(f_name, l_name):
    # f_name = f_name[0].upper() + f_name[1:-1] + f_name[-1]
    result = f_name + " " + l_name
    
    print(result.title())
    
format_name("fatih", "kayacı")