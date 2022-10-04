def arithmetic_arranger(problems, results = False):
    error = problem_checker(problems)
    if len(error) > 0:
        return error
    
    # There should be a single space between the operator and the longest of the two operands, 
    # the operator will be on the same line as the second operand, 
    # both operands will be in the same order as provided 
    # (the first will be the top one and the second will be the bottom).
    # Numbers should be right-aligned.
    # There should be four spaces between each problem.
    # There should be dashes at the bottom of each problem. 
    # The dashes should run along the entire length of each problem individually. 
    # (The example above shows what this should look like.)
    
    # Save on strings each complete line
    line1 = ""
    line2 = ""
    line3 = ""
    arranged_problems = ""
    spaces_btw_problems = ' ' * 4

    for problem in problems:
        # Split the input
        problem = problem.split()

        # Save the lenghts of the inputs
        len_op1 = len(problem[0])
        len_op2 = len(problem[2])

        # Check spaces to add to the shortest operator
        #spaces = len(problem[0]) - len(problem[2])
        #if spaces < 0:
        #    spaces = spaces * -1

        if len_op1 > len_op2:
            line1 = line1 + (' ' * 2) + problem[0] + spaces_btw_problems
            line2 = line2 + problem[1] + ' ' + (' ' * (len_op1 - len_op2)) + problem[2] + spaces_btw_problems
            line3 = ('-' * (len_op1 + 2)) + spaces_btw_problems
        elif len_op2 > len_op1:
            line1 = line1 + (' ' * 2) + (' ' * (len_op2 - len_op1)) + problem[0] + spaces_btw_problems
            line2 = line2 + problem[1] + ' ' + problem[2] + spaces_btw_problems
            line3 = ('-' * (len_op2 + 2)) + spaces_btw_problems
        else:
            line1 = line1 + (' ' * 2) + problem[0] + spaces_btw_problems
            line2 = line2 + problem[1] + ' ' + problem[2] + spaces_btw_problems
            line3 = ('-' * (len_op2 + 2)) + spaces_btw_problems

    arranged_problems = line1 + "\n" + line2 + "\n" + line3

    return arranged_problems

def problem_checker(problems):
    message = ""
    # If there are too many problems supplied to the function. 
    # The limit is five, anything more will return: Error: Too many problems.
    if len(problems) > 5:
        message = "Error: Too many problems."
        return message

    for problem in problems:
        problem = problem.split()

        # Each number (operand) should only contain digits. 
        # Otherwise, the function will return: 
        # Error: Numbers must only contain digits.
        try:
            val1 = int(problem[0])
            val2 = int(problem[2])
        except:
            message = "Error: Numbers must only contain digits."
            return message

        # Extra: Check the number of operators

        # The appropriate operators the function will accept are addition and subtraction. 
        # Multiplication and division will return an error. 
        # Other operators not mentioned in this bullet point will not need to be tested. 
        # The error returned will be: Error: Operator must be '+' or '-'.
        if ('+' not in problem) and ('-' not in problem):
            message = "Error: Operator must be '+' or '-'."  
            return message 

        # Each operand (aka number on each side of the operator) has a max of four digits in width. 
        # Otherwise, the error string returned will be: 
        # Error: Numbers cannot be more than four digits.
        if (len(problem[0]) > 4) or (len(problem[2]) > 4):
            message = "Error: Numbers cannot be more than four digits."  
            return message
        
        # print(problem)
    
    return message