import os
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# 현재 작업 디렉토리 가져오기
currentPath = os.getcwd()

# rootDir 설정
rootDir = currentPath.replace('GUIUniApp', '')

# CLIUniApp 모델 디렉토리 경로 추가
utilsPath = os.path.join(rootDir, 'CLIUniApp/src/utils/')
sys.path.append(utilsPath)

# 경로 확인을 위해 출력
print(sys.path)

import validator as val


class LoadingScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="black")
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # 현재 파일의 디렉터리 경로 가져오기:# /Users/irene/_Proj/_FSD_Project/GUIUniApp/src/frames
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # uts_logo.jpg 파일의 전체 경로 만들기
        logo_path = os.path.join(current_dir, "uts_b_logo.jpeg")
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((180, 180), Image.Resampling.LANCZOS)  # 이미지 크기 조정
        logo_img = ImageTk.PhotoImage(logo_image)
        self.logo_label = tk.Label(self, image=logo_img, bg="black", anchor="center")
        self.logo_label.image = logo_img
        self.logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        label = tk.Label(self, text="Welcome to GUIUniApp", fg = '#ffffff',
                         font="Arial 26 bold", bg='black')
        label.place(relx=0.5, rely=0.3, anchor='n')

class LoginFrame(tk.Frame):
   
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.pack(expand=True)
        
    def create_widgets(self):
        # 현재 파일의 디렉터리 경로 가져오기:# /Users/irene/_Proj/_FSD_Project/GUIUniApp/src/frames
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 이미지 로고
        logo_path = os.path.join(current_dir, "uts_w_logo.png")
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((50, 50), Image.Resampling.LANCZOS)  # 이미지 크기 조정
        logo_img = ImageTk.PhotoImage(logo_image)

        # 메인 프레임 생성
        main_frame = tk.Frame(self, bg='white')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 로고와 텍스트를 함께 표시하는 라벨 생성
        self.logo_label = tk.Label(main_frame, text="Student Portal", image=logo_img, compound=tk.LEFT, padx=10, fg='#000000', font="Arial 26 bold", bg='white')
        self.logo_label.image = logo_img
        self.logo_label.pack(pady=(80, 20))

        # 로그인 박스 생성
        login_box = tk.Frame(main_frame, bg='white', padx=20, pady=20)
        login_box.place(relx=0.5, rely=0.3, anchor=tk.N)

        # 이메일, 비밀번호 레이블 및 입력 필드 생성
        # label
        self.email_label = tk.Label(login_box, text="Email:", justify='left', fg='#000000', font="Arial 14 bold", bg='white')
        self.password_label = tk.Label(login_box, text="Password:", justify='left', fg="#000000", font="Arial 14 bold", bg='white')
        self.email_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        self.password_label.grid(row=2, column=0, sticky=tk.W, pady=(20, 10))

        # entry
        emailText = tk.StringVar()
        self.email_entry = tk.Entry(login_box, width=30, textvariable=emailText, font="Arial 14 bold", relief=tk.GROOVE, highlightthickness=2, highlightbackground="gray")
        passwordTxt = tk.StringVar()
        self.password_entry = tk.Entry(login_box, width=30, textvariable=passwordTxt, font="Arial 14 bold", show='*', relief=tk.GROOVE, highlightthickness=2, highlightbackground="gray")
        self.email_entry.grid(row=1, column=0, padx=5, pady=(0, 5))
        self.email_entry.focus()
        self.password_entry.grid(row=3, column=0, padx=5, pady=(0, 30))
        self.password_entry.focus()

       # 버튼 생성
        button_frame = tk.Frame(login_box, bg='white')
        button_frame.grid(row=4, column=0, pady=(0, 20))

        # 버튼 스타일 설정
        button_style = {'font': 'Arial 14 bold',
                        'width': 10,
                        'height' : 10,
                        'relief': tk.GROOVE,
                        'borderwidth': 5,
                        'border_color': '#4d4f4e',
                        'bg_color': '#9eada2',
                        'fg_color': '#020303',
                        'active_bg_color': '#0056b3',
                        'active_fg_color': 'white',
                        'hover_bg_color': '#0069d9',
                        'hover_fg_color': '#293e85'}

        self.login_button = tk.Button(button_frame, text="Login", command=self.login)
        self.login_button.pack(side=tk.LEFT, padx=(0, 10))

        # self.register_button = tk.Button(button_frame, text="Register", command=self.register)
        # self.register_button.pack(side=tk.RIGHT)

        # 버튼 스타일 적용
        for button in [self.login_button]:
            button.configure(font=button_style['font'],
                            width=button_style['width'],
                            height=button_style['width'],
                            relief=button_style['relief'],
                            borderwidth=button_style['borderwidth'],
                            bg=button_style['bg_color'],
                            fg=button_style['fg_color'],
                            activebackground=button_style['active_bg_color'],
                            activeforeground=button_style['active_fg_color'])
            
            button.bind("<Enter>", lambda event, btn=button: btn.configure(bg=button_style['hover_bg_color'], fg=button_style['hover_fg_color']))
            button.bind("<Leave>", lambda event, btn=button: btn.configure(bg=button_style['bg_color'], fg=button_style['fg_color']))
                    
    def login(self):
        print("Login method entered")  # Debug print
        # logger.info("Login method entered")
       
        email = self.email_entry.get()
        password = self.password_entry.get()
    
        print(email) 
        print(password) 
          
        if self.controller.authenticate(email, password):
            print("Authentication successful")  # Debug print
            self.controller.show_enrolment_frame()
        else:
            print("Authentication failed - showing message")  # Debug print
            messagebox.showerror("Login Failed", "Incorrect credentials")
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        print("Login method exited")  # Debug print

    # def register(self):
    #     print("Register method entered") # Debug print
    #     self.controller.show_registration_frame()



# class RegistrationFrame(tk.Frame):
#     def __init__(self, master, controller):
#         super().__init__(master)
#         self.controller = controller
#         self.configure_gui()
#         self.create_widgets()
#     def configure_gui(self):
#         self.pack(padx=20, pady=20)
        
#     def create_widgets(self):
#         self.email_label = tk.Label(self, text="Email:")
#         self.email_entry = tk.Entry(self)
#         self.password_label = tk.Label(self, text="Password:")
#         self.password_entry = tk.Entry(self, show="*")
#         self.name_label = tk.Label(self, text="Name:")  
#         self.name_entry = tk.Entry(self)  
#         self.student_id_label = tk.Label(self, text="Student ID:") 
#         self.student_id_entry = tk.Entry(self)  
#         self.register_button = tk.Button(self, text="Register")
#         self.register_button.bind('<Button-1>', lambda event: self.register())
#         self.cancel_button = tk.Button(self, text="Cancel")
#         self.cancel_button.bind('<Button-1>', lambda event: self.cancel())

#         # Layout management
#         self.email_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
#         self.email_entry.grid(row=0, column=1, padx=5, pady=5)
#         self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
#         self.password_entry.grid(row=1, column=1, padx=5, pady=5)
#         self.name_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')  
#         self.name_entry.grid(row=2, column=1, padx=5, pady=5)  
#         self.student_id_label.grid(row=3, column=0, padx=5, pady=5, sticky='e') 
#         self.student_id_entry.grid(row=3, column=1, padx=5, pady=5)  
#         self.register_button.grid(row=4, column=0, padx=5, pady=5)
#         self.cancel_button.grid(row=4, column=1, padx=5, pady=5)

#     def register(self):
#         email = self.email_entry.get()
#         password = self.password_entry.get()
#         name = self.name_entry.get()
#         student_id = self.student_id_entry.get()

#         # 컨트롤러를 통해 등록 로직 호출
#         message = self.controller.register_student(email, password, name, student_id)
#         if message == "Registration successful":
#             messagebox.showinfo("Success", "Registration successful")
#         else:
#             messagebox.showerror("Error", message)

#         # 입력 필드 초기화
#         self.email_entry.delete(0, tk.END)
#         self.password_entry.delete(0, tk.END)
#         self.name_entry.delete(0, tk.END)
#         self.student_id_entry.delete(0, tk.END)
        
        
#     def cancel(self):
#         """Handles the cancel action to return to the login screen."""
#         self.controller.show_login_frame()


class EnrolmentFrame(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.pack(padx=20, pady=20)

    def create_widgets(self):
        # 로그인한 학생 정보 표시
        student = self.controller.logged_in_user
        student_info = f"Student: {student.name}, ID: {student.student_id}"
        self.info_label = tk.Label(self, text=student_info)
        self.info_label.pack()

        # 과목 등록 버튼
        self.enrol_button = tk.Button(self, text="Enrol Subject", command=self.enrol_subject)
        self.enrol_button.pack()

        # 과목 리스트 박스
        self.subjects_listbox = tk.Listbox(self, width=50, height=10)
        self.subjects_listbox.pack(pady=(20, 0))

        # 과목 삭제 버튼
        self.delete_button = tk.Button(self, text="Delete Subject", command=self.delete_subject)
        self.delete_button.pack()

        self.update_subjects()

    def enrol_subject(self):
        try:
            result = self.controller.enrol_subject()
            self.update_subjects_list()
            messagebox.showinfo("Success", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_subject(self):
        subject_id = self.subjects_listbox.get(self.subjects_listbox.curselection())
        result = self.controller.remove_subject(subject_id)
        self.update_subjects_list()
        messagebox.showinfo("Notice", result)

    def update_subjects_list(self):
        self.subjects_listbox.delete(0, tk.END)
        subjects = self.controller.get_enrolled_subjects()
        for subject in subjects:
            self.subjects_listbox.insert(tk.END, f"{subject.id} - {subject.name}")