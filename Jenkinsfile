pipeline {
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Satwik-Samayamantry/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x 1.py"
                sh "./1.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    }
}
