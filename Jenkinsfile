pipeline {
    agent any

    stages {
        stage('SonarQube analysis') {
            steps {
                withSonarQubeEnv('sonar') {
                    sh '/var/jenkins_home/tools/hudson.plugins.sonar.SonarRunnerInstallation/sonarscanner/bin/bin/sonar-scanner -Dsonar.projectKey=apijava -Dsonar.host.url=http://192.168.0.7:9000 -Dsonar.token=squ_e2e490d146135e8d18775d4dd1d3c23a4f463186'
                }
            }
        }
        stage("Quality Gate") {
            steps {
                // Этот шаг ожидает завершения анализа и возвращает статус Quality Gate
                timeout(time: 2, unit: 'MINUTES') { 
                    script {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        }
                    }
                }
            }
        }
        stage('Develop') {
            steps {
                echo 'Develop commit'
            }
        }
        stage('Testing') {
            steps {
                echo 'Now is test code'
            }
        }
        stage('Deploy to prod') {
            steps {
                echo 'Deploy app to production'
            }
        }
    }
}
