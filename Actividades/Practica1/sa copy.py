N = ["<real>:=", "<entero>", "<fraccion>", "<entero-sin-signo>", "<entero-con-signo>", "<digito>"]

text_string = input("Ingrese el digito a convertir a BNF: -> ")
num_text_string = float(text_string)

int_digits = []
decimal_digits = []
list_int_digits = lambda: ''.join(int_digits)
list_decimal_digits = lambda: ''.join(decimal_digits)

if '-' in text_string:
    if '.' in text_string:
        integer_value = int(num_text_string)
        decimal_part = str(num_text_string).split('.')[1] if '.' in str(num_text_string) else '0'
        decimal_value = str('.' + decimal_part)

        length_decimal_value = len(str(decimal_value).split('.')[1])

        if integer_value == 0:
            length_int_value = len(str(integer_value))
            print(N[0] + N[1] + N[2])
            print(N[0] + N[4] + N[2])
            print(N[0] + '-' + N[3] + N[2])
            
            for x in range(length_decimal_value):
                decimal_digits.append(N[5])

            print(N[0] + '-' + N[5] + N[2])
            print(N[0] + '-' + N[5] + '.' + N[3])
            print(N[0] + '-' + N[5] + '.' + list_decimal_digits())
            
        else:
            length_int_value = len(str(integer_value).split('-')[1])
            print(N[0] + N[1] + N[2])
            print(N[0] + N[4] + N[2])
            print(N[0] + '-' + N[3] + N[2])
            for x in range(length_int_value):
                int_digits.append(N[5])

            print(N[0] + '-' + list_int_digits() + N[2])
            print(N[0] + '-' + list_int_digits() + '.' + N[3])

            for x in range(length_decimal_value):
                decimal_digits.append(N[5])
            
            print(N[0] + '-' + list_int_digits() + '.' + list_decimal_digits())
    else:
        integer_value = int(num_text_string)
        length_int_value = len(str(integer_value).split('-')[1])

        print(N[0] + N[1])
        print(N[0] + N[4])
        print(N[0] + '-' + N[3])
        for x in range(length_int_value):
            int_digits.append(N[5])

        print(N[0] + '-' + list_int_digits())

else:
    if '.' in text_string:
        integer_value = int(num_text_string)
        decimal_part = str(num_text_string).split('.')[1] if '.' in str(num_text_string) else '0'
        decimal_value = str('.' + decimal_part)

        length_decimal_value = len(str(decimal_value).split('.')[1])

        if integer_value == 0:
            length_int_value = len(str(integer_value))
            print(N[0] + N[1] + N[2])
            print(N[0] + N[3] + N[2])
            
            for x in range(length_decimal_value):
                decimal_digits.append(N[5])

            print(N[0] + N[5] + N[2])
            print(N[0] + N[5] + '.' + N[3])
            print(N[0] + N[5] + '.' + list_decimal_digits())
        
        else:
            length_int_value = len(str(integer_value))
            print(N[0] + N[1] + N[2])
            print(N[0] + N[3] + N[2])
            for x in range(length_int_value):
                int_digits.append(N[5])
            
            print(N[0] + list_int_digits() + N[2])
            print(N[0] + list_int_digits() + '.' + N[3])

            for x in range(length_decimal_value):
                decimal_digits.append(N[5])

            print(N[0] + list_int_digits() + '.' + list_decimal_digits())
    
    else:
        integer_value = int(num_text_string)
        length_int_value = len(str(integer_value))

        print(N[0] + N[1])
        print(N[0] + N[3])
        for x in range(length_int_value):
            int_digits.append(N[5])

        print(N[0] + list_int_digits())    