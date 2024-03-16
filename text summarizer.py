
from tkinter import *
import nltk  # Download required packages before running: nltk.download('punkt')

def summarize_text():
  """Summarizes the text entered in the input field"""
  inputText = input_text.get("1.0", "end-1c")
  # Preprocess text (remove stopwords, punctuation etc.) - This is a basic example
  sentences = nltk.sent_tokenize(inputText)
  filtered_sentences = [sentence for sentence in sentences if len(sentence) > 10]
  summary = ' '.join(filtered_sentences[:3])  # Pick top 3 sentences
  output_text.delete("1.0", "end-1c")
  output_text.insert("1.0", summary)

# Initialize the Tkinter window
window = Tk()
window.geometry("500x500")
window.title("Summarizer")

my_menu = Menu(window)
window.configure(menu = my_menu)

#this command is used to open a new window when you click about me
def our_command():
  newWindow = Toplevel(window)
  newWindow.title("about me")
  newWindow.geometry("400x400")
  #change the intro to something else
  label = Label(newWindow, text="hello, my name is prathampal singh \n make sure to follow me on github and linkedin ").pack()
  
  
  #settingswindow = SettingsWindow()

#class SettingsWindow:
 # def __init__(self):
  #  top = Toplevel()
   # self.window = Window(top)
    #self.window.pack()

#the about me button 
file_menu = Menu(my_menu)
my_menu.add_command(label="About Me", command=our_command)

#the exit button on the top right
exit_menu = Menu(my_menu)
my_menu.add_command(label="Exit", command=window.quit) #menu=exit_menu

# Input label and text field
input_label = Label(window, text="Enter Text to Summarize:", fg="red")
input_label.pack()
input_text = Text(window, width=60, height=15)
input_text.pack(padx=10, pady=10)

# Summarize button
summarize_button = Button(window, text="Summarize", bg="lightgreen", fg="red", command=summarize_text)
summarize_button.pack(padx=10, pady=10)

# Output label and text field
output_label = Label(window, text="Summary:", bg="lightgreen", fg="red")
output_label.pack(padx=10, pady=10)
output_text = Text(window, width=60, height=7,bg="lightgreen")
output_text.pack()

window.mainloop()
