#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(list_length):
        result = 0
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            
            # Check for non-numeric types before division
            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                print("wrong type")
                result = 0
            else:
                result = val1 / val2
                
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            # Catch TypeError if one of the elements is non-numeric 
            # and was not caught by the explicit isinstance check 
            # (e.g., if one list contained a list/dict that failed simple division check).
            # This is defensive, though the `isinstance` check should cover most cases.
            print("wrong type")
        finally:
            new_list.append(result)
            
    return new_list
