pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Sanika25More/python-sel.git'
            }
        }
        stage('Setup Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install pytest selenium'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
}
