def arithmetic_arranger(problems):
    if len(problems) > 5:
        return 'Error: Too many problems.'
        exit()
    arranged_problems = ''
    first_elements = []
    operators = []
    second_elements = []
    lens = []
    results = []
    for problem in problems:
        if problem.find('-') == -1 and problem.find('+') == -1:
            return "Error: Operator must be '+' or '-'"
            exit()
        elif problem.find('-') != -1:
            first_elements.append(problem.split(' - ')[0])
            operators.append('-')
            second_elements.append(problem.split(' - ')[1])
            lens.append(len(problem.split(' - ')[0]) if problem.split(' - ')[0] > problem.split(' - ')[1] else problem.split(' - ')[0])
        else:
            first_elements.append(problem.split(' + ')[0])
            operators.append('+')
            second_elements.append(problem.split(' + ')[1])
            lens.append(len(problem.split(' + ')[0]) if problem.split(' + ')[0] > problem.split(' + ')[1] else problem.split(' + ')[0])
    print(first_elements,second_elements,lens,results,arranged_problems)
    for i in len(first_elements):
        arranged_problems += 2 *' ' if len(first_elements[i]) == lens[i] else (2 + (lens[i] - len(first_elements[i])))*' '
        arranged_problems += first_elements[i]
    arranged_problems += '\n'
    for i in len(second_elements):
        arranged_problems += operators[i]
        arranged_problems += 1*' ' if len(second_elements[i]) == lens[i] else(1 + (lens[i] - len(second_elements[i])))*' '
        arranged_problems += second_elements[i] 
    arranged_problems += '\n'
    for item in lens:
        arranged_problems += (2 + item) * '_'
    try: 
        first_elements,second_elements = [int(x) for x in first_elements], [int(x) for x in second_elements] 
    except:
        return 'Error: Numbers must only contain digits.'
        exit()
    return arranged_problems

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))