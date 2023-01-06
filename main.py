from tkinter import *
from tkinter import ttk
from csv  import *
import tkinter.messagebox

class Selector(Tk):
    
    subs = []
    rooms = []
    
    @staticmethod
    def backtracking(assignment, slots, depth):
        if (depth == len(assignment)):             
            return True                             
        
        sub = Selector.subs[depth][0]                                            
        available = Selector.subs[depth][2:]               
        category = Selector.subs[depth][1]                  
        if (category == "c"):                                          
            for slot in available:
                if (slots[slot] == -1):             
                    assignment[depth] = [sub, slot, Selector.rooms[0]]      
                    slots[slot] = Selector.rooms[0]                       
                    if (Selector.backtracking(assignment, slots, depth+1)):
                        return True              
                    else:
                        slots[slot] = -1                  
                        assignment[depth] = [sub, -1, -1]  
            else:
                return False                        
            
        elif (category == "o"):                   
            for slot in available:                  
                if (slots[slot] == -1):            
                    assignment[depth] = [sub, slot, Selector.rooms[0]] 
                    slots[slot] = [Selector.rooms[0]]      
                    if (Selector.backtracking(assignment, slots, depth+1)):
                        return True                
                    else:
                        slots[slot] = -1
                        assignment[depth] = [sub, -1, -1]
                elif (type(slots[slot]) == list):
                    asRooms = slots[slot]
                    temp = asRooms[:]
                    if (len(asRooms) == len(Selector.rooms)):
                        continue
                    asRooms.append(Selector.rooms[len(asRooms)])
                    assignment[depth] = [sub, slot, asRooms[-1]]
                    slots[slot] = asRooms
                    if (Selector.backtracking(assignment, slots, depth+1)):
                        return True
                    else:
                        slots[slot] = temp
                        assignment[depth] = [sub, -1, -1]
            else:
                return False
   
   
   
    def __init__(self, title="My Window", icon="", max_width= 450, max_height=300, windowbg="#FFFFFF"):
        
            # ================================== Setting up the Screen =====================================================
            
            
        #Calling window        
        super().__init__()
        super().title(title)

        #Resizing Window
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.center_width = int((self.screen_width/2) - (max_width/2))
        self.center_height = int((self.screen_height/2) - (max_height/2))
        super().geometry(f"{max_width}x{max_height}+{self.center_width}+{self.center_height}")

        # Configuring Window
        # super().iconbitmap(icon)
        super().maxsize(width=max_width, height=max_height)
        super().minsize(width=max_width, height=max_height)
        super().config(background=(windowbg))

        # =============================== Defining =================================

        self.total_courses = IntVar()
        self.total_classes = IntVar()

        # ================================== Placing Entries =====================================================

        self.main_frame = Frame(self, bg=windowbg, height="250", width="400", relief=FLAT)

        self.course_frame = LabelFrame(self.main_frame, text="Enter Total Number of Courses", bg=windowbg, height="100", width="300", labelanchor="n", relief=FLAT, font="18")

        self.entry_courses = Entry(self.course_frame, bg="lightyellow", textvar=self.total_courses, font=("Times New Roman", 16), relief=SOLID, width=23, ).pack(anchor=CENTER, pady=15, padx=5)

        self.course_frame.pack(padx=30, pady=10)


        self.class_frame = LabelFrame(self.main_frame, text="Enter Total Number of Classes", bg=windowbg, height="100", width="300", labelanchor="n", relief=FLAT, font="18")

        self.entry_classes = Entry(self.class_frame, bg="lightyellow", textvar=self.total_classes, font=("Times New Roman", 16), relief=SOLID, width=23, ).pack(anchor=CENTER, pady=15, padx=5)

        self.class_frame.pack(padx=30, pady=10)


        self.button = Button(self.main_frame, text="Next Screen", font=("Times New Roman", 15), width=20, height=50, bg=windowbg, justify=CENTER, command=self.scr_change).pack(padx=30, pady=10)

        self.main_frame.pack(padx=30, pady=20)

        self.mainloop()
        
    def scr_change(self):
        if (self.total_courses.get()<8 and self.total_courses.get()>4)   and (self.total_classes.get()<8 or self.total_classes.get()>1):
            self.destroy()
            check_height = 0
            height_dict = {(5,4):480, (5,8):540, (6,4):540, (6,8):600, (7,4):600, (7,8):660}
            if self.total_classes.get()<=4:
                check_height = 4
            else:
                check_height = 8
            
            title="My Window"
            icon=""
            max_width= 1000
            max_height= height_dict[(self.total_courses.get(), check_height)]
            windowbg="#FFFFFF"
            
            
            
            #Calling window        
            super().__init__()
            super().title(title)

            #Resizing Window
            self.screen_width = self.winfo_screenwidth()
            self.screen_height = self.winfo_screenheight()
            self.center_width = int((self.screen_width/2) - (max_width/2))
            self.center_height = int((self.screen_height/2) - (max_height/2))
            super().geometry(f"{max_width}x{max_height}+{self.center_width}+{self.center_height}")

            # Configuring Window
            # super().iconbitmap(icon)
            super().maxsize(width=max_width, height=max_height)
            super().minsize(width=max_width, height=max_height)
            super().config(background=(windowbg))
            
            
            self.c1 = StringVar()
            self.c2 = StringVar()
            self.c3 = StringVar()
            self.c4 = StringVar()
            self.c5 = StringVar()
            self.c6 = StringVar()
            self.c7 = StringVar()
            self.c8 = StringVar()


            self.o1 = StringVar()
            self.o2 = StringVar()
            self.o3 = StringVar()
            self.o4 = StringVar()
            self.o5 = StringVar()
            self.o6 = StringVar()
            self.o7 = StringVar()
            self.o8 = StringVar()

            self.d1 = StringVar()
            self.d2 = StringVar()
            self.d3 = StringVar()
            self.d4 = StringVar()
            self.d5 = StringVar()
            self.d6 = StringVar()
            self.d7 = StringVar()
            self.d8 = StringVar()

            self.s1 = StringVar()
            self.s2 = StringVar()
            self.s3 = StringVar()
            self.s4 = StringVar()
            self.s5 = StringVar()
            self.s6 = StringVar()
            self.s7 = StringVar()
            self.s8 = StringVar()

            self.r1 = StringVar()
            self.r2 = StringVar()
            self.r3 = StringVar()
            self.r4 = StringVar()
            self.r5 = StringVar()
            self.r6 = StringVar()
            self.r7 = StringVar()
            self.r8 = StringVar()


            self.course = [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7]
            self.optional = [self.o1, self.o2, self.o3, self.o4, self.o5, self.o6, self.o7]
            self.days = [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7]
            self.slots = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7]
            self.room = [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7]
            
            
            main_frame = Frame(self, width=max_width, height=max_height, bg=windowbg)

            f1 = LabelFrame(main_frame, text="Enter Course Details", bg=windowbg, font=("Times New Roman",17), labelanchor="n")

            for i in range(1, self.total_courses.get()+1):
                
                l1 = Label(f1, text=f"Course {i}", font="lucida 13", bg="white").grid(row=i-1, column=0, pady=10)
                
                concept_frame = Frame(f1, bg=windowbg)
                
                lab = Label(concept_frame, text="Course Name", font=("Times New Roman", 12), bg=windowbg).grid(row=0, column=0, pady=3, padx=10)
                e1 = Entry(concept_frame,textvar=self.course[i-1],font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=1, column=0, padx=10, pady= 3)
                
                lab = Label(concept_frame, text="Course Type", font=("Times New Roman", 12), bg=windowbg).grid(row=0, column=1, pady=3, padx=10)
                e1 = Entry(concept_frame,textvar=self.optional[i-1],font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=1, column=1, padx=10, pady= 3)
                
                lab = Label(concept_frame, text="Enter Day", font=("Times New Roman", 12), bg=windowbg).grid(row=0, column=2, pady=3, padx=10)
                e1 = Entry(concept_frame,textvar=self.days[i-1],font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=1, column=2, padx=10, pady= 3)
                
                lab = Label(concept_frame, text="Enter Slot", font=("Times New Roman", 12), bg=windowbg).grid(row=0, column=3, pady=3, padx=10)
                e1 = Entry(concept_frame,textvar=self.slots[i-1],font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=1, column=3, padx=10, pady= 3)

                concept_frame.grid(row=i-1, column=1, padx=18)
                
            f1.pack(padx=5)


            f2 = LabelFrame(main_frame, text="Enter Room Name", bg = windowbg, font=("Times New Roman",17), labelanchor="n")
            j = 0
            for i in range(self.total_classes.get()):
                if i > 3:
                    j = 2
                lab = Label(f2, text=f"Room Name {i+1}", font=("Times New Roman", 12), bg=windowbg).grid(row=j, column=i%4, pady=3, padx=24)
                e1 = Entry(f2,textvar=self.room[i],font="lucida 12",bg="lightyellow",relief=SOLID).grid(row=j+1, column=i%4, padx=24, pady= 3)

            f2.pack(padx=5, pady=5)

            but = Button(main_frame, text="Generate Table", font=("Times", 15), width=20, height=1, justify=CENTER, bg="white", command=self.generate_table).pack(pady=3)

            main_frame.pack(padx=20, pady=8)
        else:
            tkinter.messagebox.showerror("Error", "Classes should be in range 2-7 and courses should be in range 5-7")
        
        
    def generate_table(self):
        
        Selector.subs = []
        Selector.rooms = []
        
        for i in range(self.total_courses.get()):
            print(i)
            da = self.days[i].get().split(",")
            sl = self.slots[i].get().split(",")
           
            if len(da)==1 and len(sl)==1:
                Selector.subs.append([self.course[i].get(), self.optional[i].get(), self.days[i].get()+self.slots[i].get()])
            else:
                print(self.course[i].get())
                ti = []
                for j in range(len(da)):
                    ti.append(da[j]+sl[j])
                rand_list = [self.course[i].get(), self.optional[i].get()]   
                rand_list.extend(ti)
                Selector.subs.append(rand_list)
                
        for i in range(self.total_classes.get()):
            Selector.rooms.append(self.room[i].get())
        print(Selector.subs)
        print(Selector.rooms)
        slots = {}
        assignment = []
        for sub in Selector.subs:
            for slot in sub[2:]:
                if (slot not in slots):
                    slots[slot] = -1
            assignment.append([sub[0],-1,-1])
        print(assignment)
        final_result = Selector.backtracking(assignment, slots, 0)
        self.assignment = assignment
        if final_result:
            self.result_scr()
        else:
            tkinter.messagebox.showinfo("No Result", "The info you provided yields no successful result")
        
    
    def result_scr(self):
        
        self.top_scr = Toplevel(self)
        
        
        self.top_scr.title('Timetable')
        self.top_scr.geometry('1200x350')
        self.top_scr.config(bg="white")
        self.top_scr.maxsize(1200, 350)
        # heading stuff
        frame1 = Frame(self.top_scr, background="white")
        frame1.pack()
        Label(frame1, text = "Time Table", width=1200,bg="#009688", fg="white",  font=("Franklin Gothic Medium", 25)).pack(pady=20)

        # define columns
        columns = ('Days', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
        frame2 = Frame(self.top_scr)
        frame2.pack()

        # configure treeview
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 15,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        tree = ttk.Treeview(frame2, columns=columns, show='headings',style="mystyle.Treeview")

        # define headings
        tree.heading('Days', text='Rooms / Days')
        tree.heading('Monday', text='Monday')
        tree.heading('Tuesday', text='Tuesday')
        tree.heading('Wednesday', text='Wednesday')
        tree.heading('Thursday', text='Thursday')
        tree.heading('Friday', text='Friday')
        
        days_lab = {"Mo":1, "Tu":2, "We":3, "Th":4, "Fr":5}
        periods = {1:"8:30-9:20", 2:"9:20-10:10", 3:"10:10-11:00", 4:"11:30-12:20", 5:"12:20-13:10", 6:"14:00-14:50", 7:"14:50-15:40", 8:"15:40-16:30"}
        self.timetable = {}
        
        # add data to the treeview
        for sub in self.assignment:
            day = sub[1][:2]
            period = int(sub[1][-1])
            if sub[2] not in self.timetable.keys():
                self.timetable[sub[2]] = [" "]*5
            self.timetable[sub[2]][days_lab[day]-1] = sub[0]+" "+f"({periods[period]})"
            
            
        for table in self.timetable:
        
            tree.insert('', END, values=[table]+self.timetable[table])


        tree.grid(row=0, column=0, sticky='nsew')
        but  = Button(self.top_scr, text="Save", font=("Times", 15), bg="yellow", width=15, command=self.save)
        but.pack(pady=5)
        # add a scrollbar
        # scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=tree.yview)
        # tree.configure(yscroll=scrollbar.set)
        # scrollbar.grid(row=0, column=1, sticky='ns')
        
        self.top_scr.mainloop()      
    
    def save(self):
        final_table = []
        for table in self.timetable:
            final_table.append([table]+self.timetable[table])
        try:
            with open("output.csv", "w") as f:
                write = writer(f)
                write.writerow(['Rooms / Days', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
                for i in final_table:
                    write.writerow(i)
        except:
            tkinter.messagebox.showerror("File Error", "Please close the file and try again")
        
if __name__ == '__main__':
    main = Selector()
