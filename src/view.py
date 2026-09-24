from PIL import Image
from customtkinter import *
import json
import src.controller as controller


with open('config/settings.json', 'r', encoding='utf-8') as settings:
    setting = json.load(settings)




set_appearance_mode(setting["set_theme_mode"])

class ToDoListApp(CTk):
    def __init__(self):
        CTk.__init__(self)
        self.resizable(False, False)
        self.geometry(f'{setting["win_width"]}x{setting["win_height"]}')
        self.title(setting["title"])

        self.top_image= CTkImage(light_image=Image.open(setting["top_image"]),
                                 size=(setting["win_width"],70))
        self.header= CTkLabel(master=self,image=self.top_image,text='')

        self.header.pack(fill=X,side=TOP)

        self.header_text= CTkLabel(master=self,text=setting['header']["text"],
                                   font=tuple(setting["header"]["font"]),
                                   text_color=setting["header"]["text_color"],
                                   fg_color=setting["header"]["fg_color"])

        self.header_text.place(relx=0.5,y=30,anchor=CENTER)




        self.todo_add_frame= CTkFrame(master=self,
                                      width=setting["win_width"],
                                      height=setting["entry_frame"]["height"],
                                      fg_color=setting["entry_frame"]["fg_color"])

        self.add_button= CTkButton(master=self.todo_add_frame,
                                   corner_radius=setting["add_button"]["corner_radius"],
                                   text=setting["add_button"]["text"],
                                   font=tuple(setting["add_button"]["font"]),
                                   compound=setting["add_button"]["compound"],
                                   command=self.add)

        self.todo_entry= CTkEntry(master=self.todo_add_frame,
                                  corner_radius=setting["todo_entry"]["corner_radius"],
                                  font=tuple(setting["todo_entry"]["font"]))
        self.list= ToDoScrollableFrame(self,controller.current_data)


        self.add_button.place(anchor=NW,relheight=1.0,relwidth=0.3,relx=0.7,y=0)

        self.todo_entry.place(anchor=NW,relheight=1.0,relwidth=0.7,x=0,y=0)



        self.delete_image = CTkImage(light_image=Image.open(setting["delete_button_img"]),
                                     size=(53, 53))
        self.delete_button = CTkButton(master=self,
                                       image=self.delete_image,
                                       text=setting["delete_button"]["text"],
                                       font=tuple(setting["delete_button"]["font"]),
                                       fg_color=setting["delete_button"]["fg_color"],
                                       hover_color=setting["delete_button"]["hover_color"],command=self.delete)

        self.delete_all_btn = CTkButton(master=self,
                                        text='Удалить всё',
                                        font=("Arial", 20, "bold"),
                                        fg_color='#956B11',
                                        command=self.delete_all)

        self.delete_button.pack(side=BOTTOM, pady=5)
        self.delete_all_btn.pack(side=BOTTOM)
        self.list.pack(side=BOTTOM,padx=10,fill=X)
        self.todo_add_frame.pack(side=BOTTOM, pady=10)

    def add(self):
        text = self.todo_entry.get()
        self.todo_entry.delete(0, END)
        controller.add_todo(self.list, text)
    def delete(self):
        controller.delete_todo(self.list)
    def delete_all(self):
        controller.delete_all_todo(self.list)

class ToDoScrollableFrame(CTkScrollableFrame):
    def __init__(self,window,list_item):
        CTkScrollableFrame.__init__(self,master=window)
        self.checkbox_list=[]
        self.show_list(list_item)

    def show_list(self,item):
        self.checkbox_list=[]

        for key, value in item.items():
            checkbox=CTkCheckBox(self,text=f'{key}:{value}')
            checkbox.pack(fill=X,pady=5)
            self.checkbox_list.append(checkbox)






