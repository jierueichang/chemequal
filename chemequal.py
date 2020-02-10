import re
# I (sort of) know regular expressions!

# Calculate number of each element

def calculate_quantity(eq,multiplier=1):
    splitted = re.findall('[A-Z][^A-Z]*', eq)
    element_dict = {}
    for i in splitted:
        try:
            element_dict[i] += multiplier
        except:
            element_dict[i] = multiplier
    return element_dict

# Find if the equation is balanced

def find_balanced(iteration_count,eq1,eq2):
    quantities_left = {}
    for i in range(len(eq1)):
        coefficient = int(str(iteration_count)[i])
        quantities = calculate_quantity(eq1[i],coefficient)
        for j in quantities:
            try:
                quantities_left[j] += quantities[j]
            except:
                quantities_left[j] = quantities[j]
    quantities_right = {}
    for i in range(len(eq2)):
        coefficient = int(str(iteration_count)[i+len(eq1)])
        quantities = calculate_quantity(eq2[i],coefficient)
        for j in quantities:
            try:
                quantities_right[j] += quantities[j]
            except:
                quantities_right[j] = quantities[j]
    if quantities_left == quantities_right:
        return True
    return False

# Parse subscripts

def parse_subscripts(eq):
    res = []
    for term in eq:
        parsed_term = ''
        elements = re.findall('([A-Z][a-z]*)([2-9]*)',term)
        for element in elements:
            if element[1].isnumeric():
                parsed_term+=element[0]*int(element[1])
            else:
                parsed_term+=element[0]
        res.append(parsed_term)
    return res

# Render final result

def render(i,eq1,eq2,colortags=False):
    res = ''
    for j in range(len(eq1)):
        if str(i)[j] != '1':
            if colortags:
                res+='<div style="color:rgb(39, 162, 211);">'+str(i)[j]+'</div>'
            else:
                res+=str(i)[j]
        res+=eq1[j]
        if j!=len(eq1)-1:
            res+='+'
    res+='->'
    for j in range(len(eq2)):
        if str(i)[j+len(eq1)] != '1':
            if colortags:
                res+='<div style="color:rgb(39, 162, 211);">'+str(i)[j+len(eq1)]+'</div>'
            else:
                res+=str(i)[j]
        else:
            res+=str(i)[j+len(eq1)]
        res+=eq2[j]
        if j!=len(eq2)-1:
            res+='+'
    print(res)
    return res

def run(eq1,eq2):
    # Split equation
    eq1 = eq1.split('+')
    eq2 = eq2.split('+')

    # Brute force
    raw_eq1 = eq1
    raw_eq2 = eq2

    eq1 = parse_subscripts(eq1)
    eq2 = parse_subscripts(eq2)

    iteration_count = int('9'*(len(eq1) + len(eq2)))
    for j in range(int('1'*(len(eq1)+len(eq2))),iteration_count):
        if find_balanced(j,eq1,eq2):
            break
    else:
        return 'Cannot balance equation. Make sure your inputs are correct, then try again.'
    return render(j,raw_eq1,raw_eq2,colortags=True)

def main():
    # Obtain sides of equation
    eq1 = input('eq1: ')
    eq2 = input('eq2: ')

    run(eq1,eq2)

if __name__ == '__main__':
    main()
