
# PyQt5 Basic Web Browser

This repository contains a simple web browser built using PyQt5 and QWebEngineView. The application includes basic navigation functionality such as navigating to URLs, going back and forward in the browsing history, and reloading the page. The default start page is set to Google.

## Features
- **Base URL**: Starts with Google (`https://www.google.com`) as the home page.
- **URL Bar**: Enter a URL and press "Enter" or click the "Go" button to navigate.
- **Navigation Buttons**:
  - **Back**: Navigate back to the previous page.
  - **Forward**: Navigate forward to the next page.
  - **Reload**: Reload the current page.

## Dependencies

To run this project, you need to have Python installed along with the following Python packages:

- PyQt5: `pip install PyQt5`
- PyQtWebEngine: `pip install PyQtWebEngine`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Vasanth-Kumar-3000/basic-browser.git
    ```

2. Navigate to the project directory:
    ```bash
    cd basic-pyqt-browser
    ```

3. Install the required dependencies:
    ```bash
    pip install PyQt5 PyQtWebEngine
    ```

4. Run the browser:
    ```bash
    python browser.py
    ```

## Usage

- Upon running the application, the window will open with Google as the default page.
- Enter any URL in the URL bar and press "Enter" or click "Go" to navigate.
- Use the `<` (Back) and `>` (Forward) buttons to move through your browser history.
- Click the "Reload" button to refresh the current page.

## File Structure

```
.
├── browser.py        # Main application code
├── README.md         # Project documentation
```

## Future Enhancements

- Adding bookmarks functionality.
- Adding multiple tabs support.
- Adding a download manager.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

