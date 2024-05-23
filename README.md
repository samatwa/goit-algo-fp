# goit-algo-fp
 
# Висновки щодо правильності розрахунків
Метод Монте-Карло є потужним інструментом для моделювання ймовірностей шляхом імітації випадкових процесів. У даному випадку ми використовували цей метод для визначення ймовірностей випадання сум чисел при киданні двох шестигранних кубиків.

## Порівняння результатів
Результати розрахунків за методом Монте-Карло та аналітичні розрахунки наведено нижче:

**Monte Carlo probabilities**:\
Sum	Probability\
2	0.0278\
3	0.0552\
4	0.0832\
5	0.1113\
6	0.1388\
7	0.1672\
8	0.1392\
9	0.1111\
10	0.0837\
11	0.0550\
12	0.0276\

**Analytical probabilities**:
Sum	Probability
2	0.0278
3	0.0556
4	0.0833
5	0.1111
6	0.1389
7	0.1667
8	0.1389
9	0.1111
10	0.0833
11	0.0556
12	0.0278

1. **Малий відсоток відхилення:** Отримані за допомогою методу Монте-Карло ймовірності дуже близькі до аналітичних значень. Відхилення в більшості випадків становлять лише тисячні долі.

2. **Точність:** Метод Монте-Карло підтвердив свою здатність надавати точні результати при великій кількості симуляцій (1,000,000).

3. **Практична користь:** Метод Монте-Карло є ефективним інструментом для задач, де аналітичні розрахунки можуть бути складними або неможливими.

## Висновки
Результати методу Монте-Карло практично збігаються з аналітичними розрахунками, що підтверджує правильність розрахунків та ефективність методу. Невеликі відхилення можна пояснити випадковим характером симуляцій та обмеженнями точності обчислень. Метод Монте-Карло підтвердив свою здатність надавати точні результати при великій кількості симуляцій. Він є корисним інструментом для задач, де аналітичні розрахунки можуть бути складними або неможливими.