class Node:
    pass


# 1. Добавление в начало
def add_to_beginning(head, data):
    new_node = Node()
    new_node.data = data
    new_node.next = head
    return new_node


# 2. Добавление в конец
def add_to_end(head, data):
    new_node = Node()
    new_node.data = data
    new_node.next = None

    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head


# 3. Удаление последнего элемента
def remove_last(head):
    if head is None:
        return None

    if head.next is None:
        return None

    current = head
    while current.next.next:
        current = current.next

    current.next = None
    return head


# 4. Вывод списка
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# 5. Поиск элемента
def search(head, target):
    current = head
    index = 0

    while current:
        if current.data == target:
            return index
        current = current.next
        index += 1

    return -1


# 6. Вставка по позиции
def insert_at_position(head, data, position):
    new_node = Node()
    new_node.data = data

    if position == 0:
        new_node.next = head
        return new_node

    current = head

    for _ in range(position - 1):
        if current is None:
            print("Ошибка: позиция вне диапазона")
            return head
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


# 7. Удаление по значению
def remove_by_value(head, value):
    if head is None:
        return None

    if head.data == value:
        return head.next

    current = head

    while current.next:
        if current.next.data == value:
            current.next = current.next.next
            return head
        current = current.next

    return head


# 8. Объединение двух списков
def merge_lists(head1, head2):
    if head1 is None:
        return head2

    current = head1
    while current.next:
        current = current.next

    current.next = head2
    return head1


# 9. Разворот списка
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# 10. Сортировка (простая)
def sort_list(head):
    if head is None:
        return None

    current = head

    while current:
        next_node = current.next
        temp = head

        while temp != current:
            if temp.data > current.data:
                temp.data, current.data = current.data, temp.data
            temp = temp.next

        current = next_node

    return head

