def solution(s):
    images = ["png", "jpeg", "gif"]
    lines = s.strip().split('\n')
    max_length = 0
    cur_length = 0
    cur_indent = 0
    stack = [len(lines[0])]
    cur_length += stack[0] + 1
    for line in lines[1:]:
        # stack.append()
        print cur_length
        line_indent = line.count(' ')
        if line_indent - cur_indent == 1 and '.' not in line:
            stack.append(len(line.strip()))
            cur_length += stack[-1] + 1
            cur_indent += 1
        elif '.' in line and line.split('.')[-1] in images:
            max_length = max(max_length, cur_length + len(line.strip()))
            cur_indent = line_indent
        elif line_indent == cur_indent:
            if '.' in line:
                pass
            else:
                cur_length -= stack.pop() + 1
                stack.append(len(line.strip()))
                cur_length += stack[-1] + 1
        elif line_indent < cur_indent:
            for i in range(line_indent - cur_indent):
                cur_length -= stack.pop() + 1

    print max_length

s = \
'''dir1
 dir11
  xxx.png
 dir12
  dir120
  picture.jpeg
  dir121
  file1.txt
 fiddddddddle3.png
dir2
 file2.gif
'''
print s.split('\n')
solution(s)




def solution2(n):
    digits = list(str(n))
    nums = len(digits)
    max_value = 0
    index = 0
    for i in digits[1:]:
        if i < digits[index]:
            break
        else:
            index += 1
    digits.insert(index, digits[index])
    print "".join(digits)

solution2(212231325511)