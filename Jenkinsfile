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
        bat '"C:/Users/Prethi/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/python.exe" --version'
        bat '"C:/Users/Prethi/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/python.exe" src\\app.py'
    }
}

stage('Test') {
    steps {
        bat '"C:/Users/Prethi/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/python.exe" -m unittest discover -s tests -v'
    }
}
        stage('Result') {
            steps {
                echo 'Build and test stages completed.'
            }
        }
    }
}