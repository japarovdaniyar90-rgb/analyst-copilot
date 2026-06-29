# Product Requirements Document (PRD)

# Analyst Copilot

Version: 0.1

Author: Daniyar

Status: Draft

---

# Vision

Analyst Copilot — AI-помощник системного аналитика.

Продукт помогает анализировать бизнес-требования, выявлять недостающую информацию, проводить интервью с аналитиком и автоматически формировать качественную техническую документацию.

Главная цель продукта — сократить время подготовки SRS и повысить качество требований.

---

# Problem

Сегодня системный аналитик получает информацию из разных источников:

- BRD
- Confluence
- Jira
- Swagger
- BPMN
- Sequence Diagram
- Figma
- SQL
- Email
- Устные требования

После этого аналитик вручную:

- анализирует документы
- ищет противоречия
- задает вопросы заказчику
- пишет SRS
- строит UML-диаграммы
- оформляет документацию

Это занимает значительное время.

---

# Solution

Analyst Copilot берет на себя рутинную работу.

Пользователь загружает документы.

AI анализирует их.

Выявляет отсутствующие требования.

Формирует вопросы.

После получения ответов автоматически создает качественный SRS.

---

# Product Goals

Основные цели:

- уменьшить время подготовки SRS
- повысить качество требований
- уменьшить количество пропущенных требований
- стандартизировать документацию
- ускорить работу аналитика

---

# Non Goals

Проект НЕ является:

- генератором кода
- системой управления проектами
- BPM системой
- Jira replacement
- Confluence replacement

---

# Target Users

Primary User

System Analyst

В будущем:

- Product Manager
- Business Analyst
- QA Engineer

---

# User Journey

Создать проект

↓

Добавить документы

↓

AI анализирует документы

↓

AI извлекает требования

↓

AI выявляет пробелы

↓

AI проводит интервью

↓

AI формирует Knowledge Model

↓

AI генерирует SRS

↓

AI строит диаграммы

↓

Экспорт DOCX

---

# MVP

Версия 1

Создание проекта

Загрузка BRD

Парсинг BRD

Requirement Extraction

Gap Analysis

Interview

SRS

DOCX

---

# Future

Проверка существующего SRS

Swagger Analysis

BPMN Analysis

PlantUML

OpenAPI

ER Diagram

Sequence Diagram

Integration with Jira

Integration with Confluence

Web UI

Desktop App

VS Code Extension

---

# Success Metrics

Подготовка SRS менее чем за 15 минут.

Не менее 90% обязательных требований извлечены автоматически.

Не менее 80% вопросов заказчику сформированы автоматически.

Минимизация ручного редактирования документа.

---

# Guiding Principles

AI не придумывает требования.

AI задает вопросы, если информации недостаточно.

AI никогда не генерирует SRS напрямую.

Сначала строится Knowledge Model.

Только затем создается документ.

---

# AI Pipeline

Document

↓

Parser

↓

Requirement Extractor

↓

Gap Analyzer

↓

Interview Agent

↓

Knowledge Model

↓

SRS Generator

↓

Reviewer

↓

DOCX Export

---

# Release Plan

EPIC 1

Project Management

EPIC 2

Documents

EPIC 3

AI

EPIC 4

Export

EPIC 5

Integrations

EPIC 6

Knowledge Base

---

# Long-term Vision

Analyst Copilot должен стать персональным AI System Analyst.

Он должен не просто отвечать на вопросы пользователя, а помогать принимать инженерные решения, анализировать требования, выявлять риски и автоматически формировать качественную проектную документацию.