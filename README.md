# Email Sender Program

This program sends an email to a recipient using Gmail's SMTP server.

## Requirements

To use this program, you need to have a Gmail account and create an app password specifically for this program. An app password is a 16-character password that gives access to your Gmail account from a non-Google app, such as this email sender program.:

1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords?).
2. Select the app you want to generate the app password for. In this case, select "Mail" from the drop-down menu.
3. Select the device you want to use the app password for. In this case, select "Other (Custom name)" and enter a name for your custom device.
4. Follow the on-screen instructions to generate the app password.
5. Copy the generated app password and use it as the email_password argument when running the program.

## Usage

To use the program, you need to:

1. Clone the repository.
2. Install the necessary requirements by running `pip install -r requirements.txt` in your terminal.
3. Open the `email_sender.py` file and update the following variables with your information:
   * `email_address`: Your Gmail address.
   * `email_password`: The app password you generated in the previous section.
   * `recipient`: The email address of the recipient.
   * `subject`: The subject of the email.
   * `body`: The body of the email.
4. Run the program by executing `python email_sender.py` in your terminal.
5. Open your terminal and navigate to the directory where the email_sender.py file is located.
6. Run the program by executing python email_sender.py in your terminal. The program will send the email using the information you provided.
