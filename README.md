# Web3 Multisender
Distribute ether or tokens to multiple addresses.

## Установка и использование
1. Скачиваем и устанавливаем [Python 3.10.8](https://www.python.org/downloads/release/python-3108/).
   - Ставим галочку напротив "Add python.exe to PATH".
2. Запускаем `install.bat`: этот файл установит отсутствующие библиотеки в виртуальное окружение, а также создаст файлы с настройками по умолчанию. Установка может занять несколько минут.
3. Задаем настройки скрипта.
4. Запускаем `start.bat`: этот файл запустит скрипт.

### Настройка
Настройки скрипта находятся в папке `./multisender/settings`.

Основные настройки задаются в `settings.toml`:

```toml
# Количество токенов:
AMOUNT = 0.01
# Отправлять токен (true) или монету сети (false)?
TOKEN_SENDING = true
# Адрес контракта токена:
# (Если token_sending = true)
TOKEN_ADDRESS = "0x0000000000000000000000000000000000000000"
# Провайдер:
# Взять ссылку требуемой сети можно на https://chainlist.org
HTTP_PROVIDER = "https://bsc-testnet.public.blastapi.io"
```

Адреса, на которые будут рассылаться токены, записываются в `public_keys.txt`.

Приватный ключ кошелька, с которого будут рассылаться токены, задается в переменных окружения или в `.env`:

```dotenv
PRIVATE_KEY=your_private_key
```