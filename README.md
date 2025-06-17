🧮 Flask Calculator
  A simple yet powerful Flask-based calculator that supports both mouse clicks and keyboard keystrokes for input. This web calculator is fast, responsive, and easy to use—designed for developers, students, and anyone who needs quick calculations on the go.


🚀 Try It Live
  👉 Click this link to use the calculator online :- https://rajesh5101x.pythonanywhere.com/


🔧 Features
  ✅ Built with Python and Flask  
  ✅ Handles basic arithmetic operations: +, -, *, /  
  ✅ Supports keyboard input for faster calculations  
  ✅ Responsive and clean UI  
  ✅ Real-time calculation feedback   


🖥️ Screenshots
  ![image](https://github.com/user-attachments/assets/8870c537-6c3d-4c56-bec1-0dcc3309d473)
  ![image](https://github.com/user-attachments/assets/53c2c9c2-240c-4287-b70d-779f30d359fe)
  ![image](https://github.com/user-attachments/assets/5800b949-4296-4224-ab8a-93a417ba53f8)


📂 Project Structure  
  calculator/  
  ├── templates/  
      └── layout.html      # Main template for nav bar   
      └── home.html   
      └── features.html   
      └── about.html   
      └── contact.html   
      └── calc.html        # This contain the main calculator logic   
      └── result.html      # This will show the final result   
  │   └── index.html       # Frontend interface   
  ├── app.py               # Main Flask application   
  └── README.md    


⚙️ How to Run Locally
  1.Clone the repository
    '''
    git clone https://github.com/Rajesh5101x/Python_Flask_calculator.git
    cd flask-calculator
    '''
    
  2.Create and activate virtual environment (optional)
    '''
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    '''

  3.Install dependencies
    '''
    pip install Flask
    '''

  4.Run the app
    '''
    python app.py
    '''

  5.Open http://127.0.0.1:5000 in your browser.


⌨️ Keyboard Support
  You can use the following keys directly in the calculator:
  Numbers: 0–9   
  Operations: +, -, *, /  
  Decimal: .   
  Enter / = to evaluate    
  Backspace to delete    
  C to clear  


📄 License
  This project is open-source and available under the MIT License.
