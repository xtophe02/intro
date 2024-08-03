# Project Two

## Setup

1. **Create a virtual environment:**

   ```sh
   py -m venv .venv
   ```

2. **Activate the virtual environment:**

   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```sh
     source .venv/bin/activate
     ```

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Start the application:**
   ```sh
   uvicorn project_two.books:app --reload
   ```

## Additional Information

- **Deactivating the virtual environment:**

  ```sh
  deactivate
  ```

- **Updating dependencies:**

  ```sh
  pip freeze > requirements.txt
  ```

- **Running tests:**
  ```sh
  pytest
  ```

For more detailed information, refer to the project documentation or contact the project maintainers.
