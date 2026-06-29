# System Architecture

# Analyst Copilot

Version: 0.1

Status: Draft

---

# Overview

Analyst Copilot представляет собой многослойное приложение.

Основной принцип:

Каждый слой отвечает только за одну задачу.

Telegram является только пользовательским интерфейсом.

Вся бизнес-логика находится внутри Application Layer.

---

# Architecture

                   Telegram

                       │

───────────────────────┼──────────────────────

                       ▼

                Presentation Layer

                 handlers.py

                 keyboards.py

                 states.py

───────────────────────┼──────────────────────

                       ▼

                Application Layer

              Project Service

              Document Service

              AI Service

              Interview Service

              Export Service

───────────────────────┼──────────────────────

                       ▼

                  Domain Layer

Project

Document

Requirement

Question

Answer

Knowledge Model

───────────────────────┼──────────────────────

                       ▼

                 Storage Layer

SQLite

File Storage

Cache

───────────────────────┼──────────────────────

                       ▼

                    AI Layer

Requirement Extractor

Gap Analyzer

Interview Agent

Knowledge Builder

SRS Generator

Reviewer

Diagram Generator

---

# Layers

## Presentation Layer

Отвечает только за взаимодействие с пользователем.

Разрешено:

- читать сообщения

- отправлять сообщения

- вызывать сервисы

Запрещено:

- писать бизнес-логику

- работать с SQLite

- работать с OpenAI напрямую

---

## Application Layer

Главная бизнес-логика.

Каждый Service отвечает только за одну область.

ProjectService

DocumentService

InterviewService

AIService

ExportService

---

## Domain Layer

Главные модели системы.

Project

Document

Requirement

Question

Answer

KnowledgeModel

Все модели используют Pydantic.

---

## Storage Layer

Отвечает исключительно за хранение данных.

Storage ничего не знает про Telegram.

Storage ничего не знает про AI.

В будущем возможна замена SQLite на PostgreSQL.

Без изменения остальных слоев.

---

## AI Layer

Каждый AI Agent решает одну задачу.

---

Requirement Extractor

Извлекает требования.

---

Gap Analyzer

Находит отсутствующую информацию.

Не придумывает данные.

---

Interview Agent

Задает вопросы пользователю.

Не повторяет уже известную информацию.

---

Knowledge Builder

Обновляет внутреннюю модель проекта.

---

SRS Generator

Формирует документ.

Не анализирует BRD.

---

Reviewer

Проверяет качество SRS.

---

Diagram Generator

Создает

PlantUML

Sequence

Activity

ER Diagram

---

# Data Flow

Пользователь

↓

Telegram

↓

Handler

↓

ProjectService

↓

Storage

↓

Project

---

При работе AI

BRD

↓

Parser

↓

Requirement Extractor

↓

Gap Analyzer

↓

Interview Agent

↓

Knowledge Builder

↓

SRS Generator

↓

Reviewer

↓

Export

---

# Storage

На этапе MVP используется SQLite.

Все операции проходят через Storage Layer.

Никакой другой слой не работает напрямую с базой данных.

---

# Dependency Rules

Presentation

может использовать

↓

Application

Application

может использовать

↓

Domain

Storage

AI

Domain

ничего не знает

ни о Telegram

ни о SQLite

ни об OpenAI.

---

# Project Lifecycle

Draft

↓

Collecting Requirements

↓

Documents Uploaded

↓

Analyzing

↓

Interview

↓

Generating SRS

↓

Review

↓

Completed

↓

Archived

---

# Coding Rules

Каждая функция делает только одну задачу.

Максимальный размер файла

≈200 строк.

Максимальный размер функции

≈30 строк.

Использовать typing.

Использовать pathlib.

Использовать Pydantic.

Не использовать глобальные словари вне Storage Layer.

Не использовать print кроме точки входа.

Использовать logging.

---

# Error Handling

Любая ошибка должна быть обработана.

Пользователь никогда не должен видеть Traceback.

Все ошибки логируются.

---

# Future

Архитектура должна позволять добавить:

Web UI

Desktop

REST API

VS Code Extension

Jira Integration

Confluence Integration

без изменения бизнес-логики.