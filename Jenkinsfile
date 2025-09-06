pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                // Create virtual environment
                bat 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m venv venv'
                
                // Upgrade pip
                bat 'venv\\Scripts\\pip install --upgrade pip'
                
                // Install Selenium
                bat 'venv\\Scripts\\pip install selenium'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run your test file (example: test_selenium.py)
                bat 'venv\\Scripts\\python.exe test_selenium.py'
            }
        }
    }
}
