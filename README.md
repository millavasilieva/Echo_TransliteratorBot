# Echo_TransliteratorBot
Bot that helps you transliterate Russian names to English according to official transliteration rules of Ministry of Foreign Affairs.

Инструкция по запуску бота:
1. Установите Docker, если он у вас еще не установлен. Информацию по установке можно найти здесь: https://docs.docker.com/engine/install/
2. Получите свой токен в телеграм боте @BotFather,кликните на /token и скопируйте.
3. Теперь откройте файл config.py и вставьте туда токен. После сохраните файл.
4. В терминале дойдите до папки(директоории) с файлами и по очереди задайте команды:
  - docker build .  #точка не лишняя
  - docker images
5. Скопируйте ID последнего IMAGE (должен быть создан несколько секунд назад), и напишите в терминале:
  - docker run -d -p 80:80 [вставляем IMAGE ID] 
