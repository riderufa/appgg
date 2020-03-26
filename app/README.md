1. Создать каталог mkdir.
2. Инициировать в нем git командой git init.
3. Создать внутри папки проекта папку app.
4. Скопировать приложение в папку app командой git pull https://github.com/riderufa/app
5. Файлы dockerfile, docker-compose.yaml, requirements.txt переместить из папки приложения в папку проекта.
6. Из папки проекта собрать контейнеры командой docker-compose build.
7. Запустить контейнеры командой docker-compose up.
8. Открыть приложение по адресу 0.0.0.0:8081.