
# ELK-стек: Образовательный курс по системам наблюдаемости

Цель курса: Подготовить инженеров к проектированию, внедрению и сопровождению современных систем наблюдаемости на базе ELK-стека и смежных технологий.

---

## Описание

Этот курс — полноценный образовательный продукт по системам наблюдаемости (Observability), охватывающий теорию, практику и интеграцию с современной инфраструктурой.  
Курс разработан на основе реального опыта работы в банковской сфере и BigData, с акцентом на практическое применение в DevOps, SRE и Data Engineering средах.

Все материалы автоматически преобразованы в интерактивный веб-сайт с помощью MkDocs и темы Material, и упакованы в Docker-контейнер для мгновенного запуска без зависимостей.

---

## Структура курса

### 10 теоретических модулей
1. Введение в системы наблюдаемости  
   Что такое observability: логи, метрики, трейсы  
   Сравнение парадигм: централизованное логирование, SIEM, observability  
   Требования к платформам хранения и анализа  
   Обзор экосистем: Elastic Stack vs OpenSearch vs Grafana Loki  

2. Архитектура ELK-стека  
   Назначение и компоненты: Elasticsearch, Logstash, Beats, Kibana  
   Роль каждого компонента в пайплайне  
   Интеграция с инфраструктурой: Docker, Kubernetes, облачные провайдеры  
   Альтернативы: Fluent Bit, Vector, Promtail, OpenTelemetry  

3. Сбор и обработка логов  
   Pull vs Push модели сбора  
   Использование Filebeat, Metricbeat, Journalbeat  
   Парсинг логов: Grok, dissect, JSON, multiline  
   Пайплайны в Logstash и Vector  
   Пример: парсинг Nginx-логов с извлечением user_id, request_url, response_time  

4. Mapping, Dynamic Templates и типы данных  
   Основы маппинга: явный vs динамический  
   Категории типов данных: text, keyword, date, nested, wildcard  
   Dynamic templates: управление автоматическим маппингом  
   Multi-fields: одновременное использование text и keyword  
   Best practices: оптимизация под агрегации, поиск и хранение  

5. Хранение и масштабирование  
   Принципы шардирования и репликации  
   Hot-Warm-Cold-Frozen архитектура  
   Index Lifecycle Management (ILM)  
   Сравнение подходов: Elasticsearch vs Loki (на основе кейса Badoo, 2020)  
   Управление потреблением памяти и дискового пространства  

6. Поиск и анализ в Kibana  
   Интерфейс Discover: фильтрация, сортировка, экспорт  
   Создание визуализаций: гистограммы, таблицы, pie charts  
   Построение дашбордов  
   Использование Lens для быстрого анализа  
   Расширенные запросы: Lucene, Painless scripts  

7. Алертинг и машинное обучение  
   Настройка правил оповещения в Kibana  
   Алертинг по логам: шаблоны ошибок, rate-метрики  
   Интеграция с Slack, PagerDuty, Email  
   Встроенные ML-функции Elasticsearch:  
   Автообнаружение аномалий  
   Прогнозирование трендов  
   Кластеризация поведения  

8. Structured Logging и контракты событий  
   Преимущества структурированных логов  
   Проектирование контрактов: общие, прикладные, access-логи  
   Использование @timestamp, service, host, trace_id  
   Обезличенные сообщения (generic messages)  
   Снижение кардинальности и повышение эффективности поиска  

9. Интеграция с другими системами  
   Связь логов и метрик: сквозная корреляция  
   Использование Logstash как брокера  
   Интеграция с Kafka, Redis, S3  
   Отправка данных в Prometheus через Logstash или Vector  
   Unified Pipeline: один путь для всех типов телеметрии  

10. Миграция, мониторинг и производительность  
   Миграция с ELK на OpenSearch или Loki  
   Мониторинг самого стека: состояние узлов, heap usage, задержки  
   Диагностика узких мест: медленные запросы, высокая нагрузка на I/O  
   Best practices для production-сред  
   Резервное копирование и восстановление: snapshots  

### Практика: 8 лабораторных работ
- Развертывание ELK-стека в Docker/Kubernetes  
- Настройка Filebeat для сбора Nginx и Java-логов  
- Создание пайплайна Logstash с парсингом и enrich-операциями  
- Проектирование mapping и dynamic templates  
- Построение дашборда в Kibana с алертами  
- Настройка ILM-политики для ротации индексов  
- Реализация structured logging в микросервисе (Python/Java)  
- Интеграция с Prometheus и Alertmanager  

### Дополнительные материалы
- [Badoo, 2020] «Grafana Loki: альтернатива ELK?» — сравнение стоимости и производительности  
- Официальная документация Elastic и Grafana  
- Видео: “How Loki Correlates Metrics and Logs”, DevOpsDays 2019  
- Шаблоны конфигураций: Filebeat, Logstash, Kibana dashboards  

---

## Как запустить курс

### Требования
- Docker (рекомендуется версия 20.10+)

### 1. Соберите образ
```bash
docker build -t elk-course-mkdocs .
```

### 2. Запустите контейнер
```bash
docker run -d -p 8001:8000 elk-course-mkdocs
```

> Если порт 8001 занят — используйте другой: -p 8002:8000

### 3. Откройте в браузере
http://localhost:8001

---

## Особенности сайта

- Тема Material с тёмным оформлением по умолчанию  
- Чёткая навигация: Модули → Практика → Дополнительно  
- Встроенный поиск по всему содержанию  
- Автоматическое оглавление на каждой странице  
- Возможность переключения между светлой и тёмной темой  

---

## Технологии

- Python — парсинг исходного файла ELK_curs.md и генерация Markdown  
- MkDocs — создание статического сайта  
- Material for MkDocs — современная тема с поддержкой TOC, поиска и тем  
- Docker — изолированное, воспроизводимое окружение  
- HTTP.server — лёгкий веб-сервер для раздачи сайта  

---

## Структура проекта

```
elk-course/
├── ELK_curs.md                  # Исходный текст курса
├── generate_course.py           # Скрипт: парсит .md → генерирует сайт
├── Dockerfile                   # Сборка образа
├── mkdocs.yml                   # Конфигурация сайта
├── docs/                        # Сгенерированные страницы
│   ├── index.md
│   ├── modules/
│   │   ├── module_01.md
│   │   └── ...
│   ├── practice/
│   │   └── labs.md
│   └── extra/
│       └── extra.md
└── README.md                    # Этот файл
```

---

## Для преподавателей и команд

- Идеально для внутреннего обучения — запустил один раз и всё готово  
- Подходит для собеседований — покажите ссылку как портфолио  
- Легко обновлять — правите ELK_curs.md → пересобираете образ  
- Готов к расширению — можно добавить тесты, PDF, викторины  

---

## Дополнительные материалы (по запросу)

Вот список рекомендуемой литературы и официальных источников по ELK-стеку (Elastic Stack), который можно использовать для углублённого изучения тем курса:

---

###  Официальная документация (наиболее важные ресурсы)

1. **Elastic Documentation**  
   https://www.elastic.co/guide/index.html  
   Полная документация по всем компонентам: Elasticsearch, Logstash, Kibana, Beats.

2. **Elasticsearch: The Definitive Guide**  
   https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html  
   Подробное руководство по архитектуре, индексации, поиску и анализу.

3. **Logstash Documentation**  
   https://www.elastic.co/guide/en/logstash/current/index.html  
   Включает примеры пайплайнов, фильтров (Grok, dissect), input/output плагинов.

4. **Kibana User Guide**  
   https://www.elastic.co/guide/en/kibana/current/index.html  
   Работа с Discover, Visualize, Dashboard, Lens, APM, Machine Learning.

5. **Beats Platform Reference**  
   https://www.elastic.co/guide/en/beats/libbeat/current/index.html  
   Filebeat, Metricbeat, Journalbeat, Heartbeat — сбор данных в реальном времени.

6. **Index Lifecycle Management (ILM)**  
   https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html  
   Управление жизненным циклом индексов: hot, warm, cold, delete phases.

7. **Elastic Security & SIEM Guide**  
   https://www.elastic.co/guide/en/security/current/index.html  
   Интеграция с SIEM, обнаружение угроз, корреляция событий.

8. **Observability Guide (APM, Logs, Metrics, Uptime)**  
   https://www.elastic.co/guide/en/observability/current/index.html  
   Мониторинг приложений, трейсинг, structured logging, алертинг.

9. **Painless Scripting Language**  
   https://www.elastic.co/guide/en/elasticsearch/painless/current/index.html  
   Язык скриптов для сложных запросов, агрегаций и обработки данных.

10. **Elastic Community & Discuss Forum**  
    https://discuss.elastic.co/  
    Активное сообщество для решения вопросов по настройке и эксплуатации.

---

###  Книги

1. **"Elasticsearch in Action"** — Radu Gheorghe, Matthew Lee Hinman, Roy Russo  
   Практическое руководство по развертыванию, оптимизации и использованию Elasticsearch.

2. **"Learning Elastic Stack 8.0"** — Bharvi Dixit  
   Современное руководство по Elastic Stack 8.x: от установки до машинного обучения и безопасности.

3. **"Mastering ElasticSearch"** — Bahaaldine Azarmi  
   Подробный разбор продвинутых тем: масштабирование, производительность, кластеризация.

4. **"The Logstash Book"** — James Densmore  
   Практические примеры пайплайнов, парсинг логов, работа с Grok и JSON.

---

###  Дополнительные материалы  

1. **[Badoo, 2020] "Grafana Loki: альтернатива ELK?"**  
   Сравнение стоимости хранения, производительности и архитектуры между ELK и Loki.

2. **Видео: "How Loki Correlates Metrics and Logs"** — DevOpsDays 2019  
   Обзор интеграции метрик и логов в Grafana Loki.

3. **OpenSearch Documentation**  
   https://opensearch.org/docs/latest/  
   Альтернатива Elastic Stack с открытым исходным кодом.

4. **Fluent Bit / Fluentd Documentation**  
   https://docs.fluentbit.io/manual  
   Лёгковесная альтернатива Beats.

5. **Vector.dev Documentation**  
   https://vector.dev/docs/  
   Высокопроизводительный агент для телеметрии.

---



