# Ссылки

[Про курс Воронцова](https://goo.gl/kDqf9y)

[Все лекции Воронцова на ютубе](https://www.youtube.com/playlist?list=PLJOzdkh8T5kp99tGTEFjH_b9zqEQiiBtC)

[Канал ШАД на ютубе](https://www.youtube.com/channel/UCKFojzto0n4Ab3CRQRZ2zYA)

[machinelearning](http://www.machinelearning.ru/wiki/index.php?title=%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0)

[habrahabr](https://habrahabr.ru/company/yandex/blog/208034/)

[Лекции Воронцова в ШАД](https://yandexdataschool.ru/edu-process/courses/machine-learning)

[Лекции Соколова](https://github.com/rumary/ml-course-hse)


# Занятие 1

Задача про гауссовы облака

* Сделать три датасета с гауссовыми облаками
  * облака различимы (расстояние между центрами порядка трёх сигм)
  * облака заметно перекрываются (расстояние между центрами порядка сигмы)
  * облака сильно перекрываются (расстояние между центрами - 0.1 сигмы)
* [Линейный классификатор](http://ru.learnmachinelearning.wikia.com/wiki/%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D1%80) - проецируем на вектор w, если меньше порога - класс 0, больше - класс 1. Посмотреть roc кривую для нескольких заданных вручную положений вектора
* Визуализация
  * нарисовать исходные данные в виде облачков красных и синих точек
  * нарисовать гистограммы для разных векторов w
  * нарисовать [roc кривую](http://ru.learnmachinelearning.wikia.com/wiki/ROC-%D0%BA%D1%80%D0%B8%D0%B2%D0%B0%D1%8F) для нескольких w
* Применить разные классификаторы, сравнить эффективность
  * линейный классификатор
  * knn
  * svm
  * random forest
