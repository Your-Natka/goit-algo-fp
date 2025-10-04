from linked_list import LinkedList
from reverse import reverse_linked_list
from sort import insertion_sort
from merge import merge_sorted_lists

# Створюємо список
ll = LinkedList()
for val in [5, 3, 8, 1, 2]:
    ll.append(val)

print("Початковий список:", ll)

# Реверсування
reversed_ll = reverse_linked_list(ll)
print("Реверсований список:", reversed_ll)

# Сортування
sorted_ll = insertion_sort(reversed_ll)
print("Відсортований список:", sorted_ll)

# Другий список для злиття
ll2 = LinkedList()
for val in [0, 4, 9]:
    ll2.append(val)

print("Другий список:", ll2)

# Злиття
merged_ll = merge_sorted_lists(sorted_ll, ll2)
print("Злитий відсортований список:", merged_ll)