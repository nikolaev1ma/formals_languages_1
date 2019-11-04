class RegularMachine:
    def __init__(self, regular_expression_):
        self.node_arr = []  # элемент массивах[i] это dict из буквы и соответсвующего массива других node,
                            # что есть переход из i в элемент массива по данной букве
        self.regular_expression = regular_expression_  # входная строка - регулярное выражение
        self.stack = []     # стек, где элемент стека это поддерево, которое потом будет соеденено с другим поддеревом
                            # элемент стека это начальное состояние и массив заершающих состояний текущего подграфа

    def make_graph(self):
        for letter in list(self.regular_expression):
            if letter == 'a' or letter == 'b' or letter == 'c':
                # создаем новый подграф и кидаем на стек
                self.make_new_temp_graph(letter)
            elif letter == '.':
                # выкидываем со стека 2 последних подграфов и добавляем новый обработанный подграф в стек
                graph2 = self.pop_with_check()
                graph1 = self.pop_with_check()
                self.composition_temp_graph(graph1, graph2)
            elif letter == '+':
                # выкидываем со стека 2 последних подграфов и добавляем новый обработанный подграф в стек
                graph1 = self.pop_with_check()
                graph2 = self.pop_with_check()
                self.plus_temp_graph(graph1, graph2)
            elif letter == '*':
                # выкидываем со стека последний подграф и добавляем новый обработанный подграф в стек
                graph = self.pop_with_check()
                self.exponentiation_temp_graph(graph)
            elif letter == '1':
                # создаем пустой подграф
                self.make_empty_new_temp_graph()
            else:
                # плохая буква
                raise Exception("Haven't got this letter")
        if len(self.stack) != 1:
            # в конце должен остаться ровно 1 связный граф
            raise Exception("Wrong polish entry")
        self.reverse_graph()

    # создаем новый подграф из 2 вершин
    def make_new_temp_graph(self, letter):
        node_arr_size = len(self.node_arr)
        self.node_arr.append({letter: [node_arr_size + 1], 'e': []})
        self.node_arr.append({'e': []})
        self.stack.append([node_arr_size, [node_arr_size + 1]])

    # соединяем два подграфа,
    # для этого проводим пустые ребра из всех завершающих одного подграфа, в начальное состояние другого графа
    def composition_temp_graph(self, graph1, graph2):
        for terminal in graph1[1]:
            self.node_arr[terminal]['e'].append(graph2[0])
        self.stack.append([graph1[0], graph2[1]])

    # реализуем сложение
    # для этого добавим новую вершину и проведем пустое ребро из нее в оба начальных состояния двух подграфов
    def plus_temp_graph(self, graph1, graph2):
        node_arr_size = len(self.node_arr)
        self.node_arr.append({'e': [graph1[0], graph2[0]]})
        self.stack.append([node_arr_size, graph1[1] + graph2[1]])

    # реализуем "зацикливание"
    # для этого создаем новую вершину и проводим пустое ребро из нее в начальное состояние подграфа
    # и проводим в нее пустые ребра из завершающих состояний в нее
    def exponentiation_temp_graph(self, graph):
        node_arr_size = len(self.node_arr)
        self.node_arr.append({'e': [graph[0]]})
        for terminal in graph[1]:
            self.node_arr[terminal]['e'].append(node_arr_size)
        self.stack.append([node_arr_size, [node_arr_size]])

    # создается просто одна вершина
    def make_empty_new_temp_graph(self):
        node_arr_size = len(self.node_arr)
        self.node_arr.append({'e': []})
        self.stack.append([node_arr_size, [node_arr_size]])

    def pop_with_check(self):
        if (len(self.stack)):
            return self.stack.pop()
        else:
            raise Exception("Wrong polish entry")

    #разворачиваем все ребра
    def reverse_graph(self):
        tmp_node_arr = []
        for i in self.node_arr:
            tmp_node_arr.append({'a': [], 'b': [], 'c': [], 'e': []})
        for i in range(len(self.node_arr)):
            for letter in self.node_arr[i].keys():
                for child in self.node_arr[i][letter]:
                    tmp_node_arr[child][letter].append(i)
        self.node_arr = tmp_node_arr
