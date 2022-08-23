"""
Problem 1: Leetcode 811
Description: We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, 
(in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.
"""
def subdomain_visits(cpdomains: List[str]) -> List[str]:

    visited_d = defaultdict(int)
    for line in cpdomains:
        times, domains = line.split(' ')
        domains = domains.split('.')
        for i in range(len(domains)-2, -1, -1):
            domains[i] = domains[i] + '.' + domains[i+1]
            
        for domain in domains:
            visited_d[domain] += int(times)
    
    return [str(val)+' '+key for key,val in visited_d.items()]

"""
Problem 2: Longest Common Continuous Subarray
Description: Output the longest common continues subarray of two users
"""
def LCS(user1, user2):
    # dp[i][j]: maximum length of user1[:i] and user2[:j]
    dp = [0] * (len(user2)+1)
    count = 0
    res = []
    for i in range(1, len(user1)+1):
        for j in range(1,len(user2)+1):
            if user1[i-1] == user2[j-1]:
                dp[j] = dp[j-1]+1
                if dp[j] > count:
                    count = dp[j]
                    res = user1[i-count: i]
    return res

"""
Problem3 : Ads Conversion Rate
Decription: check https://www.jianshu.com/p/fdbcba5fe5bc
"""
def ad_conversion_rate(completed_purchase_user_ids, ad_clicks, all_user_ips):
    ad2ip = defaultdict(list)
    ip2user = defaultdict(str)

    for ad_click in ad_clicks:
        ip, time, ad = ad_clicks.split(',')
        ad2ip[ad].append(ip)
    for all_user_ip in all_user_ips:
        user, ip = all_user_ip.split(',')
        ip2user[ip] = user
    
    ad2click = defaultdict(int)
    ad2buy = defaultdict(int)
    for key, val in ad2ip.items():
        ad2click[key] = len(val)
        for ip in val:
            if ip in ip2user:
                ad2buy[key] += 1
    return ad2buy, ad2click

"""
Problem 4: find the overlap of two students
"""
def find_overlap(student_course_pairs):
    course2student = defaultdict(list)
    for student, course in student_course_pairs:
        course2student[course].append(student)
    student2course = defaultdict(list)
    for key, val in course2student.items():
        for i in range(len(val)):
            for j in range(i+1, len(val)):
                student2course[(i,j)].append(val)
    return student2course

"""
Problem 5: find the halfway courses for each track
"""
def find_mid_courses(prereqs_courses):
    graph = defaultdict(list)
    degree = defaultdict(int)
    for src, tar in prereqs_courses:
        graph[src].append(tar)
        degree[tar] += 1
    q = deque([])
    for d in degree:
        if degree[d] == 0:
            q.append(d)
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for child in graph[node]:
            degree[child] -= 1
            if degree[child] == 0:
                q.append(child)
    if len(res) == len(prereqs_courses):
        return res[:len(prereqs_courses)//2]
    else:
        return []

"""
Problem 6: Find a Rectangle
Description: There is an image filled with 0s and 1s. There is at most one rectangle in this image filled with 0s, find the rectangle. 
Output could be the coordinates of top-left and bottom-right elements of the rectangle, or top-left element, width and height.
"""
def find_rectangle(image):
    res = []
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == 0:
                res.append((i,j))
                w, h = 0, 0
                while i+w < len(image) and image[i+w][j] == 0:
                    w += 1
                w -= 1
                while j+h < len(image[0]) and image[i+w][j+h] == 0:
                    h += 1
                h -= 1
                res.append((i+w, j+h))
                return res
    return []

"""
Problem 7: Find multiple rectangles
Description: for the same image, it is filled with 0s and 1s. It may have multiple rectangles filled with 0s. 
The rectangles are separated by 1s. Find all the rectangles.
"""
def find_multi_rectangle(image):
    res = []
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == 0:
                res.append((i,j))
                w, h = 0, 0
                while i+w < len(image) and image[i+w][j] == 0:
                    w += 1
                w -= 1
                while j+h < len(image[0]) and image[i+w][j+h] == 0:
                    h += 1
                h -= 1
                res.append((i+w, j+h))
                for ii in range(i,i+w+1):
                    for jj in range(j, j+h+1):
                        image[ii][jj]=2
    return res 

"""
Problem 8: Find all the shape
Description: the image has random shapes filled with 0s, 
separated by 1s. Find all the shapes. Each shape is represented by coordinates of all the elements inside.
"""
def find_shape(image):
    def dfs(i, j):
        path = ''
        image[i][j] = 1
        dirs = [(0,1,'r'),(0,-1,'l'),(1,0,'d'),(-1,0,'u')]
        for dx, dy, di in dirs:
            x = i + dx
            y = j + dy
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] = 0:
                path += di
                path += dfs(x, y)
                path += '.'
        return path
    res = set()
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == 0:
                path = dfs(i, j)
                res.add(path)
    return len(res)

"""
Problem 9: word wrap
Description: given a word list and maximum width, use '-' to connect them all.
"""
def word_wrap1(words, maxWidth):
    res = []
    i = 0
    while i < len(words):
        remain = maxWidth
        count = 0
        while i < len(words):
            if remain - len(words[i]) < 0:
                break
            count += 1
            remain = remain - len(words[i]) - 1
            i += 1
        res.append('-'.join(words[i-count:i]))
    return res

"""
Problem 10: follow up of problem 9
Description: Each line should have the exact specified width. If any line is too short, 
insert '-' (as stand-ins for spaces) between words as equally as possible until it fits.
"""
def word_wrap2(words, maxWidth):
    # decide how many words per line, how many space we need
    def get_interval(words):
        res = []
        i = 0
        while i < len(words):
            remain = maxWidth
            count = 0
            while i < len(words):
                if remain - len(words[i]) < 0:
                    break
                count += 1
                remain = remain - len(words[i]) - 1
                i += 1
            res.append((i,words[i-count:i]))
        return res
    
    def generate(idx, interval):
        l = ' '.join(interval)
        # check if there is only one word or the last word
        if len(interval) == 1 or idx == len(words):
            space = maxWidth - len(l)
            tmp = l + ' '*space
        else:
            space = maxWidth - len(l) + (len(interval)-1)
            s = space // (len(interval)-1)
            left = space%(len(interval)-1)
            if left > 0:
                tmp = (' '* (s + 1)).join(interval[:left])
                tmp += ' '* (s + 1)
                tmp += (' '* s).join(interval[left:])
            else:
                tmp = (' '* s).join(interval)
        return tmp

    res = []
    intervals = get_interval(words)
    for idx, interval in intervals:
        new = generate(idx, interval)
        res.append(new)
    return res

"""
Problem 11: calculator
Description: a string contain number, + and -.
"""
def calculator1(s):
    val = 0
    tmp = 0
    flag = 1
    for idx, string in enumerate(s):
        if string == '+':
            val += flag*tmp
            flag = 1
            tmp = 0
        elif string == '-':
            val += flag*tmp
            flag = -1
            tmp = 0
        else:
            tmp = tmp*10 + int(string)
    val += flag*tmp
    return val

"""
Problem 12: calculator with bracket
Description: follow up of problem 11.
"""
def calculator2(s):
    stack = []
    cur = 0
    tmp = 0
    flag = 1

    for i, string in enumerate(s):
        if string.isdigit():
            tmp = tmp*10 + int(string)
        elif string == '+':
            cur += flag * tmp
            tmp = 0
            flag = 1
        elif string == '-':
            cur += flag * tmp
            tmp = 0
            flag = -1
        elif string == '(':
            stack.append(cur)
            stack.append(flag)
            tmp = 0
            flag = 1
            cur = 0
        elif string == ')':
            cur += flag * tmp
            cur *= stack.pop()
            cur += stack.pop()
            tmp = 0
            flag = 1
    return flag*tmp + cur

"""
Problem 13: Valid Matrix
"""
def valid_matrix(matrix):
    for i in range(len(matrix)):
        tmp_set = set([matrix[i][j] for j in range(len(matrix[0]))])
        if len(tmp_set) != len(matrix[0]):
            return False
    for j in range(len(matrix[0])):
        tmp_set = set([matrix[i][j] for i in range(len(matrix))])
        if len(tmp_set) != len(matrix):
            return False
    return True

"""
Problem 14: Return node 
Description: Given an input, input[][], where input[0] is the parent of input[1], return those nodes with
only 0 or 1 parents
"""
def return_node(inputs):
    graph = defaultdict(list)
    for par, chi in inputs:
        graph[chi].append(par)
        graph[par] += []
    res = []
    for key, val in graph.items():
        if len(val) == 1 or len(val) == 0:
            res.append(key)
    return res

"""
Problem 15: Common Ancestor
Description: return whether two nodes have common ancestor
"""
def common_ancestor(inputs, p, q):
    graph = defaultdict(list)
    for par, chi in inputs:
        graph[chi].append(par)
        graph[par] += []
    seen = set()
    deq = deque([])
    deq.append(p)
    while deq:
        node = deq.popleft()
        seen.add(node)
        parents = graph[node]
        if len(parents) != 0:
            for parent in parents:
                deq.append(parent)
    deq2 = deque([])
    deq2.append(q)
    while deq2:
        node = deq2.popleft()
        if node in seen:
            return True
        parents = graph[node]
        if len(parents) != 0:
            for parent in parents:
                deq2.append(parent)
    return False

"""
Problem 16: Furthest common ancestor
"""
def furthest_common_ancestor(inputs, p, q):
    graph = defaultdict(list)
    for par, chi in inputs:
        graph[chi].append(par)
        graph[par] += []
    seen = set()
    deq = deque([])
    deq.append(p)
    while deq:
        node = deq.popleft()
        seen.add(node)
        parents = graph[node]
        if len(parents) != 0:
            for parent in parents:
                deq.append(parent)
    res = None
    deq2 = deque([])
    deq2.append(q)
    while deq2:
        node = deq2.popleft()
        if node in seen:
            res = node
        parents = graph[node]
        if len(parents) != 0:
            for parent in parents:
                deq2.append(parent)
    return res

"""
Problem 17: new meeting available
Description: given a list of meeting times, and a new meeting, determine the meeting can fit in those meeting times or not
"""
def spare_meeting(meetings, new_meeting):
    start, end = new_meeting
    for meeting in meetings:
        if (start >= meeting[0] and start < meeting[1]) or \
           (end <= meeting[1] and end > meeting[0]) or \
           (start < meeting[0] and end > meeting[1]):
           return False
    return True

"""
Problem 18: return all available time slot
"""
def spare_time(meetings):
    meetings = sorted(meetings, key=lambda x:x[0])
    res = []
    ref= meetings[0][1]
    res.append([0, meetings[0][0]])
    for i in range(1, len(meetings)):
        res.append([ref, meetings[i][0]])
        ref = meetings[i][1]
    return res

"""
Problem 19: Find legal move
"""
def legal_move(i, j, matrix):
    flag = True
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        x = i + dx
        y = j + dy
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            if matrix[x][y] == 0:
                flag = flag and True
            else:
                return False
    return flag

"""
Problem 20: find all reachable 0
"""
def find_reachable(matrix):
    def dfs(i, j):
        matrix[i][j] = -1
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            x = i + dx 
            y = j + dy
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 0:
                dfs(x, y)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                dfs(i, j)
                break

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return False
    return True

"""
Problem 21: find shortest path
Description: find all shortest path to grab all treasure (label as 1)
"""
def find_shortest(matrix, src, target):
    def dfs(i, j, path, count):
        if (i,j) == target and count == total:
            res.append(path)
            return
        if matrix[i][j] == 1:
            count += 1
        tmp = matrix[i][j] 
        matrix[i][j] = 2
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            x = i + dx 
            y = j + dy
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and (matrix[x][y] == 0 or matrix[x][y] == 1):
                dfs(x, y, path+[(x,y)], count)
        matrix[i][j] = tmp

    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                total += 1
    res = []
    dfs(src[0], src[1], [src], 0)
    min_len = float('inf')
    for r in res:
        min_len = min(min_len, len(r))
    output = []
    for x in res:
        if len(x) == min_len:
            output.append(x)
    return output