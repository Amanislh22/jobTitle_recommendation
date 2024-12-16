import tkinter as tk
from tkinter import ttk, messagebox
from experta import *
import random

class JobRecommendation(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        yield Fact(action="find_job")

    # Fact declaration methods
    @Rule(Fact(action='find_job'), NOT(Fact(skills=W())), salience=1)
    def jobSkills(self):
        self.declare(Fact(skills=self.skills))

    @Rule(Fact(action='find_job'), NOT(Fact(interests=W())), salience=1)
    def jobInterests(self):
        self.declare(Fact(interests=self.interests))

    @Rule(Fact(action='find_job'), NOT(Fact(academic_field=W())), salience=1)
    def jobAcademicField(self):
        self.declare(Fact(academic_field=self.academic_field))

    @Rule(Fact(action='find_job'), NOT(Fact(certification=W())), salience=1)
    def jobCertification(self):
        self.declare(Fact(certification=self.certification))

    # Job Recommendation Rules
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

    @Rule(Fact(action='find_job'), Fact(certification="Cisco Certified Network Associate"), Fact(skills="Networking"), Fact(interests="Network Administration"), Fact(academic_field="Engineering"))
    def r13(self):
        self.declare(Fact(jobTitle="Network Engineer"))

    @Rule(Fact(action='find_job'), Fact(certification="Certified Ethical Hacker"), Fact(interests="Cybersecurity"), Fact(academic_field="Engineering"))
    def r14(self):
        self.declare(Fact(jobTitle="Ethical Hacker"))

    @Rule(Fact(action='find_job'), Fact(certification="AWS Certified Solutions Architect"), Fact(interests="Cloud Computing"))
    def r15(self):
        self.declare(Fact(jobTitle="Cloud Architect"))

    @Rule(Fact(action='find_job'), Fact(jobTitle=MATCH.job), salience=-998)
    def recommendJob(self, job):
        self.recommended_job = job

    @Rule(Fact(action='find_job'), NOT(Fact(jobTitle=MATCH.job)), salience=-999)
    def noJobRecommendation(self):
        self.recommended_job = "No suitable job title found"

class JobRecommendationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Career Compass: Job Recommendation System")
        self.master.geometry("1100x750")
        self.master.configure(bg="#F5F7FA")  # Soft light blue background

        # Variables to store selection
        self.skills_var = tk.StringVar()
        self.interests_var = tk.StringVar()
        self.academic_field_var = tk.StringVar()
        self.certification_var = tk.StringVar()

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

        # Create UI Components
        self.create_main_frame()
        self.create_header()
        self.create_input_section()
        self.create_submit_button()

    def configure_styles(self):
        # Modern, clean color palette
        self.style.configure("TLabel", 
            font=("Inter", 12), 
            background="#F5F7FA", 
            foreground="#2C3E50"
        )
        self.style.configure("Title.TLabel", 
            font=("Inter", 24, "bold"), 
            foreground="#3498DB"  # Vibrant blue for title
        )
        self.style.configure("TCombobox", 
            font=("Inter", 10), 
            padding=6,
            background="#FFFFFF",
            fieldbackground="#FFFFFF"
        )
        self.style.configure("TButton", 
            font=("Inter", 12, "bold"), 
            padding=10,
            background="#3498DB",
            foreground="#FFFFFF"
        )
        self.style.map("TButton", 
            background=[('active', '#2980B9'), ('pressed', '#2471A3')]
        )

    def create_main_frame(self):
        # Create a main container with a subtle shadow effect
        self.main_frame = tk.Frame(
            self.master, 
            bg="#FFFFFF", 
            borderwidth=1, 
            relief=tk.FLAT
        )
        self.main_frame.pack(
            pady=20, 
            padx=20, 
            fill='both', 
            expand=True
        )
        self.main_frame.configure(highlightbackground="#E0E0E0", highlightcolor="#E0E0E0", highlightthickness=1)

    def create_header(self):
        header_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        header_frame.pack(pady=20, padx=20, fill='x')

        title_label = ttk.Label(
            header_frame, 
            text="Career Compass", 
            style="Title.TLabel",
            background="#FFFFFF"
        )
        title_label.pack()

        subtitle_label = ttk.Label(
            header_frame, 
            text="Discover Your Ideal Career Path",
            font=("Inter", 14),
            background="#FFFFFF",
            foreground="#7F8C8D"  # Soft gray
        )
        subtitle_label.pack(pady=(5,0))

    def create_input_section(self):
        input_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        input_frame.pack(pady=20, padx=40, fill='both', expand=True)

        # Skills Column
        skills_frame = self.create_input_column(
            input_frame, 
            "Skills", 
            self.skills_var,
            ["Python", "Leadership", "Java", "Communication", 
             "Security Analysis", "Networking", "Management"]
        )
        skills_frame.grid(row=0, column=0, padx=10, sticky='nsew')

        # Interests Column
        interests_frame = self.create_input_column(
            input_frame, 
            "Interests", 
            self.interests_var,
            ["Software Development", "Data Science", "Marketing", 
             "Customer Support", "Cybersecurity", "Network Administration"]
        )
        interests_frame.grid(row=0, column=1, padx=10, sticky='nsew')

        # Academic Field Column
        academic_frame = self.create_input_column(
            input_frame, 
            "Academic Field", 
            self.academic_field_var,
            ["Computer Science", "Business", "Engineering"]
        )
        academic_frame.grid(row=0, column=2, padx=10, sticky='nsew')

        # Certifications Column
        cert_frame = self.create_input_column(
            input_frame, 
            "Certifications", 
            self.certification_var,
            ["Certified Ethical Hacker", "AWS Solutions Architect", 
             "Cisco Network Associate", "CISSP","None"]
        )
        cert_frame.grid(row=0, column=3, padx=10, sticky='nsew')

        input_frame.columnconfigure((0,1,2,3), weight=1)

    def create_input_column(self, parent, title, var, values):
        frame = tk.Frame(parent, bg="#FFFFFF", borderwidth=1, relief=tk.FLAT)
        
        title_label = ttk.Label(
            frame, 
            text=title, 
            font=("Inter", 14, "bold"),
            background="#FFFFFF",
            foreground="#2C3E50"
        )
        title_label.pack(pady=(0,10))

        combobox = ttk.Combobox(
            frame, 
            textvariable=var,
            values=values, 
            state="readonly", 
            width=25,
            style="TCombobox"
        )
        combobox.pack(pady=5)

        return frame

    def create_submit_button(self):
        button_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        button_frame.pack(pady=20)

        submit_button = ttk.Button(
            button_frame, 
            text="Find My Career", 
            command=self.process_recommendation,
            style="TButton"
        )
        submit_button.pack()

    def process_recommendation(self):
        # Validate all inputs are selected
        if not all([
            self.skills_var.get(), 
            self.interests_var.get(), 
            self.academic_field_var.get(), 
            self.certification_var.get()
        ]):
            messagebox.showwarning("Incomplete Information", "Please select all fields.")
            return

        # Create expert system engine
        engine = JobRecommendation()
        
        # Set attributes for the engine
        engine.skills = self.skills_var.get()
        engine.interests = self.interests_var.get()
        engine.academic_field = self.academic_field_var.get()
        engine.certification = self.certification_var.get()
        
        # Reset and run the engine
        engine.reset()
        engine.run()

        # Get the recommended job
        recommended_job = getattr(engine, 'recommended_job', "No suitable job found")
        
        # Show recommendation
        self.show_recommendation(recommended_job)

    def show_recommendation(self, job):
        result_window = tk.Toplevel(self.master)
        result_window.title("Career Recommendation")
        result_window.geometry("600x400")
        result_window.configure(bg="#FFFFFF")

        description_text = {
            "Software Developer": "Craft innovative software solutions and bring ideas to life through code.",
            "Data Analyst": "Transform raw data into meaningful insights that drive business decisions.",
            "Network Engineer": "Design and maintain robust computer networks that keep organizations connected.",
            "Cybersecurity Specialist": "Protect digital assets and defend against emerging cyber threats.",
            "Cloud Architect": "Design and manage scalable cloud computing systems for modern enterprises.",
            "Marketing Manager": "Lead marketing strategies and drive business growth.",
            "Customer Support Specialist": "Provide exceptional customer service and support.",
            "Full Stack Developer": "Build comprehensive web applications from front-end to back-end.",
            "Embedded Systems Engineer": "Design and develop embedded systems for various technologies.",
            "Ethical Hacker": "Identify and resolve security vulnerabilities proactively.",
            "Backend Developer": "Develop server-side logic and integrate with databases and applications.",
            "No suitable job found": "Based on your profile, we couldn't find an exact match. Consider exploring related fields or adjusting your selections."
        }

        # Title Frame
        title_frame = tk.Frame(result_window, bg="#3498DB", padx=20, pady=10)
        title_frame.pack(fill='x')

        ttk.Label(
            title_frame, 
            text="Your Recommended Career Path", 
            font=("Inter", 16, "bold"),
            foreground="#FFFFFF",
            background="#3498DB"
        ).pack()

        # Content Frame
        content_frame = tk.Frame(result_window, bg="#FFFFFF", padx=20, pady=20)
        content_frame.pack(fill='both', expand=True)

        ttk.Label(
            content_frame, 
            text=job, 
            font=("Inter", 22, "bold"), 
            foreground="#2C3E50"
        ).pack(pady=10)

        ttk.Label(
            content_frame, 
            text=description_text.get(job, "An exciting career awaits you!"),
            wraplength=500,
            font=("Inter", 14),
            foreground="#34495E"
        ).pack(pady=20)

def main():
    root = tk.Tk()
    app = JobRecommendationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()