pipeline {
    agent any

    stages {
        stage('Develop') {
            steps {
                echo 'Develop commit'
            }
        }
        stage('Testing') {
            steps {
                echo 'Now is test code'
                sh 'cat hui.hui'
            }
        }
        stage('Deploy to prod') {
            steps {
                echo 'Deploy app to production'
            }
        }
    }
}
