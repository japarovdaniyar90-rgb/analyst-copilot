# Project

Мы разрабатываем коммерческий pet-проект "Analyst Copilot".

Это AI-помощник системного аналитика.

Стек:

- Python 3.14
- python-telegram-bot
- Pydantic v2
- SQLite (позже)
- OpenAI (позже)

Важно:

Проект строится по Clean Architecture.

Telegram является только интерфейсом.

Бизнес-логика не должна находиться в Telegram Handler.

Архитектура:

Telegram
↓
Handlers
↓
Services
↓
Storage
↓
Models

Текущая структура проекта:

app/
├── ai/
├── bot/
├── exporters/
├── models/
├── parsers/
├── services/
├── storage/
├── config.py
└── main.py

---

# Задача DEV-003

Нужно реализовать создание проектов.

Требования:

После нажатия кнопки

📝 Новый проект

бот должен перейти в режим ожидания описания.

После получения текстового сообщения необходимо создать новый Project.

Использовать Pydantic BaseModel.

Создать следующие файлы:

models/project.py

storage/projects.py

services/project_service.py

Перенести бизнес-логику создания проекта в ProjectService.

Storage пока хранит данные в памяти.

Не использовать SQLite.

---

Project должен иметь поля:

id

title

description

status

created_at

documents

---

Storage должен иметь методы

create()

get()

list()

delete()

---

ProjectService должен содержать бизнес-логику.

Telegram Handler должен только вызвать сервис.

---

После создания проекта бот отвечает:

✅ Проект создан

ID: ...

Название: ...

Статус: Draft

---

Использовать typing.

Использовать datetimes.

Использовать современные возможности Python 3.14.

Комментарии только там, где действительно необходимы.

Не менять существующую архитектуру без необходимости.

После выполнения покажи список измененных файлов и объясни архитектурные решения.