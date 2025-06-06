# ap_p2_labs_iot_nulp

## Лабораторні роботи з дисципліни "Алгоритмізація та програмування, ч. 2"

## Виконав: Шийка Андрій Васильович (ІР-14) (В-3)
## Рівень 1

### Варіант 1

Реалізуйте структуру даних "черга з пріоритетами" на основі  двозв'язаного списку, в якому кожен елемент має значення та пріоритет в  списку і додається в список, впорядкований за пріоритетами.

Кожен елемент черги має відноситися до певного пріоритету. Елементи з більшим пріоритетом мають бути доступні в чергу раніше, ніж елементи з меншим пріоритетом. Якщо у двох елементів однаковий пріоритет, то вони вставляються у порядку їх додавання.

Операції, які підтримує ваша черга:

1. Вставка елемента з заданим значенням та пріоритетом до черги.
2. Видалення та повернення елемента з найвищим пріоритетом з черги.
3. Перегляд черги без її зміни.

Для реалізації такої черги з пріоритетами можна використати двозв'язаний список, де кожен елемент буде мати два поля: значення та пріоритет. При вставці елемента до черги, його потрібно розмістити у відповідному порядку з урахуванням пріоритету. При видаленні елемента з найвищим пріоритетом, просто видаляємо перший елемент зі списку.

Реалізація цієї задачі передбачає написання власної структури "двозв'язаний список". Назва файлу реалізації - `list_based_priority_queue.py`

## Рівень 2
### Варіант 2

Реалізуйте структуру даних "черга з пріоритетами" на основі  бінарного дерева  `binary tree`, в якому  батьківський елемент має вищий пріоритет, ніж елемент справа, або нижчий або рівний пріоритет, ніж пріоритет його лівої дитини.

Операції, які підтримує ваша черга:

1. Вставка елемента з заданим значенням та пріоритетом до черги.
2. Видалення та повернення елемента з найвищим пріоритетом з черги.
3. Перегляд черги без її зміни.

Для реалізації такої черги з пріоритетами слід використати окремий клас `Node`, де кожен елемент буде мати два поля: значення та пріоритет. При вставці елемента до черги, його потрібно розмістити у відповідному порядку з урахуванням пріоритету.

Назва файлу реалізації - `binary_tree_priority_queue.py`

## Рівень 3
### Варіант 2

Реалізуйте структуру даних "черга з пріоритетами" на основі  AVL-дерева, в якому  батьківський елемент має вищий пріоритет, ніж елемент справа, або нижчий або рівний пріоритет, ніж пріоритет його лівої дитини.

Операції, які підтримує ваша черга:

1. Вставка елемента з заданим значенням та пріоритетом до черги.
2. Видалення та повернення елемента з найвищим пріоритетом з черги.
3. Перегляд черги без її зміни.

Для реалізації такої черги з пріоритетами слід використати окремий клас `Node`, де кожен елемент буде мати два поля: значення та пріоритет. При вставці елемента до черги, його потрібно розмістити у відповідному порядку з урахуванням пріоритету.
