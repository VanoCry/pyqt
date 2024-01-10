# CryptoPyPlayer (V1.0) 
## Простой mp3 плеер на Python (в данный момент разрабатывается продвинутая версия)
## Продвинутая версия описана ниже⬇️
### Программа разработана в рамках курсового проекта
![image](https://github.com/VanoCry/pyqt/assets/76244655/88c23830-16a1-421f-a47c-4f8eb90f7a0a)
![image](https://github.com/VanoCry/pyqt/assets/76244655/e1b6f40f-742a-4d64-9a29-df31118a5c82)
## Запуск
```
py -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
py main.py
```
## После работы программы
```
deactivate
```
> [!NOTE]
> kanban-таблица задач (не используется с середины разработки)
> https://docs.google.com/spreadsheets/d/13DF5uAvmG-ydHSbcvcPqvx3hM5Xp3ycSUn7dXnFa-O0/edit?usp=sharing

# SoundEnginePlayer (V2.0)
## Продвинутая версия плеера с минималистичным дизайноми эквалайзером
> [!NOTE]
> Версия mp3 плеера будет написана на совершенной другом звуковом движке




![image](https://github.com/VanoCry/pyqt/assets/76244655/229912d3-0c1a-4e7c-b760-dbb6195c5b11)



> [!TIP]
> *Звуки сверчков*


> [!CAUTION]
> Разработка версии приостановлена по причине неактуальности библиотеки pydub и ближайщих библиотек для работы со звуком

### Через 2 дня чтения документации оказалось что при хорошей работе с эквалайзером, библиотека не имеет метода паузы (только стоп) а также имеет кривой метод изменения громкости только при буферизации файла.
