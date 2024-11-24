# Appium Automation Testing Project

Follow the steps below to set up and run the tests.

1. **Install Python Requirements**:  
   Make sure you have Python 3.9+ installed on your system. Then, install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

2. **Place the App APK**:  
   Add your application APK to the following directory:  
   ```plaintext
   apk/app.apk
   ```  
   Ensure the file exists in this location before running the tests.

3. **Run the Tests**:  
   Execute the tests using `pytest` with the following command:  
   ```bash
   pytest -sv
   ```

---

### TO DO:
- Add more tests to cover additional scenarios.
- Integrate test reporting tools like [Allure](https://docs.qameta.io/allure/).
- Set up Docker for containerized execution and configure Continuous Integration (CI) pipelines.

**Notes**:
- Ensure Appium is running locally before executing the tests.
- Update the test configurations (e.g., APK path, desired capabilities) as needed.
- The connected Android device is recognized automatically with adb command `adb shell getprop ro.product.model`
