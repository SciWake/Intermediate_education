## Тренировки по ML. Лекция 1: Вводная по ML + knn


### Дополнительные материалы:

[Слайды](./lecture01_intro_knn_naive_bayes.pdf)

Доп. материалы:
* [Краткий ликбез по numpy и Python от комаднды из Stanford'а](https://cs231n.github.io/python-numpy-tutorial/)
* [Отличный учебник/хендбук по Python от Яндекса](https://academy.yandex.ru/handbook/python)
 * [EN] [Обсуждение разницы между Правдоподобием и Вероятностью (Likelihood и Probability) на StackExchange](https://stats.stackexchange.com/questions/2641/what-is-the-difference-between-likelihood-and-probability)
 * Серия видеоуроков от 3blue1brown по основным моментам в мат. анализе: [на английском (оригинал)](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr), [на русском](https://www.youtube.com/watch?v=qd0rzmSGPWg&list=PLVjLpKXnAGLVbrcJdDb0a2RS6MmRCgxJz&pp=iAQB)
 * Серия видео от 3blue1brown о центральной предельной теореме: [на английском (оригинал)](https://www.youtube.com/playlist?list=PLZHQObOWTQDOMxJDswBaLu8xBMKxSTvg8)
 * Видео о теореме Байеса от 3blue1brown: [один](https://www.youtube.com/watch?v=HZGCoVF3YvM), [два](https://www.youtube.com/watch?v=lG4VkPoG3ko), [три](https://www.youtube.com/watch?v=U_85TaXbeIo)


### Список To Do:
1. ndependent and Identically Distributed (независимые и одинаково распределённые данные) 
    - Когда данные не i.i.d? Как работать с такими данными?
2. Почитать Манхэттенская и Евклидова норма в линейной алгебре
3. Почитать про Функционал эмперического риска
4. Математическое отображение

### Список To Do KNN:
1. Реализовать полноценный вариант KNeighborsRegressor/Classifier
2. Реализовать разные варианты расчёта весов для KNeighborsRegressor/Classifier
    * Обратная пропорциональность
    * Экспоненциальное затухание
    * Какие варинты ещё есть?
    * Подбор весов брудфорсом
    * Метод градиентного спуска
3. Реализовать RadiusNeighborsRegressor/Classifier
4. Сравниь разные реализации на разных задачах
    * https://scikit-learn.org/stable/modules/neighbors.html#nearest-neighbors-regression
5. Реализовать свою версию KNN на C++
6. Сравнить KNN с другими алгоритмами классификации в задаче Metric learning
