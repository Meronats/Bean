import tkinter as tk




users = []




class User:
  def __init__(self, username, password):
      self.username = username
      self.password = password


def register():
  username = username_entry.get()
  password = password_entry.get()
  user = User(username, password)
  users.append(user)
  print("Registration successful.")




def login():
  username = username_entry.get()
  password = password_entry.get()
  for user in users:
      if user.username == username and user.password == password:
          print("Login successful.")
          show_home_page()
          return True
  print("Invalid username or password.")




def show_home_page():
  login_frame.pack_forget()
  home_frame.pack()




def next_button_clicked():
  print("Next button clicked")




login_window = tk.Tk()
login_window.configure(bg='lightgray')




# Login frame
login_frame = tk.Frame(login_window, bg='lightgray')
login_frame.pack(pady=10)




# Username and password
username_label = tk.Label(login_frame, text="Username:", bg='lightgray')
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)




password_label = tk.Label(login_frame, text="Password:", bg='lightgray')
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)




# Login button
login_button = tk.Button(login_frame, text="Login", command=login, bg='green', fg='white')
login_button.grid(row=2, column=1, padx=5, pady=5)


# Home frame
home_frame = tk.Frame(login_window, bg='lightblue')


home_label = tk.Label(home_frame, text="Welcome to the Home Page!", bg='lightblue', fg='darkblue', font=('Arial', 16))
home_label.pack(pady=20)


# Information about Ethiopian coffee
coffee_info_label = tk.Label(home_frame, text="Discover the Rich World of Ethiopian Coffee", bg='lightblue', fg='darkblue', font=('Arial', 14))
coffee_info_label.pack(pady=10)


coffee_info_text = """Coffee was first found and discovered in Ethiopia, specifically in the region known as Kaffa.
The coffee plant, Coffea, is native to the highlands of Ethiopia and grows naturally in the region.
The story of its discovery is attributed to a goat herder named Kaldi, who observed his goats becoming
more energetic after consuming the berries from a certain tree. This led him to investigate further
and ultimately discover the stimulating effects of coffee.


People find it hard to choose Ethiopian coffee type because Lack of familiarity: Ethiopian coffee
varieties can be diverse and complex, with different regions and processing methods producing distinct
flavor profiles. For those who are not well-versed in coffee or have limited exposure to Ethiopian coffees,
the range of options can be overwhelming, leading to uncertainty about which coffee to choose.


Ethiopia is known for its "heirloom" coffee varieties, which are cultivated using traditional
methods and have genetic diversity due to their long history of cultivation. These heirloom varieties
produce a wide range of flavor profiles. Let us guide you through the roller coaster of finding your
next favorite coffee.
"""


coffee_info_label = tk.Label(home_frame, text=coffee_info_text, bg='lightblue', font=('Arial', 12), justify='left')
coffee_info_label.pack(pady=10)


# Next button
next_button = tk.Button(home_frame, text="Next", command=next_button_clicked, bg='blue', fg='white')
next_button.pack()


# Signup message
signup_message = tk.Label(login_window, text="Don't have an account? Sign up!", bg='lightgray')
signup_message.pack(pady=5)


# Signup button
signup_button = tk.Button(login_window, text="Signup", command=register, bg='blue', fg='white')
signup_button.pack()


login_window.mainloop()



















from flask import Flask, render_template, request


app = Flask(__name__)


class Coffee:
   def __init__(self, name, flavor, roast_level, brewing_method):
       self.name = name
       self.flavor = flavor
       self.roast_level = roast_level
       self.brewing_method = brewing_method


def recommend_ethiopian_coffee(user_preferences):
   # Sample Ethiopian coffees for recommendation
   ethiopian_coffees = [
       Coffee("Yirgacheffe", "Fruity", "Light", "Pour Over"),
       Coffee("Sidamo", "Chocolatey", "Medium", "French Press"),
       Coffee("Harrar", "Complex", "Medium-Dark", "Espresso Machine")
   ]


   # Filter Ethiopian coffees based on user preferences
   recommended_coffees = []
   for coffee in ethiopian_coffees:
       if (
           (user_preferences["flavor"] is None or coffee.flavor.lower() == user_preferences["flavor"].lower()) and
           (user_preferences["roast_level"] is None or coffee.roast_level.lower() == user_preferences["roast_level"].lower()) and
           (user_preferences["brewing_method"] is None or coffee.brewing_method.lower() == user_preferences["brewing_method"].lower())
       ):
           recommended_coffees.append(coffee)


   return recommended_coffees


@app.route('/', methods=['GET', 'POST'])
def home():
   if request.method == 'POST':
       flavor = request.form['flavor']
       roast_level = request.form['roast_level']
       brewing_method = request.form['brewing_method']


       user_preferences = {
           "flavor": flavor,
           "roast_level": roast_level,
           "brewing_method": brewing_method
       }


       recommended_coffees = recommend_ethiopian_coffee(user_preferences)


       return render_template('result.html', recommended_coffees=recommended_coffees)


   return render_template('index.html')


if __name__ == '__main__':
   app.run(debug=True)
