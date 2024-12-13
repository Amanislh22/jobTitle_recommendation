import tkinter as tk
from tkinter import *
from tkinter import messagebox
from experta import *
import random

root = tk.Tk()  # create root window
root.iconphoto(False, tk.PhotoImage(file='/home/ameni/jobTitle_recommendation/icons/Job.png'))

jobResult = ""
skills = StringVar()
interests = StringVar()
academic_field = StringVar()


class JobRecommendation(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        yield Fact(action="find_job")

    # ************ FACTS *******************
    
    # Skills (e.g., Python, Leadership, Management)
    @Rule(Fact(action='find_job'), NOT(Fact(skills=W())), salience=1)
    def jobSkills(self):
        self.declare(Fact(skills=skills.get()))  # first

    # Interests (e.g., Software Development, Data Science, Marketing)
    @Rule(Fact(action='find_job'), NOT(Fact(interests=W())), salience=1)
    def jobInterests(self):
        self.declare(Fact(interests=interests.get()))

    # Academic field (e.g., Computer Science, Business, Medicine)
    @Rule(Fact(action='find_job'), NOT(Fact(academic_field=W())), salience=1)
    def jobAcademicField(self):
        self.declare(Fact(academic_field=academic_field.get()))

    # ************ RULES *******************

    @Rule(Fact(action='find_job'), Fact(skills="Python"), Fact(interests="Software Development"))
    def r1(self):
        self.declare(Fact(jobTitle="Software Developer"))

    @Rule(Fact(action='find_job'), Fact(skills="Leadership"), Fact(interests="Management"))
    def r2(self):
        self.declare(Fact(jobTitle="Project Manager"))

    @Rule(Fact(action='find_job'), Fact(academic_field="Computer Science"), Fact(interests="Data Science"))
    def r3(self):
        self.declare(Fact(jobTitle="Data Scientist"))

    @Rule(Fact(action='find_job'), Fact(jobTitle=MATCH.job), salience=-998)
    def recommendJob(self, job):
        print("\nThe recommended job title for you is: " + job + "\n")
        global jobResult
        jobResult = job

    @Rule(Fact(action='find_job'), NOT(Fact(jobTitle=MATCH.job)), salience=-999)
    def noJobRecommendation(self):
        print("Need more information to make a decision\n")
        global jobResult
        jobResult = "No suitable job title found"

# ********************** MAIN PROGRAM ************************

# colors
backgroundvalue = "#F6F5F5"
bgFrames = "#D3E0EA"
textColors = "#1687A7"
optionsColor = "black"
titleColor = "#276678"
engine = JobRecommendation()

# Prepare function to display result
def openResultWindow():
    engine.reset()
    engine.run()

    windowRes = Tk()
    windowRes.title="Job Title Recommendation"
    windowRes.iconphoto(False, PhotoImage(master=windowRes, file='/home/ameni/jobTitle_recommendation/icons/Job.png'))
    windowRes.maxsize(700, 500)
    windowRes.config(bg=backgroundvalue)

    headFrame = Frame(windowRes, width=600, height=100, bg=backgroundvalue)
    headFrame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    BodyFrame = Frame(windowRes, width=700, height=300, bg=backgroundvalue)
    BodyFrame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

    if jobResult == "No suitable job title found":
        jobName = random.choice(["Data Analyst", "Software Engineer", "Marketing Specialist"])
        Label(headFrame, text="Sorry, we couldn't find a matching job title.", font=("arial italic", 10), bg=backgroundvalue, fg=titleColor).grid(row=0, column=1, padx=5, pady=5)
        Label(headFrame, text="But we recommend: ", font=("arial italic", 10), bg=backgroundvalue, fg=titleColor).grid(row=1, column=1, padx=5, pady=5)
        title1 = Label(headFrame, text=jobName, font=("arial italic", 18, "bold"), bg=backgroundvalue, fg=titleColor).grid(row=3, column=1, padx=5, pady=5)
    else:
        Label(headFrame, text="Based on your preferences, we recommend: ", font=("arial italic", 10), bg=backgroundvalue, fg=titleColor).grid(row=0, column=1, padx=5, pady=5)
        title1 = Label(headFrame, text=jobResult, font=("arial italic", 18, "bold"), bg=backgroundvalue, fg=titleColor).grid(row=2, column=1, padx=5, pady=5)

    windowRes.mainloop()

# Main window setup
root.title("Job Title Recommendation System")
root.maxsize(900, 700)
root.config(bg=backgroundvalue)

headFrame = tk.Frame(root, width=600, height=150, bg=backgroundvalue)
headFrame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

title1 = tk.Label(headFrame, text="Job Title Recommendation System", font=("arial italic", 18, "bold"), bg=backgroundvalue, fg=titleColor).grid(row=0, column=1, padx=5, pady=5)
subTitle1 = tk.Label(headFrame, text="Find the job title that suits your preferences.", font=("arial italic", 15), bg=backgroundvalue, fg=titleColor).grid(row=1, column=1, padx=5, pady=5)

BodyFrame = tk.Frame(root, width=600, height=400, bg=backgroundvalue)
BodyFrame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

# Create frames for user input (skills, interests, academic field)
left_frame = tk.Frame(BodyFrame, width=400, height=400, bg=bgFrames)
left_frame.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

right_frame = tk.Frame(BodyFrame, width=400, height=400, bg=bgFrames)
right_frame.grid(row=1, column=1, padx=20, pady=5, sticky="nsew")

# Footer
footerFrame = tk.Frame(root, width=600, height=150, bg=backgroundvalue)
footerFrame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

# Skills input
groupe1 = Frame(left_frame, width=400, height=185, bg=bgFrames)
groupe1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Label(groupe1, text="Skills", bg=bgFrames, fg=textColors, font=("arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

skills.set(None)
Radiobutton(groupe1, text="Python", variable=skills, value="Python", bg=bgFrames, fg=optionsColor).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Radiobutton(groupe1, text="Leadership", variable=skills, value="Leadership", bg=bgFrames, fg=optionsColor).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

# Interests input
groupe2 = Frame(left_frame, width=400, height=185, bg=bgFrames)
groupe2.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
Label(groupe2, text="Interests", bg=bgFrames, fg=textColors, font=("arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

interests.set(None)
Radiobutton(groupe2, text="Software Development", variable=interests, value="Software Development", bg=bgFrames, fg=optionsColor).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Radiobutton(groupe2, text="Data Science", variable=interests, value="Data Science", bg=bgFrames, fg=optionsColor).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

# Academic Field input
groupe3 = Frame(right_frame, width=400, height=185, bg=bgFrames)
groupe3.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Label(groupe3, text="Academic Field", bg=bgFrames, fg=textColors, font=("arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

academic_field.set(None)
Radiobutton(groupe3, text="Computer Science", variable=academic_field, value="Computer Science", bg=bgFrames, fg=optionsColor).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Radiobutton(groupe3, text="Business", variable=academic_field, value="Business", bg=bgFrames, fg=optionsColor).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

# Submit button
submit_button = Button(footerFrame, text="Submit", width=30, height=2, bg=titleColor, fg="white", font=("arial", 10), relief="solid", command=openResultWindow)
submit_button.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()
