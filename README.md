🚀 Быстрый старт
Предварительные требования
Python 3.10 или выше
pip
Git
Установка
# 1. Клонировать репозиторий
git clone https://github.com/glebzerg/selectel-qa-task2.git
cd selectel-qa-task2
# 2. Создать виртуальное окружение (рекомендуется)
python -m venv venv
# Активация на macOS/Linux:
source venv/bin/activate
# Активация на Windows:
venv\Scripts\activate
# 3. Установить зависимости
pip install -r requirements.txt
# 4. Установить браузеры Playwright
playwright install chromium
# 5. Скопировать конфиг окружения (опционально)
cp .env.example .env
