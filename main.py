import tkinter as tk
from tkinter import messagebox
import random
import threading
import turtle
import time

# ==== QUESTIONS ====
questions = {
    "Science": [
        {"question": "What is the boiling point of water?", "options": ["90\u00b0C", "100\u00b0C", "80\u00b0C", "120\u00b0C"], "answer": "100\u00b0C"},
        {"question": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
        {"question": "H2O is the chemical formula for?", "options": ["Oxygen", "Water", "Hydrogen", "Salt"], "answer": "Water"},
        {"question": "Which organ pumps blood?", "options": ["Lungs", "Kidney", "Heart", "Liver"], "answer": "Heart"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Earth", "Jupiter", "Venus"], "answer": "Mars"},
    ],
    "Math": [
        {"question": "What is 12 \u00d7 8?", "options": ["96", "88", "108", "86"], "answer": "96"},
        {"question": "What is the square root of 144?", "options": ["11", "13", "12", "14"], "answer": "12"},
        {"question": "What is 25% of 200?", "options": ["50", "25", "75", "60"], "answer": "50"},
        {"question": "What is 1/2 of 1/4?", "options": ["1/2", "1/4", "1/8", "1/6"], "answer": "1/8"},
        {"question": "What is 9 squared?", "options": ["81", "18", "27", "72"], "answer": "81"},
    ],
    "English": [
        {"question": "Which word is a noun?", "options": ["Quickly", "Apple", "Run", "Blue"], "answer": "Apple"},
        {"question": "What is the opposite of 'cold'?", "options": ["Cool", "Warm", "Hot", "Freezing"], "answer": "Hot"},
        {"question": "'He ___ to school daily.'", "options": ["go", "goes", "going", "gone"], "answer": "goes"},
        {"question": "Choose the correct spelling:", "options": ["Enviroment", "Environment", "Enviornment", "Envirenment"], "answer": "Environment"},
        {"question": "What is the plural of 'mouse'?", "options": ["Mouses", "Mouse", "Mices", "Mice"], "answer": "Mice"},
    ],
    "Social Science": [
        {"question": "Who was the first President of India?", "options": ["Rajendra Prasad", "Jawaharlal Nehru", "Gandhi", "Radhakrishnan"], "answer": "Rajendra Prasad"},
        {"question": "Where is the Taj Mahal?", "options": ["Delhi", "Mumbai", "Agra", "Jaipur"], "answer": "Agra"},
        {"question": "Which is the national bird of India?", "options": ["Crow", "Sparrow", "Peacock", "Pigeon"], "answer": "Peacock"},
        {"question": "What is the capital of Haryana?", "options": ["Faridabad", "Panipat", "Gurugram", "Chandigarh"], "answer": "Chandigarh"},
        {"question": "Which festival is known as the festival of lights?", "options": ["Holi", "Diwali", "Eid", "Baisakhi"], "answer": "Diwali"},
    ],
    "Haryana GK": [
        {"question": "What is the folk dance of Haryana?", "options": ["Bhangra", "Ghoomar", "Jhumar", "Garba"], "answer": "Jhumar"},
        {"question": "Who is known as the 'Iron Man' of Haryana?", "options": ["Bhagat Singh", "Lal Bahadur Shastri", "Ch. Devi Lal", "Sardar Patel"], "answer": "Ch. Devi Lal"},
        {"question": "Which sport is most popular in Haryana?", "options": ["Cricket", "Kabaddi", "Football", "Tennis"], "answer": "Kabaddi"},
        {"question": "Which river flows through Haryana?", "options": ["Ganga", "Yamuna", "Saraswati", "Krishna"], "answer": "Yamuna"},
        {"question": "Haryana was carved out of which state?", "options": ["Punjab", "Rajasthan", "UP", "MP"], "answer": "Punjab"},
    ],
    "sports": [
        {"question": "How many players in a cricket team?", "options": ["10", "11", "12", "9"], "answer": "11"},
        {"question": "Which country invented chess?", "options": ["China", "India", "Russia", "USA"], "answer": "India"},
        {"question": "How many rings are there in Olympic symbol?", "options": ["4", "5", "6", "7"], "answer": "5"},
        {"question": "Which sport uses a shuttlecock?", "options": ["Tennis", "Badminton", "Squash", "Football"], "answer": "Badminton"},
        {"question": "What is the national game of India?", "options": ["Cricket", "Hockey", "Kabaddi", "Football"], "answer": "Hockey"},
    ],
}

# ==== MAIN APP ====
class FunLearningApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fun Learning App")
        self.geometry("600x500")
        self.resizable(False, False)
        self.configure(bg="#e0d8c3")
        self.username = ""
        self.show_welcome_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_screen()
        tk.Label(self, text="\ud83d\udc4b Welcome to Fun Learning App", font=("Arial", 20, "bold"), bg="#e0d8c3").pack(pady=30)
        tk.Label(self, text="Enter your name:", font=("Arial", 14), bg="#e0d8c3").pack(pady=10)
        name_entry = tk.Entry(self, font=("Arial", 14))
        name_entry.pack(pady=5)

        def start_app():
            name = name_entry.get().strip()
            if not name:
                messagebox.showwarning("Input Error", "Please enter your name!")
                return
            self.username = name
            self.show_main_menu()

        tk.Button(self, text="Start", font=("Arial", 14), command=start_app).pack(pady=20)

    def show_main_menu(self):
        self.clear_screen()
        tk.Label(self, text=f"\ud83c\udf93 Fun Learning App", font=("Arial", 24, "bold"), bg="#e0d8c3").pack(pady=20)
        tk.Label(self, text=f"Hello, {self.username}!", font=("Arial", 16), bg="#e0d8c3").pack(pady=5)
        tk.Button(self, text="\ud83e\udde0 Start Quiz", font=("Arial", 16), command=self.start_quiz).pack(pady=10)
        tk.Button(self, text="\ud83c\udfae Play Snake Game", font=("Arial", 16), command=self.start_snake_game).pack(pady=10)
        tk.Button(self, text="\ud83c\udfa8 Drawing Pad", font=("Arial", 16), command=self.start_drawing).pack(pady=10)
        tk.Button(self, text="\ud83e\udde9 Play Puzzle", font=("Arial", 16), command=self.start_puzzle_game).pack(pady=10)
        tk.Button(self, text="\ud83d\udeaa Exit", font=("Arial", 14), command=self.quit).pack(pady=30)

    def start_quiz(self):
        QuizApp(self, questions, self.username)

    def start_snake_game(self):
        threading.Thread(target=snake_game).start()

    def start_drawing(self):
        DrawingPad(self)

    def start_puzzle_game(self):
        PuzzleGame(self)

# ==== PUZZLE GAME ====
class PuzzleGame(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Puzzle Game - Unscramble the Word")
        self.geometry("400x300")
        self.configure(bg="lightyellow")

        words = ["apple", "banana", "orange", "school", "pencil", "haryana"]
        self.correct_word = random.choice(words)
        scrambled = ''.join(random.sample(self.correct_word, len(self.correct_word)))

        tk.Label(self, text=f"Unscramble: {scrambled}", font=("Arial", 18), bg="lightyellow").pack(pady=20)
        self.entry = tk.Entry(self, font=("Arial", 16))
        self.entry.pack(pady=10)
        tk.Button(self, text="Submit", command=self.check_answer).pack(pady=10)
        self.result_label = tk.Label(self, text="", font=("Arial", 14), bg="lightyellow")
        self.result_label.pack(pady=10)

    def check_answer(self):
        if self.entry.get().lower() == self.correct_word:
            self.result_label.config(text="\u2705 Correct!", fg="green")
        else:
            self.result_label.config(text=f"\u274c Wrong! Try again.", fg="red")

# ==== SNAKE GAME ====
def snake_game():
    import turtle
    import time
    import random

    delay = 0.1
    score = 0
    high_score = 0

    # Set up screen
    win = turtle.Screen()
    win.title("Snake Game")
    win.bgcolor("black")
    win.setup(width=600, height=600)
    win.tracer(0)  # Turns off the screen updates

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("green")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    segments = []

    # Score display
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))

    # Movement functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    # Keyboard bindings
    win.listen()
    win.onkeypress(go_up, "Up")
    win.onkeypress(go_down, "Down")
    win.onkeypress(go_left, "Left")
    win.onkeypress(go_right, "Right")

    # Main game loop
    while True:
        win.update()

        # Border collision
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

        # Food collision
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            # Add new segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("lightgreen")
            new_segment.penup()
            segments.append(new_segment)

            # Update score
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

        # Move segments
        for i in range(len(segments)-1, 0, -1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x, y)

        if segments:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        # Self collision
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                score = 0
                pen.clear()
                pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

        time.sleep(delay)

# ==== DRAWING PAD ====
class DrawingPad(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Drawing Pad")
        self.geometry("600x400")
        self.canvas = tk.Canvas(self, bg="white", width=600, height=400)
        self.canvas.pack()
        self.old_x = None
        self.old_y = None

        self.canvas.bind("<Button-1>", self.set_start)
        self.canvas.bind("<B1-Motion>", self.draw)

    def set_start(self, event):
        self.old_x = event.x
        self.old_y = event.y

    def draw(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, fill="black", width=3)
        self.old_x = event.x
        self.old_y = event.y

# ==== QUIZ CLASS ====
class QuizApp:
    def __init__(self, root, questions, username):
        self.root = root
        self.questions = questions
        self.username = username
        self.qn = 0
        self.score = 0
        self.timer_seconds = 20
        self.selected = tk.IntVar()
        self.subject_var = tk.StringVar()
        self.quiz_data = []
        self.timer_label = None
        self.timer_job = None
        self.create_subject_screen()

    def create_subject_screen(self):
        self.root.clear_screen()
        tk.Label(self.root, text=f"{self.username}, Select Subject", font=("Arial", 18), bg="#f0f8ff").pack(pady=20)
        subjects = list(self.questions.keys())
        self.subject_var.set(subjects[0])
        tk.OptionMenu(self.root, self.subject_var, *subjects).pack(pady=10)
        tk.Button(self.root, text="Start Quiz", font=("Arial", 14), command=self.start_quiz).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.root.show_main_menu).pack()

    def start_quiz(self):
        self.qn = 0
        self.score = 0
        self.quiz_data = random.sample(self.questions[self.subject_var.get()], min(10, len(self.questions[self.subject_var.get()])))
        self.show_question()

    def show_question(self):
        self.root.clear_screen()
        if self.qn >= len(self.quiz_data):
            self.show_result()
            return

        current_q = self.quiz_data[self.qn]
        tk.Label(self.root, text=f"Q{self.qn+1}: {current_q['question']}", font=("Arial", 14), wraplength=500, bg="#f0f8ff").pack(pady=20)
        self.selected.set(-1)
        for idx, opt in enumerate(current_q["options"]):
            tk.Radiobutton(self.root, text=opt, variable=self.selected, value=idx, font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", padx=50)

        self.timer_label = tk.Label(self.root, text="", font=("Arial", 12), fg="red", bg="#f0f8ff")
        self.timer_label.pack(pady=10)
        self.update_timer(self.timer_seconds)

        tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 12)).pack(pady=20)

    def update_timer(self, seconds):
        self.timer_label.config(text=f"Time Left: {seconds}s")
        if seconds > 0:
            self.timer_job = self.root.after(1000, self.update_timer, seconds - 1)
        else:
            self.next_question()

    def next_question(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)

        if self.selected.get() == -1:
            messagebox.showwarning("Alert", "Time's up or No answer selected!")
        else:
            if self.quiz_data[self.qn]["options"][self.selected.get()] == self.quiz_data[self.qn]["answer"]:
                self.score += 1

        self.qn += 1
        self.show_question()

    def show_result(self):
        self.root.clear_screen()
        tk.Label(self.root, text=f"Great job, {self.username}!\nYour Score: {self.score}/{len(self.quiz_data)}", font=("Arial", 16), bg="#f0f8ff").pack(pady=30)
        tk.Button(self.root, text="Play Again", command=self.create_subject_screen).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", command=self.root.show_main_menu).pack()

# ==== RUN APP ====
if __name__ == "__main__":
    app = FunLearningApp()
    app.mainloop()
