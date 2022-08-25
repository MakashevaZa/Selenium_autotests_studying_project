# Selenium_autotests_studying_project
This is a project for 3d module's (lesson 6) final task:

    Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
    
    Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
    
    Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
    
    В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
    
    Тест должен запускаться с параметром language следующей командой:
    
    pytest --language=es test_items.py
    
    и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
    

![images](https://user-images.githubusercontent.com/37474743/186638146-74d372be-d832-4b4c-b561-4cc8cd57ee53.jpg)

Столкнулась с тем, что информация в курсе немного устарела(?):
1) ловила deprecationWarning при использовании profiles в Firefox, для него в Selenium введен Options
