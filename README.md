# URL Shortener Web Application

The URL Shortener web application is built using Flask, a Python web framework, to create short and easily shareable links for long URLs. Users can enter a long URL, optionally specify a custom short term, and obtain a shortened URL for easy sharing.

## Features

The application offers the following features:

- URL Shortening: Users can enter a long URL and receive a shortened version.

- Custom Short Terms: Users can optionally specify their own custom short terms for the URLs.

- Click Tracking: The application tracks the number of clicks on the shortened URLs.

## How to Run the Application

1. Clone the repository to your local machine.

2. Ensure you have Flask installed. If Flask is not installed, you can install it using `pip`:

   ```bash
   pip install flask
   ```

3. In the terminal, navigate to the project directory containing the `app.py` file.

4. Run the Flask application using the following command:

   ```bash
   python app.py
   ```

5. Once the application is running, open a web browser and go to `http://localhost:5000` to access the URL Shortener.

## Using the Application

### Shortening URLs

1. Open the web application in your browser.

2. Enter a long URL in the provided input field.

3. Optionally, specify a custom short term for the URL.

4. Click the "Shorten URL" button.

5. The shortened URL will be displayed on the page.

### Accessing Shortened URLs

1. To access a shortened URL, enter the short term in the browser's address bar after the application's base URL (e.g., `http://localhost:5000/short_term`).

2. You will be redirected to the original long URL associated with the short term.

### Click Tracking

The application tracks the number of clicks on the shortened URLs. You can monitor the click count for each URL.

### About and Contact Pages

The application also includes "About" and "Contact" pages to provide additional information and contact details.

## Acknowledgments

This URL Shortener is a useful tool for converting long, complex URLs into shorter, more manageable links. It can help you easily share links with others and monitor their usage.

Feel free to use, modify, and integrate this application into your projects or enhance it with additional features as needed.
