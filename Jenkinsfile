pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python --version'
                bat 'python src\\app.py'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover -s tests -v'
            }
        }

        stage('Result') {
            steps {
                echo 'Build and test stages completed.'
            }
        }
    }
}