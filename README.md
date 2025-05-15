# UpTrader Django App

![Django](https://img.shields.io/badge/Django-5.2.1-green.svg)
![Python](https://img.shields.io/badge/Python-3.10.12-blue.svg)

Демо-проект в рамках тестового задания для UpTrader.

## 🚀 Быстрый старт

### Установка и запуск

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/yourusername/UpTraderDjangoApp.git
cd UpTraderDjangoApp
```
   
2. **Создайте и активируйте виртуальное окружение**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate     # Windows
```

3. **Установите зависимости**

```bash
pip install -r requirements.txt
```

4. **Настройте базу данных**
```bash
cd uptrader/
python manage.py makemigrations
python manage.py migrate
```
5. Загрузите демо-данные
```bash
python manage.py loaddata db_data.json
```

6. Запустите сервер
```bash
python manage.py runserver
```

7. Откройте в браузере http://localhost:8000/


> [!NOTE]
> 🔐 Доступ к админ-панели
> Для входа в административный раздел используйте:
> Логин: admin
> Пароль: 12345


> [!IMPORTANT]
> Все секретные данные указаны намеренно, так как проект является демонстрационным.

📌 Особенности проекта:
- Реализация древовидного меню
- Оптимизированные запросы к БД
- Готовые демо-данные
- Простая установка и настройка

📂 Структура проекта
```
UpTraderDjangoApp/

├── uptrader/
│   ├── static/             # Статический контент            
│   ├── uptrader/           # Основное приложение
│   ├── tree_menu/          # Приложение древовидного меню
│   ├── manage.py
│   └── ...
├── requirements.txt        # Зависимости
└── db_data.json            # Фикстура с данными для демонстрации
```
📝 Лицензия
Этот проект является тестовым заданием и не имеет лицензии.
