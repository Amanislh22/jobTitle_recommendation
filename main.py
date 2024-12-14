import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from experta import *
import random

root = tk.Tk()  # create root window
root.iconphoto(False, tk.PhotoImage(file='D:\Bureau\professionrecom\jobTitle_recommendation\icons\Job.png'))

jobResult = ""
skills = StringVar()
interests = StringVar()
academic_field = StringVar()
certification = StringVar()





class JobRecommendation(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        yield Fact(action="find_job")

    # ************ FACTS *******************

    @Rule(Fact(action='find_job'), NOT(Fact(skills=W())), salience=1)
    def jobSkills(self):
        self.declare(Fact(skills=skills.get()))  # first

    @Rule(Fact(action='find_job'), NOT(Fact(interests=W())), salience=1)
    def jobInterests(self):
        self.declare(Fact(interests=interests.get()))

    @Rule(Fact(action='find_job'), NOT(Fact(academic_field=W())), salience=1)
    def jobAcademicField(self):
        self.declare(Fact(academic_field=academic_field.get()))

    @Rule(Fact(action='find_job'), NOT(Fact(certification=W())), salience=1)
    def jobCertification(self):
        self.declare(Fact(certification=certification.get()))  # Récupère la certification si elle est fournie


    # ************ RULES *******************

    @Rule(Fact(action='find_job'), Fact(skills="Python"), Fact(interests="Software Development"), Fact(academic_field="Computer Science"))
    def r1(self):
        self.declare(Fact(jobTitle="Software Developer"))




    @Rule(Fact(action='find_job'), Fact(skills="Java"), Fact(interests="Backend Development"))
    def r4(self):
        self.declare(Fact(jobTitle="Backend Developer"))

    
    @Rule(Fact(action='find_job'), Fact(skills="Python"), Fact(interests="Data Science"), Fact(academic_field="Computer Science"))
    def r5(self):
        self.declare(Fact(jobTitle="Data Analyst"))

    @Rule(Fact(action='find_job'), Fact(skills="Leadership"), Fact(interests="Marketing"), Fact(academic_field="Business"))
    def r6(self):
        self.declare(Fact(jobTitle="Marketing Manager"))

    @Rule(Fact(action='find_job'), Fact(skills="Communication"), Fact(interests="Customer Support"), Fact(academic_field="Business"))
    def r7(self):
        self.declare(Fact(jobTitle="Customer Support Specialist"))

    @Rule(Fact(action='find_job'), Fact(skills="Python"), Fact(interests="Software Development"), Fact(academic_field="Computer Science"))
    def r8(self):
        self.declare(Fact(jobTitle="Full Stack Developer"))

    @Rule(Fact(action='find_job'), Fact(skills="Security Analysis"), Fact(interests="Cybersecurity"), Fact(academic_field="Engineering"))
    def r9(self): 

        self.declare(Fact(jobTitle="Cybersecurity Specialist"))

   

    @Rule(Fact(action='find_job'), Fact(skills="Microcontrollers"), Fact(interests="Embedded Systems"), Fact(academic_field="Engineering"))
    def r11(self):
        self.declare(Fact(jobTitle="Embedded Systems Engineer"))

    @Rule(Fact(action='find_job'), Fact(skills="Networking"), Fact(interests="Network Administration"), Fact(academic_field="Computer Science"))
    def r12(self):
        self.declare(Fact(jobTitle="Network Engineer"))

    @Rule(Fact(action='find_job'),Fact(certification="Cisco Certified Network Associate"), Fact(skills="networking"), Fact(interests="Network Administration"), Fact(academic_field="Engineering"))
    def r13(self):
        self.declare(Fact(jobTitle="Network Engineer"))
    @Rule(Fact(action='find_job'), Fact(certification="Certified Ethical Hacker"), Fact(interests="Cybersecurity"), Fact(academic_field="Engineering"))
    def r14(self):
        self.declare(Fact(jobTitle="Ethical Hacker"))

    @Rule(Fact(action='find_job'), Fact(certification="AWS Certified Solutions Architect"), Fact(interests="Cloud Computing"))
    def r15(self):
        self.declare(Fact(jobTitle="Cloud Architect"))

    @Rule(Fact(action='find_job'), Fact(certification="Cisco Certified Network Associate"), Fact(interests="Network Administration"), Fact(academic_field="Engineering"))
    def r16(self):
        self.declare(Fact(jobTitle="Network Engineer"))

    @Rule(Fact(action='find_job'),Fact(skills="Networking"), Fact(certification="Certified Information Systems Security Professional"), Fact(interests="Cybersecurity"), Fact(academic_field="Engineering"))
    def r17(self):
        self.declare(Fact(jobTitle="Security Architect"))

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
    windowRes.iconphoto(False, PhotoImage(master=windowRes, file='D:\Bureau\professionrecom\jobTitle_recommendation\icons\Job.png'))
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

# Skills input using Combobox
groupe1 = Frame(left_frame, width=400, height=185, bg=bgFrames)
groupe1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Label(groupe1, text="Skills", bg=bgFrames, fg=textColors, font=("arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

skills.set(None)
skills_combobox = Combobox(groupe1, textvariable=skills, 
                           values=["Python", "Leadership", "Management", "Java", 
                                   "Communication", "Security Analysis", "C++", 
                                   "Microcontrollers", "Networking", "CCNA"], 
                           state="readonly")
skills_combobox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Interests input using Combobox
groupe2 = Frame(left_frame, width=400, height=185, bg=bgFrames)
groupe2.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
Label(groupe2, text="Interests", bg=bgFrames, fg=textColors, font=("arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

interests.set(None)
interests_combobox = Combobox(groupe2, textvariable=interests, 
                              values=["Software Development", "Data Science", "Marketing", 
                                      "Customer Support", "Backend Development", 
                                      "Cybersecurity", "Embedded Systems", 
                                      "Network Administration"], 
                              state="readonly")
interests_combobox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Academic Field input using Combobox
groupe3 = Frame(right_frame, width=400, height=185, bg=bgFrames)
groupe3.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Label(groupe3, text="Academic Field", bg=bgFrames, fg=textColors, font=("arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

academic_field.set(None)
academic_field_combobox = Combobox(groupe3, textvariable=academic_field, 
                                   values=["Computer Science", "Business", 
                                           "Engineering"], 
                                   state="readonly")
academic_field_combobox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Certifications input using Combobox
groupe4 = Frame(right_frame, width=400, height=185, bg=bgFrames)
groupe4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
Label(groupe4, text="Certification", bg=bgFrames, fg=textColors, font=("arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

certification.set(None)
certification_combobox = Combobox(groupe4, textvariable=certification, 
                                   values=["Certified Ethical Hacker", "AWS Certified Solutions Architect", 
                                           "Cisco Certified Network Associate", 
                                           "Certified Information Systems Security Professional"], 
                                   state="readonly")
certification_combobox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Submit button
submit_button = Button(footerFrame, text="Submit", width=30, height=2, bg=titleColor, fg="white", font=("arial", 10), relief="solid", command=openResultWindow)
submit_button.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()
