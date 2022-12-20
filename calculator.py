class Calculator():

    def __init__(self):
        self.numbers = list("0123456789")
        self.special_chars = "*,**,/,//,^,+,-,%".split(",")

    def ans_equ(self, equ):
        try:
            pre_notation = self.split_equation(equ)
            ans = self.solve_equation(pre_notation)
            print(ans)
        except:
            print("Invalid equation")

    def join_numbers(self, equ):
        r_list = []
        last_num = False
        for char in equ:
            if not char in self.numbers:
                r_list.append(char)
                last_num = False
            else:
                if last_num:
                    r_list[-1] += char
                else:
                    r_list.append(char)
                last_num = True
        
        return r_list

    def get_pow(self, char):
        if char in ["^"]:
            rv = 3
        elif char in ["*", "/", "//", "%"]:
            rv = 2
        elif char in ["+", "-"]:
            rv = 1

        return rv
        

    def split_equation(self, equ):
        # Split equation into a list of functions to do

        equ = "".join(equ.split(" ")) # Remove spaces
        equ = "^".join(equ.split("**"))
        # add handling for multiplication of brackets e.g 2(5-1)
        # add // and ** and --
        # Replace ** with ^
        
        equ = list(equ)
        equ_list = self.join_numbers(equ)

        for index in range(len(equ_list)):
            if equ_list[index] == "(":
               equ_list[index] = ")"
            elif equ_list[index] == ")":
                equ_list[index] = "("   

        index = 0
        while index < len(equ):
            char = equ[index]
            index += 1

        stack = []
        output = []
        for char in list(reversed(equ_list)):
            if char in self.special_chars:
                if stack == [] or stack[-1] == "(":
                    stack.append(char)
                else:
                    stack_pow = self.get_pow(stack[-1])
                    char_pow = self.get_pow(char)

                    if stack_pow <= char_pow:
                        stack.append(char)
                    else:
                        output.append(stack[-1])
                        stack.pop()
                        stack.append(char)
                        
            elif char in ["("]:
                stack.append(char)
            elif char in [")"]:
                last_bracket = len(stack) - list(reversed(stack)).index("(")
                output += list(reversed(stack[last_bracket:])) # Add everthing in bracket to stack
                stack = stack[:last_bracket - 1] # remove everthing in bracket from stack
                
            else:
                output.append(char)
                
        output += list(reversed(stack)) # Add remaining operators)
        output = list(reversed(output)) # reverse the stack again
            
        return output

        

    def solve_equation(self, prefix):
        stack = []
        prefix = list(reversed(prefix))
        for char in prefix:
            if char in self.special_chars:
                num1 = int(stack[-1])
                num2 = int(stack[-2])
                if char in ["^", "**"]: new_num = num1 ** num2
                elif char == '*': new_num = num1 * num2
                elif char == '/': new_num = num1 / num2
                elif char == '//': new_num = num1 // num2
                elif char == '%': new_num = num1 % num2
                elif char == '+': new_num = num1 + num2
                elif char == '-': new_num = num1 - num2
                stack = stack[:-2] + [new_num]
            else:
                stack.append(char)

        return stack[0]
                


calc = Calculator()

# calc.split_equation("(15+2)-(3+46)")

while True:
    ans = input(">>> ")
    calc.ans_equ(ans)
