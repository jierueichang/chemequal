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
    '''coefficients_left = []
    for i in eq1:
        coefficients_left.append(i[0])
    coefficients_right = []
    for i in eq2:
        coefficients_right.append(i[1])'''
    quantities_left = {}
    for i in range(len(eq1)):
        coefficient = int(str(iteration_count)[i])
        print(coefficient)
        quantities = calculate_quantity(eq1[i],coefficient)
        for j in quantities:
            try:
                quantities_left[j] += quantities[j]
            except:
                quantities_left[j] = quantities[j]
    print(quantities_left)
    quantities_right = {}
    for i in range(len(eq2)):
        coefficient = int(str(iteration_count)[i+len(eq1)])
        print(coefficient)
        quantities = calculate_quantity(eq2[i],coefficient)
        for j in quantities:
            try:
                quantities_right[j] += quantities[j]
            except:
                quantities_right[j] = quantities[j]
    print(quantities_right)
    if quantities_left == quantities_right:
        return True
    return False

# Parse subscripts

def parse_subscripts(eq):
    res = []
    for i in eq:
        subscripted = re.findall('[A-Z]._\d|[A-Z]_\d',i)
        print(subscripted)
        for j in range(len(subscripted)):
            element_name = subscripted[j].split('_')[0]
            print(element_name)
            subscript = int(subscripted[j][subscripted[j].find('_')+1])
            subscripted[j] = [subscripted[j].replace(l,element_name*(subscript-1)) for l in re.findall('_\d',subscripted[j])][0]
            print(subscripted[j])
        k = re.findall('[A-Z]._\d|[A-Z]_\d',i)
        for j in range(len(subscripted)):
            i = i.replace(k[j],subscripted[j])
        res.append(i)
    return res

# Render final result

def render(i,eq1,eq2):
    res = ''
    for j in range(len(eq1)):
        if str(i)[j] != '1':
            res+=str(i)[j]
        res+=eq1[j]
        if j!=len(eq1)-1:
            res+='+'
    res+='->'
    for j in range(len(eq2)):
        if str(i)[j+len(eq1)] != '1':
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
        print(j)
    else:
        return 'Cannot balance equation. Make sure your inputs are correct, then try again.'
    print(j)
    return render(j,raw_eq1,raw_eq2)

def main():
    # Obtain sides of equation
    try:
        eq1 = input('eq1: ')
        eq2 = input('eq2: ')
    # 2/3 compatibility
    except:
        eq1 = raw_input('eq1: ')
        eq2 = raw_input('eq2: ')

    run(eq1,eq2)

if __name__ == '__main__':
    main()
