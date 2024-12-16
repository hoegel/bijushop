# BIJU SHOP

BIJU SHOP — это учебный проект интернет-магазина косметики, созданный для практики работы с Django и Bootstrap. Проект включает базовые функции интернет-магазина: просмотр товаров, управление корзиной, а также административный функционал.

---

## Основной функционал

**Каталог товаров**:
   - Просмотр всех доступных товаров
   - Переход к детальной странице товара

**Корзина**:
   - Просмотр добавленных товаров
   - Возможность изменить количество или удалить товар
   - Общая стоимость заказа

**Управление товарами**:
   - Добавление товаров для администратора
---

## Используемые версии:

- Python 3.11.2
- Django 5.1.4
- Bootstrap 4

---

## Инструкция к запуску

### 1. Клонирование репозитория
```bash
git clone https://github.com/hoegel/bijushop.git
cd bijushop
```

### 2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv <venvname>
venv\Scripts\activate
```
После этого установите локальные зависимости, сделайте миграцию и запустите сервер.

Теперь проект доступен по адресу: http://127.0.0.1:8000/