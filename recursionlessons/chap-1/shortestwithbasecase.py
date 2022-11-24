def shortest_with_base_case(make_recursive_call):
    print("shortest_with_base_case(%s) called." % make_recursive_call)

    if not make_recursive_call:
        print("Returning from base case")
        return
    else:
        shortest_with_base_case(False)
        print("Return from recursive case")
        return


#   ===============================================

if __name__ == '__main__':

    print("Calling shortest_with_base_case(False):")
    shortest_with_base_case(False)
    print()
    print("Calling shortest_with_base_case(True):")
    shortest_with_base_case(True)
