def the_fastest_sorting_algorithm_in_the_world(case_list):
    for case_num, case in enumerate(case_list):
        print(f"Case {case_num + 1}: Sorting... done!")
        

if __name__ == "__main__":
    case_list = []
    
    while True:
        case = input()
        
        if case == "0":
            break
        
        case_list.append(list(map(int, case.split())))
        
    the_fastest_sorting_algorithm_in_the_world(case_list=case_list)