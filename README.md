1. It used to convert the pdf to tiff file.
2. Can be used to convet multi-pages pdf conversion.
3. Pick the pdf files from the source folder and creates a destination folder where it contains or  stored the .tiff files.

Before runnig the .py file, check the below dependencies whether the libary is already present or need to install.
For install the libary, run the below command in terminal:

--> pip install pdf2image pillow

Then you need to install the poppler utility which it relies on to read and convert PDF files.

You need to install Poppler and add it to your system's PATH.

✅ Step 1: Download Poppler for Windows
1. Go to: "https://github.com/oschwartz10612/poppler-windows/releases/"
2. Download the latest .zip file under "Assets" (e.g., poppler-xx_xx_xx.zip)
3. Extract it to a folder, e.g., C:\poppler

✅ Step 2: Add Poppler to System PATH
1. Press Win + S and search for “Environment Variables”
2. Click on “Edit the system environment variables”
3. In the System Properties window, click “Environment Variables”
4. Under “System variables”, find and select Path, then click “Edit”
5. Click “New” and add the path to the bin folder inside Poppler, e.g.:   C:\poppler\poppler-xx_xx_xx\Library\bin
6. Click OK on all windows to apply changes

✅ Step 3: Restart Your IDE or Terminal
Close and reopen your terminal or IDE (like PyCharm or VS Code) to apply the new PATH settings.

----
Try running this in your Python script or terminal to confirm:

# from pdf2image import convert_from_path
# images = convert_from_path("your.pdf", dpi=200)

If it runs without error, you're good to go!
