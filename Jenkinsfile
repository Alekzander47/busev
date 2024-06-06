pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/omahire007/web-test.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t busev .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8000:8000 busev'
            }
        }
    }
}