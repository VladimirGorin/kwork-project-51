import sys, subprocess

print("\nЗапуск установки...\n")

try:
    if sys.version_info < (3, 10, 5):
        print("Версия Python ниже 3.10.5. Пожалуйста, установите более новую версию.")
        sys.exit(1)

    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    input("\nНажмите ENTER что бы завершить установку")

    from clear_screen import clear
    clear()

except Exception:
    print("Ошибка при установке зависимостей. Убедитесь, что файл requirements.txt существует и содержит правильные зависимости.")
    sys.exit(1)
