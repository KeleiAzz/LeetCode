def solution(s):
    images = ["png", "jpeg", "gif"]
    lines = s.strip().split('\n')
    cur_indent = 0
    stack = [lines[0]]
    paths = []
    for line in lines[1:]:
        line_indent = line.count(' ')
        if line_indent - cur_indent == 1:
            if '.' in line and line.strip().split('.')[-1] in images:
                paths.append("/" + "/".join(stack))
            elif '.' not in line:
                stack.append(line.strip())
            # cur_length += stack[-1] + 1
            cur_indent += 1
            # new_dir = 1
        elif line_indent == cur_indent:
            if '.' in line and line.strip().split('.')[-1] in images:
                if line_indent < len(stack):
                    stack.pop()
                cur_path = "/" + "/".join(stack)
                paths.append(cur_path)
            elif '.' not in line:
                # cur_length -= stack.pop() + 1
                if line_indent < len(stack):
                    stack.pop()
                stack.append(line.strip())
                # cur_length += stack[-1] + 1
                # new_dir = 1
        elif line_indent < cur_indent:
            # print line, line_indent, cur_indent
            for i in range(cur_indent - line_indent):
                print stack.pop()

            if '.' in line and line.strip().split('.')[-1] in images:
                cur_path = "/" + "/".join(stack)

                paths.append(cur_path)
            elif '.' not in line:
                stack.append(line.strip())
            cur_indent = line_indent
            # new_dir = 1
        print line, stack
    print set(paths)


def solution1(s):
    images = ["png", "jpeg", "gif"]
    lines = s.strip().split('\n')
    cur_indent = 0
    stack = [lines[0]]
    paths = []
    for line in lines[1:]:
        line_indent = line.count(' ')
        if line_indent - cur_indent == 1:
            if '.' in line and line.strip().split('.')[-1] in images:
                paths.append("/" + "/".join(stack))
            elif '.' not in line:
                stack.append(line.strip())
            cur_indent += 1
        else:
            while len(stack) > line_indent:
                stack.pop()
            if '.' in line and line.strip().split('.')[-1] in images:
                cur_path = "/" + "/".join(stack)
                paths.append(cur_path)
            elif '.' not in line:
                stack.append(line.strip())
            cur_indent = line_indent
    print set(paths)

s = \
'''dir1
 dir11
  xxx.png
 dir12
  dir120
  picture.jpeg
  dir121
   adfasdf.png
  ppp.png
  file1.txt
dir2
 file2.gif
'''
print s.split('\n')
solution(s)
solution1(s)
def solution2(n):
    digits = list(str(n))
    removable = 0
    previous = digits[0]
    remove = -1
    for i in range(1, len(digits)):
        if digits[i] == previous:
            removable = 1
            continue
        elif removable == 1 and digits[i] > previous:
            remove = i - 1
            # print i
            break
        elif digits[i] != previous:
            removable = 0
            previous = digits[i]

    # print remove
    digits.pop(remove)
    return int(''.join(digits))

def solution22(n):
    digits = list(str(n))
    max_res = 0
    removable = 0
    previous = digits[0]
    for i in range(1, len(digits)):
        if digits[i] == previous:
            print int(''.join(digits[:i] + digits[i+1:]))
            max_res = max(max_res, int(''.join(digits[:i] + digits[i+1:])))
            # print max_res
        else:
            previous = digits[i]
    return max_res

print solution2(33223336226) == solution22(33223336226)