🥕 Bajaru Image Bot
Bajaru Image Bot is a Python-based utility designed to automate image processing for the Bajaru app. It resizes and compresses images into optimized WebP formats: 200x200 for thumbnails and 800x800 for product details.

🚀 Getting Started
Follow these steps to set up your environment and process your images.

🛠️ Step 1: Installation & Environment Setup
Open your terminal in the project root folder and run the following commands:

Create the Virtual Environment:

Bash
python -m venv venv
Activate the Environment:

Bash
venv\Scripts\activate
Install Dependencies:

Bash
pip install Pillow
Verify Setup:
Check if Pillow appears in the list:

Bash
pip list
📂 Step 2: Create Folder Structure
The bot expects a specific folder hierarchy to find your raw images. Please create the following folders in the root directory of the project:

Create a folder named raw.

Inside raw, create these two sub-folders:

detail_raw — Paste your high-resolution product images here.

thumbnail_raw — Paste your thumbnail images here.

🏃 Step 3: Run the Bot
Once your images are pasted into the folders above, simply run the batch file:

Bash
run_bajaru_env.bat
📊 What happens next?
Images in thumbnail_raw will be resized to 200x200 and saved to output/thumbnails.

Images in detail_raw will be resized to 800x800 and saved to output/details.

All output files will be converted to .webp for maximum compression and performance in the Bajaru app.

📁 Git Note
The venv/ folder and any images inside raw/ or output/ are ignored by Git to prevent the repository from becoming too large. Only the scripts and configuration are tracked.
