from RegularMachine import RegularMachine


def dfs(node_arr, letter, node, visit, next_cur_arr):
    visit[node] = True
    for child in node_arr[node][letter]:
        if next_cur_arr.count(child) == 0:
            next_cur_arr.append(child)
    for child in node_arr[node]['e']:
        if not visit[child]:
            dfs(node_arr, letter, child, visit, next_cur_arr)


def longest_suffix(regular_machine_str, pattern):
    regular_machine = RegularMachine(regular_machine_str) # создаем автомат
    regular_machine.make_graph() # строим автомат
    current_node_arr = regular_machine.stack[0][1]  # массив текущих состояний node
    pattern = pattern[::-1]
    max_suffix_len = 0
    for letter in pattern:
        if letter != 'a' and letter != 'b' and letter != 'c':
            raise Exception("u haven't got this letter")
        visit = []
        for node in regular_machine.node_arr:
            visit.append(False)
        tmp_current_node_arr = []
        for node in current_node_arr:
            dfs(regular_machine.node_arr, letter, node, visit, tmp_current_node_arr)
        current_node_arr = tmp_current_node_arr
        if len(current_node_arr) == 0:
            return max_suffix_len
        max_suffix_len += 1
    return max_suffix_len
