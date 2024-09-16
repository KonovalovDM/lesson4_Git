# Это учебный код по изучению расширенных возможностей Git

a = 10
b = 20
c = a + b
print(c)          # печать произведения суммы
# Функция добавления задачи в План, которая запускается по нажатию кнопки
def task_writing():
    task = entry.get()
    if task != '':
        task_listBox.insert(tk.END, task)
        entry.delete(0, tk.END)
        label.config(text=f'\nВнесите задачу в План\nЗадача записана, можно внести следующую\n')
        save_tasks()  # Сохраняем задачи после добавления новой

if __name__ == '__main__':
    print('Hello, World!')
