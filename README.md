
# College Chatbot

A chatbot designed to help new and current college students by providing instant answers to queries about the college, courses, facilities, and other relevant information. It aims to make students' academic journey smoother by offering a user-friendly and accessible platform.

## Features

- **Instant Query Resolution**: Get quick responses about college courses, events, and facilities.
- **Course Information**: Detailed information about academic programs and subjects.
- **College Events**: Stay updated with the latest events happening in the college.
- **24/7 Assistance**: Available anytime for students to get information at their convenience.

## Technologies Used

- **Backend**: Python
- **Framework**: Flask (for web app)
- **Chatbot Engine**: [Insert your chosen NLP/Chatbot Engine like Rasa, DialogFlow, etc.]
- **Frontend**: HTML, CSS (Bootstrap or Tailwind)
- **Database**: [Insert if any, e.g., SQLite, Firebase]

## Installation

### Prerequisites

- Python (3.7 or higher)
- Flask
- [NLP Engine (e.g., Rasa, DialogFlow, etc.)]

### Steps to Run the Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vinaypandey11/college-chatbot.git
   cd college-chatbot
   ```

2. **Set up a Python virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   Run the following command to install all the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the chatbot engine:**

   - For **Rasa**:
     - Install Rasa and its dependencies:
       ```bash
       pip install rasa
       ```
     - Train the model:
       ```bash
       rasa train
       ```

   - For **DialogFlow** (if using):
     - Set up DialogFlow and connect the API.
   
5. **Run the Flask Application:**

   ```bash
   python app.py
   ```

6. **Access the chatbot:**

   Open your browser and visit `http://127.0.0.1:5000/` to interact with the chatbot.

## Usage

- Type your queries in the chat interface to receive information about college courses, events, and more.
- You can integrate the chatbot with your preferred communication platform (e.g., web, mobile).

## Contributing

Feel free to fork the repository, submit issues, or send pull requests to improve this project. Contributions are welcome!


## Snapshots
![chatbot1_page-0001](https://github.com/user-attachments/assets/b84e9900-b9a8-4f29-babd-f1be61e3eca7)
![chatbot2_page-0002](https://github.com/user-attachments/assets/4193b9df-fce5-4e0a-9b78-8467dae8d2e8)
![chatbot2_page-0001](https://github.com/user-attachments/assets/7cb7b87e-4bc6-4cea-997c-01036722e892)

