# Import the setuptools library
import setuptools

# Read the README.md file to use as the long description for your package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of your package
__version__ = "0.0.0"

# Define metadata for your package
REPO_NAME = "Kidney-Disease-Classification-mlflow/DVC"
AUTHOR_USER_NAME = "ridabayi"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "bayi.rida@gmail.com"

# Use setuptools to define the setup for your package
setuptools.setup(
    # The name of your package
    name=SRC_REPO,
    
    # The version of your package
    version=__version__,
    
    # The author of your package
    author=AUTHOR_USER_NAME,
    
    # The author's email address
    author_email=AUTHOR_EMAIL,
    
    # A short description of your package
    description="A small python package for CNN app",
    
    # The long description of your package (read from README.md)
    long_description=long_description,
    
    # The format of the long description (Markdown)
    long_description_content_type="text/markdown",
    
    # The URL of your package's repository
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    
    # Additional URLs for your package (e.g. bug tracker)
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    
    # The directory containing your package's source code
    package_dir={"": "src"},
    
    # Automatically find and include all packages in the 'src' directory
    packages=setuptools.find_packages(where="src")
)