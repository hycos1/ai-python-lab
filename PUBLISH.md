# Публикация на PyPI

Это краткое руководство по публикации библиотеки `ai-python-lab` на PyPI.

## Предварительные требования

1. Учетная запись на [PyPI](https://pypi.org/account/register/)
2. Учетная запись на [TestPyPI](https://test.pypi.org/account/register/) (для тестирования)
3. Установленные инструменты:
   ```bash
   pip install build twine
   ```

## Шаги для публикации

### 1. Подготовка

Убедитесь, что все изменения закоммичены в git и версия обновлена в `ai_python_lab/__init__.py`.

### 2. Сборка пакета

```bash
python -m build
```

Эта команда создаст файлы в папке `dist/`:
- `ai_python_lab-X.X.X-py3-none-any.whl` (wheel)
- `ai_python_lab-X.X.X.tar.gz` (source distribution)

### 3. Проверка пакета

```bash
twine check dist/*
```

### 4. Тестирование на TestPyPI (рекомендуется)

```bash
twine upload --repository testpypi dist/*
```

Затем протестируйте установку:
```bash
pip install --index-url https://test.pypi.org/simple/ ai-python-lab
```

### 5. Публикация на PyPI

```bash
twine upload dist/*
```

### 6. Проверка публикации

После публикации проверьте:
```bash
pip install ai-python-lab
```

## Настройка API токенов

### Для PyPI

1. Перейдите в [настройки PyPI](https://pypi.org/manage/account/)
2. Создайте API токен
3. Настройте `.pypirc`:

```ini
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = pypi-ваш-токен-здесь
```

### Для TestPyPI

```ini
[distutils]
index-servers = pypi testpypi

[pypi]
username = __token__
password = pypi-ваш-токен-здесь

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-ваш-тест-токен-здесь
```

## Автоматизация с GitHub Actions

Создайте `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [created]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build package
      run: python -m build
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

## Команды для быстрой публикации

```bash
# Очистка предыдущих сборок
rm -rf dist/ build/ *.egg-info/

# Сборка
python -m build

# Проверка
twine check dist/*

# Тест на TestPyPI
twine upload --repository testpypi dist/*

# Публикация на PyPI
twine upload dist/*
```

## Важные замечания

1. **Версионирование**: Используйте семантическое версионирование (major.minor.patch)
2. **Тестирование**: Всегда тестируйте на TestPyPI перед публикацией
3. **Документация**: Убедитесь, что README.md содержит актуальную информацию
4. **Лицензия**: Проверьте, что файл LICENSE корректен
5. **Зависимости**: Убедитесь, что все зависимости указаны в setup.py/pyproject.toml

## Обновление пакета

Для обновления существующего пакета:

1. Увеличьте версию в `ai_python_lab/__init__.py`
2. Обновите CHANGELOG.md (если есть)
3. Соберите и опубликуйте новую версию

## Отзыв пакета

Если нужно отозвать версию:
```bash
twine upload --repository pypi --skip-existing dist/*
```

**Примечание**: PyPI не позволяет удалять или перезаписывать уже опубликованные версии. Можно только отозвать версию, но файлы останутся доступными.
