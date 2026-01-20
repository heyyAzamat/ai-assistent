#Assistent's logic

# import pygame
# import sys
# import os

# pygame.init()

# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size() #constants
# IMAGE_FOLDER = "emotions"
# images = [
#     os.path.join(IMAGE_FOLDER, file)
#     for file in os.listdir(IMAGE_FOLDER)
#     if file.lower().endswith((".png", ".jpg", "jpeg"))
# ]

# if not images:
#     pygame.quit()
#     sys.exit()

# current_index = 0

# def load_image(index):
#     image = pygame.image.load(images[index])
#     image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
#     return image 

# current_image = load_image(current_index)

# clock = pygame.time.Clock()
# clock.tick(60)

# while running:
#     for event in pygame.event.get():
#         if event.key == pygame.K_ESCAPE:
#             running = False 
#             current_index = (current_index + 1) % len(images)
#             screen_blit(current_image, (0, 0))
#             pygame.display.flip()
#             pygame.quit()
#             sys.exit()

# import time

# def countdown(seconds, label):
#     while seconds > 0:
#         mins, secs = divmod(seconds, 60)
#         print(f"{label}: {mins:02d}:{secs:02d}")
#         time.sleep(1)
#         seconds -= 1
#     print(f"{label} закончено!\n")

# print("Pomodoro таймер")
# cycles = int(input("Сколько помодоро сделать? "))

# for i in range(1, cycles + 1):
#     print(f"Помодоро {i}")
#     countdown(25 * 60, "Фокус")
    
#     if i != cycles:
#         countdown(5 * 60, "Отдых")

# print("Все помодоро завершены, красавчик")


from datetime import datetime
import random
import time

print("Ассистент запущен.")
print("Доступные команды: привет, время, дата, как дела, помощь, выход")

running = True

while running:
    command = input("Ты: ").lower().strip()
    
    if command == "привет":
        print("Привет! Чем могу помочь?")

    elif command == "pomodoro":
        minutes = 24
        seconds = 60
        while seconds > 0:
            print(f"{minutes:02d}:{seconds:02d}")
            time.sleep(1)
            seconds -= 1

    elif command == "как дела?":
        answers = [
            "Отлично!",
            "Работаю в штатном режиме.",
            "Готов помогать."
        ]
        print("Ассистент:", random.choice(answers))
    elif command == "время":
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Ассистент: Текущее время - {current_time}")
    
    elif command == "дата":
        current_date = datetime.now().strftime("%d.%m.%Y")
        print(f"Ассистент: Сегодня {current_date}")

    elif command == "помощь":
        print("Ассистент: Я понимаю следующие команды:")
        print("- привет")
        print("- как дела")
        print("- время")
        print("- дата")
        print("- помощь")
        print("- выход")
        print("- pomodoro")

    elif command == "выход":
        print("Ассистент: До свидания!")
        running = False
    
    else:
        print("Ассистент: Я не понимаю эту команду.")
